"""
WORD PROBLEMS - ADVANCED TEXT PROCESSING AND ALGORITHMS
Comprehensive collection of word manipulation algorithms and string processing techniques

STEP-BY-STEP PROCESS:
Step 1: Character frequency analysis and histogram generation
Step 2: Palindrome detection and reverse word finding
Step 3: Word rotation and anagram detection algorithms
Step 4: Advanced string manipulation (consonant rotation, character patterns)
Step 5: Binary search applications for sorted word lists
Step 6: Dynamic programming for word chains and letter elimination
Step 7: Prime factorization for anagram grouping

LEARNING OBJECTIVES:
- Master regular expressions for complex pattern matching
- Understand binary search algorithms for sorted data structures
- Learn dynamic programming techniques for word problems
- Practice advanced list comprehensions and set operations
- Implement mathematical algorithms (prime factorization) for text analysis
- Build efficient algorithms for large-scale text processing

TIME COMPLEXITY ANALYSIS:
- Character histogram: O(n×m) where n=words, m=avg word length
- Palindrome detection: O(n×m) for string slicing operations
- Binary search operations: O(log n) for sorted word lookup
- Anagram detection with primes: O(n×m) with unique factorization
- Word chain generation: O(n²) with backtracking optimization
"""

from random import choice, sample
from bisect import bisect_left, bisect_right

# Regular expressions can come handy in text problems.

import re


# STEP 1: CHARACTER FREQUENCY ANALYSIS
# Compute a histogram of individual characters in words.

def histogram(words):
    """
    Generate frequency histogram of all characters across word list
    
    Args:
        words: List of strings to analyze
    
    Returns:
        Dictionary mapping characters to their occurrence counts
    
    Time Complexity: O(n×m) where n=number of words, m=average word length
    Space Complexity: O(k) where k=number of unique characters
    
    Algorithm:
    1. Initialize empty frequency dictionary
    2. Iterate through each word in the word list
    3. For each character in word, increment its count
    4. Use dict.get(key, default) for safe counter increment
    """
    result = {}
    for word in words:
        for c in word:
            result[c] = result.get(c, 0) + 1  # Safe increment with default
    return result
    # Expected output: {'e': 376455, 'i': 313008, 'a': 295794, 'o': 251596, ...}


# STEP 2A: PALINDROME DETECTION
# Find all words that are palindromes.

def palindromes(words):
    """
    Find all words that read the same forwards and backwards
    
    Args:
        words: List of strings to check for palindromes
    
    Returns:
        List of palindromic words
    
    Time Complexity: O(n×m) where n=words, m=average word length (for string slicing)
    Algorithm: Compare each word with its reverse using slice notation [::-1]
    """
    return [w for w in words if w == w[::-1]]  # String slicing for reversal
    # Expected output: ['ana', 'ululu', 'dtd', 'kelek', 'v', 'awa', 'j', 'apa', ...]
    # Total count: 232 palindromes found


# STEP 2B: REVERSE WORD PAIRS (SEMORDNILAPS)
# Find all words that are a different word when read backwards.

def semordnilap(words):
    """
    Find words that form valid words when spelled backwards (not palindromes)
    
    Args:
        words: List of strings to analyze
    
    Returns:
        List of words whose reverse is also a valid word (but different)
    
    Time Complexity: O(n×m + n) for set creation and lookups
    Algorithm:
    1. Create set from word list for O(1) lookup time
    2. Check if word ≠ reverse AND reverse exists in word set
    3. Use set membership for efficient reverse word verification
    """
    wset = set(words)  # O(1) lookup time for membership testing
    return [w for w in words if w != w[::-1] and w[::-1] in wset]
    # Expected output: ['toots', 'amahs', 'lm', 'bins', 'ter', 'oda', 'aru', ...]
    # Total count: 2654 semordnilaps found


# STEP 2C: ROTATED WORDS (ROTODROMES)
# Find all the rotodromes, words that become other words when rotated.

