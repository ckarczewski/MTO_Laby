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

def x_checker(inside, param):
    if not is_digit(inside): # when inside is not number
        return ""
    elif is_digit(inside) and inside.isdigit(): #when inside is (5; 05;)
        x = int(inside)
        if inside[0] == "0":
            return x*"0"+decrease_numbers(param)
        else:
            return x*" "+decrease_numbers(param)
    elif is_digit(inside) and not inside.isdigit(): #when inside is(-5; -05;)
        x = int(inside)*(-1)
        if inside[1] == "0":
            return decrease_numbers(param)+x*"0"
        else: 
            return decrease_numbers(param)+x*" " 

            # sprawdzić czy pierwsze jest zerem jeśli tak to niech sprawdzi czy resta jest liczba  


def my_printf(format_string,param):
    #print(format_string)
    if not is_digit(param):
        print("Error", end="")
        print("")
    else:
        shouldDo=True
        changed_param = ""
        result = ""
        for idx in range(0,len(format_string)):
            if shouldDo:
                if format_string[idx] == '#':
                    for jdx in range(idx,len(format_string)):
                        if format_string[jdx] == 'g':
                            result = re.search('#(.*)g', format_string)
                            t = result.group(1)
                            output = x_checker(t, param)
                            if output == "":
                                break
                            else:
                                print(output)      
                else:
                    print(format_string[idx],end="")
            else:
                shouldDo=True
        print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())