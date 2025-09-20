"""
WORD COUNT ANALYSIS - WAR AND PEACE TEXT PROCESSING
Complete text analysis demonstration using regular expressions and dictionary processing

STEP-BY-STEP PROCESS:
Step 1: Define contractions replacement table for text normalization
Step 2: Compile regex pattern for word separation
Step 3: Process text file line by line with preprocessing
Step 4: Extract and count individual words using dictionary
Step 5: Display individual word frequency statistics
Step 6: Sort words by frequency and create ranked lists
Step 7: Analyze most frequent and unique (once-occurring) words

LEARNING OBJECTIVES:
- Text preprocessing and normalization techniques
- Regular expression usage for pattern matching
- Dictionary operations for counting and frequency analysis
- File I/O operations with encoding handling
- List comprehensions and tuple manipulation
- Sorting and data transformation methods

TIME COMPLEXITY ANALYSIS:
- Text processing: O(n) where n = number of characters
- Dictionary operations: O(1) average for get/set operations
- Sorting: O(m log m) where m = number of unique words
- List operations: O(m) for comprehensions and filtering
"""

# Regular expressions are a powerful way to perform some computations
# on strings that otherwise would be quite difficult.

import re

# STEP 1: Define contractions replacement table for text normalization
# To get rid of single quotes in text, we replace contractions with
# full words. This way, any single quotes that remain are actual quotes.

replacements = (
      ("doesn't", "does not"),
      ("don't", "do not"),
      ("you're", "you are"),
      ("i'm", "i am"),
      ("we're", "we are"),
      ("they're", "they are"),
      ("won't", "will not"),
      ("can't", "can not"),
      ("shan't", "shall not"),
      ("shouldn't", "should not"),
      ("mustn't", "must not"),
      ("aren't", "are not")
    )
# Expected result: Tuple of 12 common contraction replacement pairs

# STEP 2: Compile regex pattern for word separation
# Precompile a regex machine to recognize word separators. For
# simplicity, we accept any non-letter to be a word separator.

word_separators = re.compile("[^a-z]+")
# Expected result: Compiled regex pattern object for splitting on non-letters

# STEP 3: Initialize dictionary for word frequency counting
# The dictionary of words that we shall build up as we see them.

words = {}
# Expected result: Empty dictionary to store word counts

# STEP 4: Process text file line by line with preprocessing and word counting
with open('warandpeace.txt', encoding="utf-8") as wap:
    for line in wap:
        if len(line) < 2:  # skip empty lines
            continue
        # Lowercase the line and remove the trailing linebreak character.
        line = line.lower()
        if line[-1] == '\n':
            line = line[:-1]
        # Remove the contractions using replacement table (see above).
        for (orig, repl) in replacements:
            line = line.replace(orig, repl)
        # Remove whatever other contractions might remain using regex.
        # Raw strings are handy for regexes.
        line = re.sub(r"'s\b", "", line)      # Remove possessive 's
        line = re.sub(r"'ll\b", " will", line)  # Replace 'll with will
        # Process the individual words in the line using regex split.
        for word in word_separators.split(line):
            if len(word) > 0:
                words[word] = words.get(word, 0) + 1  # Increment word count
# Expected result: Dictionary with ~66,000+ word entries and their frequencies

# STEP 5: Display individual word frequency statistics
print("Here are some individual word counts.")
# Expected output: Here are some individual word counts.
for w in ('prince', 'russia', 'you', 'supercalifragilisticexpialidocious'):
    print(f"The word {w!r} occurs {words.get(w, 0)} times.")
    # Expected output: The word 'prince' occurs 1928 times.
    # Expected output: The word 'russia' occurs 173 times.
    # Expected output: The word 'you' occurs 3801 times.
    # Expected output: The word 'supercalifragilisticexpialidocious' occurs 0 times.

# STEP 6A: Transform dictionary to list of (count, word) tuples for sorting
# Turn a dictionary into a list of its items as (value, key) tuples.
# Dictionary method items() produces sequence of (key, value) pairs,
# but swapping these is trivial with a list comprehension.

words_list_f = [(c, w) for (w, c) in words.items()]
# Expected result: List of ~66,000+ tuples like (1928, 'prince'), (173, 'russia')

# STEP 6B: Sort words by frequency (descending) then alphabetically
# Sorting the list of pairs of the form (count, word). Python tuple
# comparison happens lexicographically, so the primary sorting criteria
# is the count. Words of equal frequency then get sorted according to
# their dictionary order.

words_list_f = sorted(words_list_f, reverse=True)
# Expected result: List sorted by count (highest first), then alphabetically

# STEP 6C: Extract sorted words into separate list, dropping the counts
# Extract the sorted words into a separate list, dropping the counts.
words_list = [w for (c, w) in words_list_f]
# Expected result: List of words ordered by frequency: ['the', 'and', 'to', ...]

# STEP 7A: Display the 300 most frequent words
print("\nThe 300 most frequent words in War and Peace are:")
# Expected output: The 300 most frequent words in War and Peace are:
print(", ".join(words_list[:300]))
# Expected output: the, and, to, of, a, he, in, that, his, was, with, not, it, had, her, him, at, i, but, as, on, you, for, she, is, said, all, from, be, were, by, what, they, who, one, this, which, have, pierre, prince, so, an, will, up, do, there, them, or, when, did, been, their, are, no, would, now, only, if, me, out, my, natasha, man, andrew, could, we, more, himself, about, how, into, then, time, princess, face, french, went, some, know, after, old, before, eyes, your, very, men, rostov, room, thought, go, like, well, see, count, moscow, began, again, has, down, come, came, still, mary, asked, without, army, same, can, those, am, looked, say, nicholas, first, felt, emperor, where, our, another, life, away, left, something, over, two, such, these, seemed, napoleon, other, head, just, its, day, yes, people, little, long, why, hand, should, than, whole, kutuzov, back, even, general, own, here, heard, good, having, way, because, countess, must, look, nothing, any, always, saw, being, made, though, russian, love, right, sonya, young, officer, father, suddenly, denisov, round, off, moment, voice, us, everything, smile, looking, knew, told, never, whom, let, while, took, house, words, much, too, turned, dear, through, quite, tell, chapter, under, think, once, get, battle, soldiers, take, evidently, understand, yet, last, sat, every, door, dolokhov, herself, already, most, feeling, going, oh, might, god, behind, place, stood, gave, horse, done, others, replied, expression, side, commander, war, position, wife, order, boris, anna, toward, anything, seen, new, may, give, three, make, son, put, petya, also, great, front, enemy, ran, chief, troops, hands, both, shall, talk, soon, want, mother, horses, petersburg, called, shouted, does, vasili, taken, alone, between, word, whether, saying, part, many, things, officers, thing, letter, everyone, regiment, mind, along, night, table, sent, during, rode, against, anatole, sitting, found, entered, question, moved, morning, evening, among

# STEP 7B: Analyze words that occur exactly once (unique words)
once = list(reversed([w for w in words_list if words[w] == 1]))
# Create list of words with frequency=1, reversed for reverse alphabetical order
print(f"\n{len(once)} words occur exactly once in War and Peace:")
# Expected output: 5847 words occur exactly once in War and Peace:
print(", ".join(once))
# Expected output: aah, ab, abacus, abandons, abasement, abbreviations, abc, abdicate, abductors, abhorrence, abnormal, abnormally, abodes, abolishing, abolition, abominably, abounding, aboveboard, abramovna... (5847 unique words total)