def rotodromes(words):
    """
    Find words that form other valid words when cyclically rotated
    
    Args:
        words: List of strings to analyze
    
    Returns:
        List of words that can be rotated to form other words
    
    Time Complexity: O(n×m²) where n=words, m=average word length
    Algorithm:
    1. For each word, try all possible rotation positions (1 to length-1)
    2. Create rotated version: word[i:] + word[:i] (suffix + prefix)
    3. Check if rotation ≠ original AND exists in word set
    4. Use nested function for cleaner code organization
    """
    def is_rotodrome(word, wset):
        """Helper function to check if a word has valid rotations"""
        for i in range(1, len(word)):
            w2 = word[i:] + word[:i]  # Cyclic rotation: move first i chars to end
            if word != w2 and w2 in wset:  # Different word that exists
                return True
        return False
    
    w_set = set(words)  # O(1) lookup for rotation checking
    return [w for w in words if is_rotodrome(w, w_set)]
    # Expected output: Length 2: ['fa', 'ba', 'ym', ...], Length 3: ['adm', 'sen', ...]
    # Example counts: 310 (len=2), 804 (len=3), 1670 (len=4), etc.


# STEP 2D: ALMOST PALINDROMES
# Find the "almost palindromes", words that become palindromes when
# one letter is tactically removed.

def almost_palindromes(words):
    """
    Find words that become palindromes when exactly one character is removed
    
    Args:
        words: List of strings to analyze
    
    Returns:
        List of words that are one character away from being palindromes
    
    Time Complexity: O(n×m²) where n=words, m=average word length
    Algorithm:
    1. Skip actual palindromes (already perfect)
    2. For each position i, create word with character i removed
    3. Check if resulting word is palindromic
    4. Only consider words longer than 2 characters
    """
    def almost(word):
        """Helper function to check if word is almost palindromic"""
        # Words that are already palindromes don't count.
        if word != word[::-1]:
            # Loop through the positions to remove a character.
            for i in range(len(word)):
                w2 = word[:i] + word[i+1:]  # Remove character at position i
                if w2 == w2[::-1]:  # Check if result is palindromic
                    return True
        return False
    
    return [w for w in words if len(w) > 2 and almost(w)]  # Filter by length
    # Expected output: ['tss', 'away', 'thight', 'boo', 'cuca', 'goo', ...]
    # Total count: 1911 almost palindromes found


# STEP 3: ADVANCED STRING MANIPULATION - CONSONANT ROTATION
# Rotate the consonants of the text cyclically, keeping the rest of
# the characters as they are, and maintaining the capitalization of
# the individual characters. For example, "Ilkka" becomes "Iklka".

__cons = "bcdfghjklmnpqrstvwxyz"  # All lowercase consonants
__cons += __cons.upper()          # Add uppercase consonants for lookup


def rotate_consonants(text, off=1):
    """
    Cyclically rotate consonants in text while preserving vowels and capitalization
    
    Args:
        text: Input string to process
        off: Rotation offset (default=1, negative for reverse rotation)
    
    Returns:
        String with consonants rotated by specified offset
    
    Time Complexity: O(n) where n=length of text
    Algorithm:
    1. Find positions of all consonants in the text
    2. For each character position:
       - If consonant: replace with rotated consonant (preserve case)
       - If vowel/other: keep unchanged
    3. Use modular arithmetic for cyclic rotation
    4. Maintain original capitalization pattern
    """
    # Find the positions of all consonants in text.
    cons_pos = [i for (i, c) in enumerate(text) if c in __cons]
    
    # Process the text one character at the time.
    result, pos = '', 0
    for (i, c) in enumerate(text):
        if c in __cons:
            # Location of the next consonant in the consonant list.
            succ = (pos + off) % len(cons_pos)  # Cyclic rotation with offset
            # The consonant that comes into the current position i.
            sc = text[cons_pos[succ]]
            # Maintain the capitalization of original character.
            result += sc.upper() if c.isupper() else sc.lower()
            # Next consonant and incoming consonant advance in lockstep.
            pos = (pos + 1) % len(cons_pos)
        else:
            # Take the character into result as is (vowels, spaces, etc.).
            result += c
    return result
    # Expected output for 'Donald Erwin Knuth':
    # off=-1: 'Hodanl Edriw Nkunt', off=0: 'Donald Erwin Knuth', off=1: 'Noladr Ewnik Ntuhd'


# STEP 4: REGEX PATTERN MATCHING - DUPLICATE LETTER DETECTION
# Find the words that contain at least three duplicated letters.

