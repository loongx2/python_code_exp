#!/usr/bin/env python3
"""
Python Dictionary Built-in Functions Test Application
Demonstrates all dictionary type built-in functions with expected outputs
"""

def test_dictionary_functions():
    print("=== Dictionary Built-in Functions Test ===\n")
    
    # Initial dictionary setup
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Original dictionary: {sample_dict}")
    
    # 1. len() - Returns number of key-value pairs
    length = len(sample_dict)
    print(f"len(sample_dict): {length}")  # Expected: 3
    
    # 2. dict() - Creates a new dictionary
    new_dict = dict([('x', 10), ('y', 20)])
    print(f"dict([('x', 10), ('y', 20)]): {new_dict}")  # Expected: {'x': 10, 'y': 20}
    
    # 3. keys() - Returns dictionary keys
    keys = list(sample_dict.keys())
    print(f"sample_dict.keys(): {keys}")  # Expected: ['a', 'b', 'c']
    
    # 4. values() - Returns dictionary values
    values = list(sample_dict.values())
    print(f"sample_dict.values(): {values}")  # Expected: [1, 2, 3]
    
    # 5. items() - Returns key-value pairs as tuples
    items = list(sample_dict.items())
    print(f"sample_dict.items(): {items}")  # Expected: [('a', 1), ('b', 2), ('c', 3)]
    
    # 6. get() - Returns value for key, None if not found
    value = sample_dict.get('a')
    missing = sample_dict.get('z', 'default')
    print(f"sample_dict.get('a'): {value}")  # Expected: 1
    print(f"sample_dict.get('z', 'default'): {missing}")  # Expected: default
    
    # 7. pop() - Removes and returns value for key
    test_dict = sample_dict.copy()
    popped = test_dict.pop('b')
    print(f"test_dict.pop('b'): {popped}")  # Expected: 2
    print(f"Dictionary after pop: {test_dict}")  # Expected: {'a': 1, 'c': 3}
    
    # 8. popitem() - Removes and returns last key-value pair
    test_dict2 = sample_dict.copy()
    popped_item = test_dict2.popitem()
    print(f"test_dict2.popitem(): {popped_item}")  # Expected: ('c', 3)
    print(f"Dictionary after popitem: {test_dict2}")  # Expected: {'a': 1, 'b': 2}
    
    # 9. clear() - Removes all items
    test_dict3 = sample_dict.copy()
    test_dict3.clear()
    print(f"Dictionary after clear(): {test_dict3}")  # Expected: {}
    
    # 10. copy() - Returns shallow copy
    copied_dict = sample_dict.copy()
    print(f"sample_dict.copy(): {copied_dict}")  # Expected: {'a': 1, 'b': 2, 'c': 3}
    
    # 11. update() - Updates dictionary with another dictionary
    test_dict4 = {'a': 1}
    test_dict4.update({'b': 2, 'c': 3})
    print(f"After update({'b': 2, 'c': 3}): {test_dict4}")  # Expected: {'a': 1, 'b': 2, 'c': 3}
    
    # 12. setdefault() - Returns value or sets default if key doesn't exist
    test_dict5 = {'a': 1}
    existing = test_dict5.setdefault('a', 100)
    new_key = test_dict5.setdefault('b', 2)
    print(f"setdefault('a', 100): {existing}")  # Expected: 1
    print(f"setdefault('b', 2): {new_key}")  # Expected: 2
    print(f"Dictionary after setdefault: {test_dict5}")  # Expected: {'a': 1, 'b': 2}
    
    # 13. fromkeys() - Creates dictionary with specified keys and value
    keys_list = ['x', 'y', 'z']
    new_dict_fromkeys = dict.fromkeys(keys_list, 0)
    print(f"dict.fromkeys(['x', 'y', 'z'], 0): {new_dict_fromkeys}")  # Expected: {'x': 0, 'y': 0, 'z': 0}
    
    # Built-in functions that work with dictionaries
    print("\n=== Built-in Functions with Dictionaries ===")
    
    # 14. str() - String representation
    str_repr = str(sample_dict)
    print(f"str(sample_dict): {str_repr}")  # Expected: {'a': 1, 'b': 2, 'c': 3}
    
    # 15. bool() - Boolean conversion
    empty_dict = {}
    print(f"bool(sample_dict): {bool(sample_dict)}")  # Expected: True
    print(f"bool(empty_dict): {bool(empty_dict)}")  # Expected: False
    
    # 16. sorted() - Returns sorted keys
    unsorted_dict = {'z': 3, 'a': 1, 'b': 2}
    sorted_keys = sorted(unsorted_dict)
    print(f"sorted(unsorted_dict): {sorted_keys}")  # Expected: ['a', 'b', 'z']
    
    # 17. max() and min() - Maximum and minimum keys
    max_key = max(sample_dict)
    min_key = min(sample_dict)
    print(f"max(sample_dict): {max_key}")  # Expected: c
    print(f"min(sample_dict): {min_key}")  # Expected: a
    
    # 18. sum() - Sum of keys (if numeric)
    numeric_dict = {1: 'a', 2: 'b', 3: 'c'}
    sum_keys = sum(numeric_dict)
    print(f"sum(numeric_dict keys): {sum_keys}")  # Expected: 6
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_dictionary_functions()