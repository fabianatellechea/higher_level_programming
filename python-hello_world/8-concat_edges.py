#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str = str[39:-62] + ' ' + str[106:-18] + ' ' + str[:-122]
print(str)
