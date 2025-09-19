def find_unique_characters_set(text):
    """
    Find unique characters in a string using set approach.
    
    Args:
        text (str): Input string
    
    Returns:
        list: List of unique characters in order of first appearance
    """
    seen = set()
    unique_chars = []
    
    for char in text:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)
    
    return unique_chars


def find_unique_characters_dict(text):
    """
    Find unique characters using dictionary to count frequencies.
    
    Args:
        text (str): Input string
    
    Returns:
        dict: Dictionary with character frequencies
    """
    char_count = {}
    
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count


def find_characters_appearing_once(text):
    """
    Find characters that appear exactly once in the string.
    
    Args:
        text (str): Input string
    
    Returns:
        list: List of characters that appear only once
    """
    char_count = {}
    
    # Count character frequencies
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find characters with count = 1
    unique_once = [char for char, count in char_count.items() if count == 1]
    
    return unique_once


def find_unique_characters_order_preserved(text):
    """
    Find unique characters preserving the order of first appearance.
    
    Args:
        text (str): Input string
    
    Returns:
        str: String with unique characters in order of appearance
    """
    result = ""
    seen = set()
    
    for char in text:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result


def find_first_non_repeating_character(text):
    """
    Find the first character that doesn't repeat in the string.
    
    Args:
        text (str): Input string
    
    Returns:
        str or None: First non-repeating character or None if all repeat
    """
    char_count = {}
    
    # Count frequencies
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count = 1
    for char in text:
        if char_count[char] == 1:
            return char
    
    return None


# Test cases and demonstrations
def main():
    print("Unique Character Finding Demo")
    print("=" * 40)
    
    # Test strings
    test_strings = [
        "hello world",
        "programming",
        "abcdef",
        "aabbcc",
        "mississippi", 
        "racecar",
        "abcabcabc",
        "unique"
    ]
    
    for test_str in test_strings:
        print(f"\nTest string: '{test_str}'")
        print("-" * 30)
        
        # 1. All unique characters (order preserved)
        unique_ordered = find_unique_characters_set(test_str)
        print(f"Unique chars (ordered): {unique_ordered}")
        # Expected output: List of unique characters in order of first appearance
        
        # 2. Character frequencies
        frequencies = find_unique_characters_dict(test_str)
        print(f"Character frequencies: {frequencies}")
        # Expected output: Dictionary showing count of each character
        
        # 3. Characters appearing exactly once
        once_only = find_characters_appearing_once(test_str)
        print(f"Chars appearing once: {once_only}")
        # Expected output: List of characters that appear only once
        
        # 4. Unique string (duplicates removed)
        unique_string = find_unique_characters_order_preserved(test_str)
        print(f"Unique string: '{unique_string}'")
        # Expected output: String with duplicates removed, order preserved
        
        # 5. First non-repeating character
        first_non_repeat = find_first_non_repeating_character(test_str)
        print(f"First non-repeating: {first_non_repeat}")
        # Expected output: First character that doesn't repeat, or None
    
    # Special test cases
    print("\n" + "=" * 40)
    print("Special Test Cases")
    print("=" * 40)
    
    # Empty string
    empty_test = ""
    print(f"\nEmpty string test: '{empty_test}'")
    print(f"Unique chars: {find_unique_characters_set(empty_test)}")
    # Expected output: []
    print(f"First non-repeating: {find_first_non_repeating_character(empty_test)}")
    # Expected output: None
    
    # Single character
    single_test = "a"
    print(f"\nSingle character test: '{single_test}'")
    print(f"Unique chars: {find_unique_characters_set(single_test)}")
    # Expected output: ['a']
    print(f"First non-repeating: {find_first_non_repeating_character(single_test)}")
    # Expected output: a
    
    # All same characters
    same_test = "aaaaa"
    print(f"\nAll same characters test: '{same_test}'")
    print(f"Unique chars: {find_unique_characters_set(same_test)}")
    # Expected output: ['a']
    print(f"Chars appearing once: {find_characters_appearing_once(same_test)}")
    # Expected output: []
    print(f"First non-repeating: {find_first_non_repeating_character(same_test)}")
    # Expected output: None
    
    # Case sensitivity test
    case_test = "AaAa"
    print(f"\nCase sensitivity test: '{case_test}'")
    print(f"Unique chars: {find_unique_characters_set(case_test)}")
    # Expected output: ['A', 'a']
    print(f"Character frequencies: {find_unique_characters_dict(case_test)}")
    # Expected output: {'A': 2, 'a': 2}
    
    # Unicode characters test
    unicode_test = "café naïve"
    print(f"\nUnicode test: '{unicode_test}'")
    print(f"Unique chars: {find_unique_characters_set(unicode_test)}")
    # Expected output: ['c', 'a', 'f', 'é', ' ', 'n', 'ï', 'v', 'e']
    print(f"Chars appearing once: {find_characters_appearing_once(unicode_test)}")
    # Expected output: ['c', 'f', 'é', ' ', 'n', 'ï', 'v']
    
    print("\n" + "=" * 40)
    print("Demo completed!")
    # Expected output: Demo completed!


if __name__ == "__main__":
    main()