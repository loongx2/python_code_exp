import json
from datetime import datetime


def json_to_dict(json_string):
    """
    Convert JSON string to Python dictionary.
    
    Args:
        json_string (str): Valid JSON string
    
    Returns:
        dict: Python dictionary representation of JSON
    
    Raises:
        json.JSONDecodeError: If JSON string is invalid
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def dict_to_json(dictionary, indent=None, sort_keys=False):
    """
    Convert Python dictionary to JSON string.
    
    Args:
        dictionary (dict): Python dictionary to convert
        indent (int, optional): Number of spaces for indentation (pretty printing)
        sort_keys (bool): Whether to sort keys alphabetically
    
    Returns:
        str: JSON string representation of dictionary
    
    Raises:
        TypeError: If dictionary contains non-serializable objects
    """
    try:
        return json.dumps(dictionary, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    except TypeError as e:
        print(f"Error converting to JSON: {e}")
        return None


def json_file_to_dict(filename):
    """
    Read JSON from file and convert to dictionary.
    
    Args:
        filename (str): Path to JSON file
    
    Returns:
        dict: Python dictionary or None if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None


def dict_to_json_file(dictionary, filename, indent=4):
    """
    Convert dictionary to JSON and save to file.
    
    Args:
        dictionary (dict): Python dictionary to save
        filename (str): Output file path
        indent (int): Indentation for pretty printing
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=indent, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error writing JSON to file: {e}")
        return False


# Demonstration and test cases
def main():
    print("JSON ↔ Dictionary Conversion Demo")
    print("=" * 40)
    
    # Test Case 1: Simple dictionary to JSON
    print("\n1. Dictionary to JSON:")
    simple_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "is_student": False
    }
    print(f"Original dict: {simple_dict}")
    # Expected output: Original dict: {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_student': False}
    json_string = dict_to_json(simple_dict, indent=2)
    print(f"JSON string:\n{json_string}")
    # Expected output: JSON string:
    #                  {
    #                    "name": "Alice",
    #                    "age": 30,
    #                    "city": "New York",
    #                    "is_student": false
    #                  }
    
    # Test Case 2: JSON to dictionary
    print("\n2. JSON to Dictionary:")
    json_data = '{"product": "laptop", "price": 999.99, "in_stock": true, "specs": {"ram": "16GB", "storage": "512GB"}}'
    print(f"JSON string: {json_data}")
    # Expected output: JSON string: {"product": "laptop", "price": 999.99, "in_stock": true, "specs": {"ram": "16GB", "storage": "512GB"}}
    converted_dict = json_to_dict(json_data)
    print(f"Converted dict: {converted_dict}")
    # Expected output: Converted dict: {'product': 'laptop', 'price': 999.99, 'in_stock': True, 'specs': {'ram': '16GB', 'storage': '512GB'}}
    
    # Test Case 3: Complex nested structure
    print("\n3. Complex nested structure:")
    complex_dict = {
        "users": [
            {"id": 1, "name": "John", "hobbies": ["reading", "swimming"]},
            {"id": 2, "name": "Jane", "hobbies": ["painting", "cycling"]}
        ],
        "metadata": {
            "total_users": 2,
            "last_updated": "2025-09-19",
            "active": True
        }
    }
    print("Original complex dict:")
    # Expected output: Original complex dict:
    print(dict_to_json(complex_dict, indent=2))
    # Expected output: Pretty-printed JSON showing nested users array and metadata object
    
    # Test Case 4: Round-trip conversion (dict → JSON → dict)
    print("\n4. Round-trip conversion:")
    original = {"a": 1, "b": [2, 3, 4], "c": {"nested": True}}
    json_str = dict_to_json(original)
    back_to_dict = json_to_dict(json_str)
    print(f"Original: {original}")
    # Expected output: Original: {'a': 1, 'b': [2, 3, 4], 'c': {'nested': True}}
    print(f"After round-trip: {back_to_dict}")
    # Expected output: After round-trip: {'a': 1, 'b': [2, 3, 4], 'c': {'nested': True}}
    print(f"Are they equal? {original == back_to_dict}")
    # Expected output: Are they equal? True
    
    # Test Case 5: Error handling - Invalid JSON
    print("\n5. Error handling - Invalid JSON:")
    invalid_json = '{"name": "John", "age":}'  # Missing value
    result = json_to_dict(invalid_json)
    print(f"Result for invalid JSON: {result}")
    # Expected output: Error parsing JSON: Expecting value: line 1 column 24 (char 23)
    #                  Result for invalid JSON: None
    
    # Test Case 6: JSON with special characters
    print("\n6. JSON with special characters:")
    special_dict = {
        "message": "Hello, 世界! 🌍",
        "symbols": ["α", "β", "γ"],
        "unicode": "café naïve résumé"
    }
    json_with_unicode = dict_to_json(special_dict, indent=2)
    print("JSON with Unicode:")
    # Expected output: JSON with Unicode:
    print(json_with_unicode)
    # Expected output: Pretty-printed JSON with Unicode characters like 世界, 🌍, α, β, γ, café, naïve, résumé
    
    # Test Case 7: File operations (create test file)
    print("\n7. File operations:")
    test_filename = "test_data.json"
    
    # Save to file
    test_data = {
        "timestamp": "2025-09-19T10:30:00",
        "data": {
            "temperature": 23.5,
            "humidity": 65,
            "readings": [21.0, 22.5, 23.5, 24.0]
        }
    }
    
    success = dict_to_json_file(test_data, test_filename)
    print(f"Saved to file: {success}")
    # Expected output: Saved to file: True
    
    # Read from file
    loaded_data = json_file_to_dict(test_filename)
    print(f"Loaded from file: {loaded_data}")
    # Expected output: Loaded from file: {'timestamp': '2025-09-19T10:30:00', 'data': {'temperature': 23.5, 'humidity': 65, 'readings': [21.0, 22.5, 23.5, 24.0]}}
    
    print(f"Data integrity check: {test_data == loaded_data}")
    # Expected output: Data integrity check: True
    
    print("\n" + "=" * 40)
    # Expected output: ========================================
    print("Demo completed!")
    # Expected output: Demo completed!


if __name__ == "__main__":
    main()