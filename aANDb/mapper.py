import sys

# input comes from standard input
for line in sys.stdin:
    # remove whitespace and split
    line = line.strip()
    words = line.split()
    #counter process
    for word in words:
         print '%s\t%s' % (word, 1)

