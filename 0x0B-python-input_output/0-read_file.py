#!/usr/bin/python3
def read_file(filename="", mode="r", encoding="utf-8"):
    with open(filename) as f:
        for line in f:
            print(line, end="")
