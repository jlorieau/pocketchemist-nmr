#!/bin/bash

nmrPipe () {
    pc --debug nmrpipe "$@"
    }

#nmrPipe -in test.fid \
#| nmrPipe -fn FT -auto 
# -ov -out out.ft2

nmrPipe -in test.fid \
| nmrPipe -fn FT -auto \
| nmrPipe -out -ov out.ft2


