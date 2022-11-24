#!/usr/bin/env python3

import sys
import re

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

def x_checker(number, whole, param):
    try:
        whole.index("-")
        sign = True
    except:
        sign = False

    if sign == True:
        x = int(number)
        if number[0] == "0":
            return decrease_numbers(param)+x*"0"
        else: 
            return decrease_numbers(param)+x*" "
    else:
        x = int(number)
        if number[0] == "0":
            return x*"0"+decrease_numbers(param)
        else:
            return x*" "+decrease_numbers(param)
            # sprawdzić czy pierwsze jest zerem jeśli tak to niech sprawdzi czy resta jest liczba  


def my_printf(format_string,param):
    #print(format_string)
    x_param=""
    pattern = re.compile(r'#-?(\d+)g')
    if not is_digit(param):
        print("Error", end="")
        print("")
    else:
        if ((pattern.search(format_string)) != None):
            result = pattern.search(format_string)
            number = result.group(1)
            whole = result.group(0)
            out = x_checker(number, whole, param)
            new_string = format_string.replace(whole, out)
            print(new_string, end="")
            print("")
        else:
            print(format_string, end="")
            print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())