#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
