
import hangman_helper
import functools

def update_word_pattern(word, char, current_pattern):
    ret = ""
    for ichar ,jchar in zip(current_pattern , word):
        if ichar != '_' or char == jchar:
            ret += jchar
        else:
            ret += ichar
    return ret


def filter_words_list(words, pattern, wrong_geuss_lst):
    ret = []
    for word in words:
        ret.append(word)
        for ichar , jchar in zip(word, pattern):
           if (jchar != '_' and ichar != jchar) or ichar in wrong_geuss_lst:
               ret.pop()
               break
    return ret

def choose_letter(words, pattern):
    words_deg , _max , _maxchar = { } , 0 , words[0][0]
    for word in words:
        for char in word:
            if char in words_deg :
                words_deg[char] += 1
                if char not in pattern and _max < words_deg[char]:
                    _max , _maxchar = words_deg[char] , char
            else :
                words_deg[char] = 1
    return _maxchar

def run_single_game(words_list):
    random_word = hangman_helper.get_random_word( words_list ) 
    #random_word = "debug"
    wrong_guess_lst , guess = [ ] , [ ]
    error_count = 0 
    pattern = functools.reduce( lambda x , y :  x + y , [ '_' if char != ' ' else ' ' for char in random_word  ])
   
    PLAY = True
    msg = hangman_helper.DEFAULT_MSG

    while error_count < hangman_helper.MAX_ERRORS :
        hangman_helper.display_state(pattern , error_count, wrong_guess_lst,msg)
        input_type , value = hangman_helper.get_input()

        if input_type == hangman_helper.LETTER:
            if len(value) == 0 or value > 'z' or value < 'a':
                msg = hangman_helper.NON_VALID_MSG
            else:
                if value in guess:
                    msg = hangman_helper.ALREADY_CHOSEN_MSG
                else:
                    guess.append(value)
                    msg = hangman_helper.DEFAULT_MSG
                    if value in random_word:        
                        pattern = update_word_pattern(random_word, value, pattern)
                    else:
                        wrong_guess_lst.append(value)
                        error_count += 1
        if input_type == hangman_helper.HINT:
            msg = hangman_helper.HINT_MSG + choose_letter(filter_words_list(words_list, pattern, wrong_guess_lst), pattern)
   
    msg = hangman_helper.WIN_MSG if pattern == random_word else hangman_helper.LOSS_MSG + random_word
    hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, True)
    input_type , value = hangman_helper.get_input()
    if input_type == hangman_helper.PLAY_AGAIN:
        return value
    return False

def main():
    words_list  = hangman_helper.load_words()
    PLAY = True
    while PLAY:
        PLAY = run_single_game( words_list )

def run():
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()

if __name__ == "__main__":
    run()