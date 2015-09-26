import sys

letter = None
previous_letter = None
tuples = []

for line in sys.stdin:
    line = line.strip()
    letter, word, count = line.split("\t", 2)

    # If we just started
    if(previous_letter is None):
        previous_letter = letter

    # If current letter is not the same as previous letter
    if(previous_letter != letter):
        # Sort tuples and take max 20 elements
        tuples.sort(key=lambda t: t[2], reverse=True)
        tuples = tuples[1:min(20, len(tuples))]

        # Print out result
        for t in tuples:
            print("%s\t%s" % (t[1], t[2]))

        # Reset tuples array
        tuples = []
        # Set new previous letter
        previous_letter = letter

    else:
        tuples.append((letter, word, int(count)))