#!/usr/bin/env bash
python ./ex5.py ./part_a/word_list.txt ./part_a/mat.txt "y" ./out1.txt
python ./ex5.py ./part_a/word_list.txt ./part_a/mat.txt "u" ./out2.txt
python ./crossword3d.py ./part_b/word_list.txt ./part_b/mat_3d.txt "udlrwxyzb" ./out3.txt
python ./crossword3d.py ./part_b/word_list.txt ./part_b/mat_3d.txt "udlrwxyzc" ./out4.txt
python ./ex5.py ./part_a/word_list.txt ./part_a/mat.txt "udlrwxyz" ./out.txt
python ./crossword3d.py ./part_b/word_list.txt ./part_b/mat_3d.txt "udlrwxyzabc" ./out5.txt
