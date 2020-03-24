import os, inspect, subprocess, random

def fuzz(max_length = 100, start = 64, end = 126):
    out = ""
    string_length = random.randrange(max_length) + 1
    for i in range(string_length):
        out += chr(random.randint(start, end))

    return out