
fullpath = 'C:\\Users\\david~ponar\\workspace\\introHW\\exercises\\exercises\\ex\\ex{0}.py'

def createExercies() :
    for i in range(2,20):
        open(fullpath.format(i) , 'x')