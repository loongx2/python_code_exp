def insert_repeat_counts(s):
    """
    Insert numerical counts after repeating characters in a string (consecutive approach).
    Example: "aaabbc" -> "a3b2c"
    """
    if not s:
        return s
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            # Add character and count (if > 1)
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            
            # Reset for new character
            current_char = s[i]
            count = 1
    
    # Handle the last group
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    return ''.join(result)


def insert_repeat_counts_dict(s):
    """
    Insert numerical counts using dictionary approach - shows unique characters with total frequency (only if > 1).
    Example: "aaabbc" -> "a3b2c" (each character appears once with its total count, singles excluded)
    """
    if not s:
        return s
    
    # Count frequency of each character while preserving first occurrence order
    char_count = {}
    order = []
    for char in s:
        if char not in char_count:
            order.append(char)
            char_count[char] = 0
        char_count[char] += 1
    
    # Build result string - each unique character with its total count (only if > 1)
    result = []
    for char in order:
        result.append(char)
        if char_count[char] > 1:
            result.append(str(char_count[char]))
    
    return ''.join(result)

# Test cases
test_strings = [
    "aaabbc",
    "hello",
    "aabbccdd",
    "programming",
    "aaa",
    "abcd",
    # Examples with multiple occurrences of same repeating characters
    "aabbaaabbbcdefffgaa",
    "xxyyxxzzzyyxx",
    "aaabbbaaacccaaa",
    "mississippi",
    "bookkeeper",
    "aabbccaabbcc"
]

print("Comparing Consecutive vs Dictionary Approaches")
# Expected output: Comparing Consecutive vs Dictionary Approaches
print("=" * 50)
# Expected output: ==================================================
print("Original -> Consecutive -> Dictionary")
# Expected output: Original -> Consecutive -> Dictionary
print("-" * 50)
# Expected output: --------------------------------------------------
for test in test_strings:
    consecutive = insert_repeat_counts(test)
    dictionary = insert_repeat_counts_dict(test)
    print(f"{test} -> {consecutive} -> {dictionary}")
# Expected output for all test cases:
# aaabbc -> a3b2c -> a3b2c
# hello -> hel2o -> hel2o
# aabbccdd -> a2b2c2d2 -> a2b2c2d2
# programming -> program2ing -> pr2og2am2in
# aaa -> a3 -> a3
# abcd -> abcd -> abcd
# aabbaaabbbcdefffgaa -> a2b2a3b3cdef3ga2 -> a7b5cdef3g
# xxyyxxzzzyyxx -> x2y2x2z3y2x2 -> x6y4z3
# aaabbbaaacccaaa -> a3b3a3c3a3 -> a9b3c3
# mississippi -> mis2is2ip2i -> mi4s4p2
# bookkeeper -> bo2k2e2per -> bo2k2e3pr
# aabbccaabbcc -> a2b2c2a2b2c2 -> a4b4c4

# Interactive mode
print("\nInteractive Mode:")
# Expected output: 
# Interactive Mode:
print("Enter a string to compress (or 'quit' to exit)")
# Expected output: Enter a string to compress (or 'quit' to exit)
print("Both consecutive and dictionary approaches will be applied")
# Expected output: Both consecutive and dictionary approaches will be applied

while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break
    
    # Run both approaches on the input
    consecutive_result = insert_repeat_counts(user_input)
    dictionary_result = insert_repeat_counts_dict(user_input)
    
    print(f"Input: {user_input}")
    print(f"Consecutive: {consecutive_result}")
    print(f"Dictionary:  {dictionary_result}")
    print("-" * 30)