"""Gabriela Marie S. Mendez
   DATALGO Lab 01
   Feb. 11, 2020
   I have neither received nor provided any help
   on this (lab) activity, nor have I concealed
   any violation of the Honor Code.
"""
def sequence(x):
    return sorted(x) == list(range(min(x), max(x) + 1))
firstseq = [3, 4, 6, 5, 1, 2]
secondseq = [3, 1, 4, 2, 1, 3]
print(firstseq , sequence(firstseq))
print(secondseq , sequence(secondseq))