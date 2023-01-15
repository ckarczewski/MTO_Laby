#!/usr/bin/env python3

import sys
import re

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False




def hex_change(param):
    num = int(param)
    result = hex(num)

    params = str(result[2:])
    new_param = ""

    for par in params:
        if par.isdigit():
            new_param = new_param + par
        elif par == "a":
            par = "g"
            new_param = new_param + par
        elif par == "b":
            par = "h"
            new_param = new_param + par
        elif par == "c":
            par = "i"
            new_param = new_param + par
        elif par == "d":
            par = "j"
            new_param = new_param + par
        elif par == "e":
            par = "k"
            new_param = new_param + par
        elif par == "f":
            par = "l"
            new_param = new_param + par

    return new_param
 
 #a b c d e f

 #g h i j k l
 
def x_checker(number, param):
    if len(param) > int(number):
        return hex_change(param)
    else:
        x = int(number) - len(hex_change(param))
        if int(param) >= 0:
            return x*"o"+hex_change(param)
        # else:
        #     num = hex_change(param)
        #     return "-"+x*"0"+num[1:]

def my_printf(format_string,param):
    #print(format_string)
    x_param=""
    pattern = re.compile(r'#\.(\d+)j')
    if not is_digit(param):
        print("Error", end="")
        print("")
    elif int(param) < 0:
        print("Error", end="")
        print("")
    else:
        if ((pattern.search(format_string)) != None):
            result = pattern.search(format_string)
            number = result.group(1)
            whole = result.group(0)
            out = x_checker(number, param)
            new_string = format_string.replace(whole, out)
            print(new_string, end="")
            print("")
        else:
            print(format_string, end="")
            print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())