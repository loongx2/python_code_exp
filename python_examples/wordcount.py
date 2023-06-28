# Regular expressions are a powerful way to perform some computations
# on strings that otherwise would be quite difficult.

import re

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

# Precompile a regex machine to recognize word separators. For
# simplicity, we accept any non-letter to be a word separator.

word_separators = re.compile("[^a-z]+")

# The dictionary of words that we shall build up as we see them.

words = {}

with open('warandpeace.txt', encoding="utf-8") as wap:
    for line in wap:
        if len(line) < 2:  # skip empty lines
            continue
        # Lowercase the line and remove the trailing linebreak character.
        line = line.lower()
        if line[-1] == '\n':
            line = line[:-1]
        # Remove the contractions (see above).
        for (orig, repl) in replacements:
            line = line.replace(orig, repl)
        # Remove whatever other contractions might remain.
        # Raw strings are handy for regexes.
        line = re.sub(r"'s\b", "", line)
        line = re.sub(r"'ll\b", " will", line)
        # Process the individual words in the line.
        for word in word_separators.split(line):
            if len(word) > 0:
                words[word] = words.get(word, 0) + 1

print("Here are some individual word counts.")
for w in ('prince', 'russia', 'you', 'supercalifragilisticexpialidocious'):
    print(f"The word {w!r} occurs {words.get(w, 0)} times.")

# Turn a dictionary into a list of its items as (value, key) tuples.
# Dictionary method items() produces sequence of (key, value) pairs,
# but swapping these is trivial with a list comprehension.

words_list_f = [(c, w) for (w, c) in words.items()]

# Sorting the list of pairs of the form (count, word). Python tuple
# comparison happens lexicographically, so the primary sorting criteria
# is the count. Words of equal frequency then get sorted according to
# their dictionary order.

words_list_f = sorted(words_list_f, reverse=True)

# Extract the sorted words into a separate list, dropping the counts.
words_list = [w for (c, w) in words_list_f]

print("\nThe 300 most frequent words in War and Peace are:")
print(", ".join(words_list[:300]))

once = list(reversed([w for w in words_list if words[w] == 1]))
print(f"\n{len(once)} words occur exactly once in War and Peace:")
print(", ".join(once))
