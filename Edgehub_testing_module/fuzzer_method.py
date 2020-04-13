import os, inspect, subprocess, random, re

def fuzz(max_length = 100, start = 97, end = 122):
    out = ""
    string_length = random.randrange(max_length) + 1
    for i in range(string_length):
        out += chr(random.randint(start, end))

    return out

START_SYMBOL = "<start>"
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')

def nonterminams(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]
    return re.findall(RE_NONTERMINAL, expansion)

assert nonterminams("<term> * <factor>") == ["<term>","<factor>"]
class ExpansionError(Exception):
    pass