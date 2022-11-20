#!/usr/bin/env python3

import sys
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False
        
def my_printf(format_string,param):
    #print(format_string)
    t = ""
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
                if param.isdigit():
                    for par in param:
                        if par == "0":
                            temp = "9"
                        else:
                            res = int(par) - 1
                            temp = str(res)
                        t = t + temp
                        temp = ""
                print(t,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())