#!/usr/bin/env bash
pretools="C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Tools\\MSVC\\14.14.26428\\bin\\Hostx86\\x86\\cl.exe"
powershell "&\"$pretools\" /P /C /Fitemp$1 $1"
python ./build.py ./temp$1 ./c$1
