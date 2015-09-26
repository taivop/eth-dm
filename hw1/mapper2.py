import sys, re

A = 10
B = 35

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)
    count = int(count)

    if(A <= count and count <= B):
        l = word[0]
        print("%s\t%s\t%s" % (l, word, count))