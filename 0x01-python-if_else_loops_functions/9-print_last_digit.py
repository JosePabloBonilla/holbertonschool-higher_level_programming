#!/usr/bin/python3
def print_last_digit(number):
    last_num = number % 10
    neg_num = (number % -10) * -1
    if number >= 0:
        print("{}".format(last_num), end='')
        return(last_num)
    else:
        print("{}".format(neg_num), end='')
        return(neg_num)