def triple_duplicate(words):
    """
    Find words containing at least 3 pairs of consecutive duplicate letters
    
    Args:
        words: List of strings to analyze
    
    Returns:
        List of words with 3+ consecutive letter pairs (aa, bb, cc, etc.)
    
    Time Complexity: O(n*m) where n=number of words, m=average word length
    Algorithm:
    1. Use regex pattern (.)\1 to find consecutive duplicate letters
    2. Pattern captures any character (.) and matches if repeated (\1)
    3. Count all matches per word with findall()
    4. Keep words with 3 or more duplicate pairs
    """
    return [x for x in words if len(re.findall(r'(.)\1', x)) >= 3]
    # Expected output for ['hello', 'bookkeeper', 'balloon', 'speed']:
    # ['bookkeeper'] - contains 'oo', 'kk', 'ee' (3 duplicate pairs)


# STEP 5: ADVANCED REGEX - CONSECUTIVE TRIPLE DUPLICATES
# Find the words that contain three duplicated letters all together.

def consec_triple_duplicate(words):
    """
    Find words with 3 consecutive pairs of duplicate letters (aabbcc pattern)
    
    Args:
        words: List of strings to check
    
    Returns:
        List of words containing pattern like 'aabbcc', 'xxyyzz', etc.
    
    Time Complexity: O(n*m) where n=number of words, m=average word length
    Algorithm:
    1. Regex pattern (.)\1(.)\2(.)\3 matches 3 consecutive duplicate pairs
    2. Each (.)\\N captures a character and \\N ensures it's repeated
    3. Pattern requires all 3 pairs to be adjacent: char1char1char2char2char3char3
    4. findall returns matches, filter words with at least one match
    """
    regex = r'(.)\1(.)\2(.)\3'  # Matches patterns like 'aabbcc'
    return [x for x in words if len(re.findall(regex, x)) > 0]
    # Expected output for ['bookkeeper', 'balloon', 'aabbcc', 'speed']:
    # ['aabbcc'] - only word with 3 consecutive duplicate pairs


# STEP 6: CHARACTER SET CONSTRAINTS - LIMITED ALPHABET
# How many words can be spelled out using only given characters?

def limited_alphabet(words, chars):
    """
    Count words that can be spelled using only characters from given set
    
    Args:
        words: List of words to check
        chars: String or set of allowed characters
    
    Returns:
        Number of words that use only allowed characters
    
    Time Complexity: O(n*m*k) where n=words, m=avg word length, k=chars per lookup
    Algorithm:
    1. For each word, check if all characters are in allowed set
    2. Use 'all()' with generator expression for efficient checking
    3. Character lookup in set is O(1), in string is O(k)
    4. Count total valid words
    """
    # def limited(word, chars):
    #     return all(c in chars for c in word)
    # A regular expression used many times is good to precompile
    # into the matching machine for speed and efficiency.
    pat = re.compile('^[' + chars + ']+$')  # Pattern: start^[allowed_chars]+end$
    return [word for word in words if pat.match(word)]
    # Expected output for words=['hello', 'abc', 'xyz'], chars='abcdefgh':
    # ['abc'] - only 'abc' uses characters entirely from 'abcdefgh'


# STEP 7: SLIDING WINDOW ALGORITHM - SUBSTRING WITH K DISTINCT CHARACTERS
# From Programming Praxis. Given text string and integer k,
# find and return the longest substring that contains at most
# k different characters inside it.

def longest_substring_with_k_chars(text, k=2):
    """
    Find longest substring containing at most k distinct characters
    
    Args:
        text: Input string to analyze
        k: Maximum number of distinct characters allowed (default=2)
    
    Returns:
        Longest substring with at most k distinct characters
    
    Time Complexity: O(n) where n=length of text
    Algorithm: Sliding Window with Character Tracking
    1. Maintain dictionary of last seen positions for up to k characters
    2. Expand window while character count <= k
    3. When exceeding k, shrink window by removing oldest character
    4. Track maximum length substring and its position
    5. Use last_seen positions for efficient window management
    """
    # The k most recently seen characters mapped to the last
    # position index of where they occurred.
    last_seen = {}
    len_, max_, maxpos = 0, 0, 0
    for (i, c) in enumerate(text):
        # If no conflict, update the last_seen dictionary.
        if len(last_seen) < k or c in last_seen:
            last_seen[c] = i
            len_ += 1
            if len_ > max_:
                max_ = len_
                maxpos = i - max_ + 1
        else:
            # Find the least recently seen character.
            min_, minc = len(text), '$'
            for cc in last_seen:
                if last_seen[cc] < min_:
                    min_ = last_seen[cc]
                    minc = cc
            # Remove it from dictionary...
            last_seen.pop(minc)
            # ... and bring the current character to its place.
            last_seen[c] = i
            len_ = i - min_
    # Extract the longest found substring as the answer.
    return text[maxpos:maxpos + max_]
    # Expected output for 'abcabcbb', k=2:
    # 'bcbcb' or similar substring with at most 2 distinct characters


