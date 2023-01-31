#!/usr/bin/python3
def magic_string(n=[]):
    # function objects can have attributes, here at global count of calls
    n += ['BestSchool']
    return (", ".join(n) + '$')
