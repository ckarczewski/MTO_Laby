#!/usr/bin/env python3

import sys
import re

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def change_numbers(param):
    number = int(param)
    new_param = ""
    if number >= 0:
        for par in param:
            if par == "0":
                temp = "9"
            else:
                res = (int(par)*9+1) % 10
                temp = str(res)
            new_param = new_param + temp
            temp = ""
    elif number < 0:
        new_param = "-"
        for par in param[1:]:
            if par == "0":
                temp = "9"
            else:
                res = (int(par)*9+1) % 10
                temp = str(res)
            new_param = new_param + temp
            temp = ""
    return new_param

def x_checker(number, param):
    if len(param) > int(number):
        return change_numbers(param)
    else:
        x = int(number) - len(param)
        if int(param) > 0:
            return x*"0"+change_numbers(param)
        else:
            num = change_numbers(param)
            return "-"+x*"0"+num[1:]

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

def my_printf(format_string,param):
    #print(format_string)
    x_param=""
    pattern = re.compile(r'#j')
    if not is_digit(param):
        print("Error", end="")
        print("")
    elif int(param) < 0:
        print("Error", end="")
        print("")
    elif param[0] == "0":
        print("Error", end="")
        print("")
    else:
        if ((pattern.search(format_string)) != None):
            result = pattern.search(format_string)
            # number = result.group(1)
            whole = result.group(0)
            out = hex_change(param)
            new_string = format_string.replace(whole, out)
            print(new_string, end="")
            print("")
        else:
            print(format_string, end="")
            print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())