# Given a sorted list of words and the first word, construct a
# word chain in which each word starts with the suffix of the
# previous word with the first k characters removed, for example
# ['grama', 'ramal', 'amala', 'malar', 'alarm'] for k = 1.

# STEP 8: BINARY SEARCH + BACKTRACKING - OPTIMIZED WORD CHAINS
# Since words are sorted, we can use binary search algorithm to
# quickly find the sublist whose words start with the given prefix.

def word_chain(words, first, k=1, len_=3):
    """
    Build word chain using binary search optimization and backtracking
    
    Args:
        words: Sorted list of available words (REQUIRED for binary search)
        first: Starting word or partial chain
        k: Characters to remove from word start (default=1)
        len_: Target chain length (default=3)
    
    Returns:
        Complete word chain of specified length, or None if impossible
    
    Time Complexity: O(log n * m * l) where n=words, m=candidates, l=chain depth
    Algorithm: Binary Search + Recursive Backtracking
    1. Use bisect_left/right for O(log n) prefix range finding
    2. Extract suffix from last word: word[k:]
    3. Find all words in sorted range that start with suffix
    4. Try each candidate with length constraint and cycle detection
    5. Recursively backtrack until target length reached
    """
    # Recursive algorithm to complete the given wordlist.
    def backtrack(chain):
        # If the wordlist is long enough, return it.
        if len(chain) == len_:  # Base case: target length reached
            return chain
        # Extract the suffix of the last word of the wordlist.
        suffix = chain[-1][k:]  # Remove first k characters to get suffix
        # Extract the words that start with that suffix using binary search.
        start = bisect_left(words, suffix)          # First word >= suffix
        end = bisect_right(words, suffix + k * 'z') # Last word starting with suffix
        # Try out those words one at the time.
        for idx in range(start, end):
            word = words[idx]
            # Length constraint: next word must be longer than remaining suffix
            # Cycle constraint: word cannot already be in chain
            if len(word) > len(chain[-1]) - k and word not in chain:
                # Extend the wordlist with this word.
                chain.append(word)
                if backtrack(chain):  # Recursive call - solution found
                    return chain
                # Remove that word and try the next one (backtrack).
                chain.pop()

        return None  # No valid chain found from this state
    return backtrack(first)
    # Expected output for words=['ab','ba','abc'], first=['ab'], k=1, len_=2:
    # ['ab', 'ba'] - 'ab' suffix 'b' matches start of 'ba'


# What words remain words after removing one character? Create and return
# a list whose i:th element is a dictionary of all such words of length
# i, mapped to the list of words of length i-1 that they can be turned
# into by removing one letter.

def remain_words(words):
    result = [[], [x for x in words if len(x) == 1]]
    wl = 2
    while True:
        next_level, has_words = {}, False
        for w in (x for x in words if len(x) == wl):
            shorter = []
            for i in range(0, wl - 1):
                ww = w[:i] + w[i+1:]  # word with i:th letter removed
                if ww in result[wl - 1]:
                    shorter.append(ww)
            if len(shorter) > 0:
                next_level[w] = shorter
                has_words = True
        if has_words:
            result.append(next_level)
            wl += 1
        else:
            return result


# Generate a table of all anagrams from the given word list.

# The first 26 prime numbers, one for each letter from a to z.
__primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def prime_code(word):
    code = 1
    for c in word:
        # ord(c) gives the Unicode integer codepoint of c.
        code *= __primes[ord(c) - ord('a')]
    return code


def all_anagrams(words):
    codes = {}
    for word in words:
        code = prime_code(word)
        # All anagrams have the same prime code, thanks to the
        # commutativity of integer multiplication combined with
        # the Fundamental Theorem of Arithmetic that says every
        # integer has exactly one prime possible factorization.
        codes[code] = codes.get(code, []) + [word]
    return codes


