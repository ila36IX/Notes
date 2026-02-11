#!/bin/env python3

def generate_line(line):
    pair = line.split(":")
    key, value = pair[0], pair[1]
    newline = f"KEY:  {key.strip()}\nVALUE: {value.strip()}\n"
    return newline
    # print("KEY: ", key.strip())
    # print("VALUE: ", value.strip())


def read_file():
    try:
        with open("./English pool.md", "r", encoding="utf-8") as f:
            data = ""
            for line in f.read().split("---"):
                data += generate_line(line)
            print(data)
            
    except Exception as e:
        print(f"Error: {e}")

read_file();
