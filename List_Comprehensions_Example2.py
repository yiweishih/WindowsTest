#!/usr/bin/python3

"""
Write a function called lognlengths that returns the lengths of those strings that have at least 4 characters.
Try it with a list comprehension
"""

def longlengths1(strings):
    return [len(s) for s in strings if len(s)>=4]

def longlengths2(strings):
    mylist = []
    for i in strings:
        if len(i) >=4:
            mylist.append(len(i))
    return mylist

def longlengths3(strings):
    filtered_strings = filter(lambda s: len(s)>=4, strings)
    return map(lambda s: len(s), filtered_strings)





print(longlengths3(["qwe","qwrqrqwr","q","Yiwei Shih", "abc", "ccd"]))