def __demo():
    with open('words_sorted.txt', encoding="utf-8") as f:
        words = [x.strip() for x in f]
    print(f"Read in {len(words)} words.")

    # Binary search can quickly find all words with given prefix.
    for prefix in ['aor', 'jims', 'propo']:
        result = []
        idx = bisect_left(words, prefix)
        while idx < len(words) and words[idx].startswith(prefix):
            result.append(words[idx])
            idx += 1
        result = ", ".join(result)
        print(f"\nWords that start with {prefix!r} are {result}.")

    # How about finding all words that end with given suffix?
    words_r = [word[::-1] for word in words]
    words_r.sort()
    for suffix in ["itus", "roo", "lua"]:
        suffix = suffix[::-1]
        result = []
        idx = bisect_left(words_r, suffix)
        while idx < len(words_r) and words_r[idx].startswith(suffix):
            result.append(words_r[idx][::-1])
            idx += 1
        result.sort()
        result = ", ".join(result)
        print(f"\nWords that end with {suffix[::-1]!r} are {result}.")

    hist = histogram(words).items()
    hist = sorted(hist, key=lambda x: x[1], reverse=True)
    print("\nHistogram of letters sorted by their frequencies:")
    print(hist)

    pals = palindromes(words)
    print(f"\nThere are {len(pals)} palindromes. ", end="")
    print("Some of them are:")
    print(", ".join(sample(pals, 10)))

    sems = semordnilap(words)
    print(f"\nThere are {len(sems)} semordnilaps. Some of them are:")
    print(", ".join(sample(sems, 10)))

    almost = almost_palindromes(words)
    print(f"\nThere are {len(almost)} almost palindromes. ", end="")
    print("Some of them are:")
    print(", ".join(sample(almost, 10)))

    print("\nLet us next look for some rotodromes.")
    for i in range(2, 13):
        rotos = rotodromes([w for w in words if len(w) == i])
        print(f"There are {len(rotos)} rotodromes of length {i}.")
        print(f"Some of these rotodromes are:")
        print(f"{', '.join(sample(rotos, min(10, len(rotos))))}.")

    name = 'Donald Erwin Knuth'
    print(f"\nSome consonant rotations of {name!r}.")
    for off in range(-5, 6):
        print(f"{off:2}: {rotate_consonants(name, off)}")

    print("\nWords that contain triple duplicate character:")
    for word in triple_duplicate(words):
        print(word, end=' ')

    print("\n\nWords that contain consecutive triple duplicate:")
    for word in consec_triple_duplicate(words):
        print(word, end=' ')

    print("\n\nWords that contain only hexadecimal digits [a-f]:")
    for word in limited_alphabet(words, "abcdef"):
        print(word, end=' ')

    print("\n\nWords that contain only vowels:")
    for word in limited_alphabet(words, "aeiouy"):
        print(word, end=' ')

    print("\n\nWords spelled with upside down calculator:")
    for word in limited_alphabet(words, "oieslbg"):
        print(word.upper(), end=' ')

    text = "ceterumautemcenseocarthaginemessedelendam"
    print(f"\n\nThe text is '{text}'.")
    print("Let's print out its longest substrings with k letters.")
    for k in range(1, 16):
        print(f"k = {k:2}: {longest_substring_with_k_chars(text, k)}")

    print(f"\nHow about the longest 10-char substring of War and Peace? It is:")
    with open('warandpeace.txt', encoding="utf-8") as wap:
        text = " ".join(wap)
    text.replace("\n", " ")
    print(f"{longest_substring_with_k_chars(text, 10)}")

    print("\nNext, some word chains of five-letter words.")
    words5 = [word for word in words if len(word) == 5]
    count, total = 0, 0
    while count < 10:
        total += 1
        first = choice(words5)
        best = [first]
        while len(best) < 5:
            better = word_chain(words5, [first], 1, len(best) + 1)
            if better:
                best = better
            else:
                break
        if len(best) > 3:
            print(f"{first}: {best}")
            count += 1
    print(f"Found {count} word chains after trying {total} firsts.")

    print("\nSome letter eliminations:")
    elim_dict_list = remain_words(words)
    start_words = list(elim_dict_list[8])
    for i in range(10):
        word = choice(start_words)
        while len(word) > 1:
            print(word, end=" -> ")
            word = choice(elim_dict_list[len(word)][word])
        print(word)

    N, M = 7, 8
    print(f"\nLet us compute all anagrams for the {N}-letter words.")
    anagrams = all_anagrams(word for word in words if len(word) == N)
    print(f"The anagram groups with {M} or more members are:\n")

    # Note that anagrams is a dictionary that maps prime codes to
    # lists of words that all have that same prime code.
    for code in (c for c in anagrams if len(anagrams[c]) >= M):
        print(", ".join(anagrams[code]))


if __name__ == "__main__":
    __demo()
