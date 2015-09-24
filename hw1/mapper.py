import sys, re

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = re.sub('[\W_]+|[0-9]+', '', word).lower()
        if(len(word) > 0):
            print("%s\t%s" % (word, 1))