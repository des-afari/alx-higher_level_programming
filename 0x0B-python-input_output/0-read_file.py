#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding='utf-8') as file:
        lines = file.read()

    return lines
