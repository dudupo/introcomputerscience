import re , os
from copy import deepcopy as copy

if __name__ == "__main__" :
    _in = open(os.sys.argv[1]).read()
    _out = open("temp" +  os.sys.argv[1] , "w+")

    definepattern = "#define"


    substitutions = { }

    for x in re.finditer(r"#define\s*(\w+)(\((.*?)\))+(.*?)#enddef" , _in ,   re.DOTALL):
        if x :
            substitutions[x.group(1)] = ( x.group(3).split(',') , x.group(4))
            _in = _in.replace(x.group(0) , '')
    print (substitutions)

    for _mac , (args , replacement) in substitutions.items():
        for x in re.finditer(r"^(\s*){0}\s*(\((.*?)\))+".format(_mac), _in ,re.MULTILINE |re.DOTALL):
            temp = copy( replacement )
            for u , v in zip( x.group(3).split(',') , args ):
                temp = temp.replace(v , u)
            c =  x.group(1)
            #temp = temp.replace("\\\n" , "\\" + c )
            ttemp = temp.split("\n")
            temp = ""
            for W in ttemp[1:-2]:
                temp += c + W + "\n"
            temp += c + ttemp[-2]
            #temp = temp.replace("\n" ,"\n"+ c )
            _in = _in.replace(x.group(0), temp, 1)
    _out.write(_in)

    #    print(x.group(0))
    # for _ in range(4):
    #     print("{0} --->".format(_))
    #     print(.group(_))



    #print(re.search(r"#define.*\\\n" , _in , re.DOTALL).group(2))
    #for search, replacement in substitutions:
    #    _in = _in.replace(search, replacement)
    #_out.write(_in)
