#!/usr/bin/env python3

import sys

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def decrease_numbers(param):
    number = int(param)
    new_param = ""
    if number >= 0:
        for par in param:
            if par == "0":
                temp = "9"
            else:
                res = int(par) - 1
                temp = str(res)
            new_param = new_param + temp
            temp = ""
    elif number < 0:
        new_param = "-"
        for par in param[1:]:
            if par == "0":
                temp = "9"
            else:
                res = int(par) - 1
                temp = str(res)
            new_param = new_param + temp
            temp = ""
    return new_param

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    changed_param = ""
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
                if is_digit(param):
                    changed_param = decrease_numbers(param)
                print(changed_param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())