from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN (output of mapper) 
for line in sys.stdin:
    line = line.strip()

    # parse the input from mapper.py
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, current_count)

