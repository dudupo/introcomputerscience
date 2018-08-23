#!/usr/bin/python

import script
import os , importlib


if __name__ == "__main__":
    args = os.sys.argv
    if len(args) > 1:
        exerice = "ex.ex{0}.ex{0}".format( args[1] )
        importlib.import_module(exerice).run()
