"""
TIMESTAMP DICTIONARY MANAGER - COMPLETE TUTORIAL

This program demonstrates a dictionary-based timestamp management system with:
1. Adding entries with automatic timestamps
2. Updating timestamps for existing entries  
3. Removing timestamps while preserving values
4. Comparing timestamps between entries
5. Finding newest and oldest entries

STEP-BY-STEP PROCESS:
Step 1: Initialize empty dictionary storage
Step 2: Add entries with current timestamp
Step 3: Update existing entry timestamps  
Step 4: Remove timestamps (keep values only)
Step 5: Compare timestamps between two entries
Step 6: Find entry with most recent timestamp
Step 7: Find entry with oldest timestamp

LEARNING OBJECTIVES:
- Understand dictionary data structure with nested values
- Learn datetime handling and formatting
- Practice conditional logic and error handling
- Implement timestamp comparison algorithms
- Build a practical data management system

TIME COMPLEXITY ANALYSIS:
- add_entry(): O(1) - direct dictionary access
- update_timestamp(): O(1) - dictionary key lookup
- compare_timestamps(): O(1) - parse and compare two timestamps
- get_newest_entry(): O(n) - iterate through all entries
- get_oldest_entry(): O(n) - iterate through all entries
"""

from datetime import datetime

class TimestampManager:
    def __init__(self):
        """
        STEP 1: Initialize empty dictionary storage
        - self.data will store all entries as nested dictionaries
        - Each entry has format: {key: {'value': data, 'timestamp': datetime_string}}
        """
        self.data = {}
    
    def add_entry(self, key, value):
        """
        STEP 2: Add or update an entry with current timestamp
        - Generate current timestamp in standardized format
        - Store both value and timestamp in nested dictionary
        - Return the created entry for confirmation
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data[key] = {
            'value': value,
            'timestamp': timestamp
        }
        return self.data[key]
        # Expected output: {'value': 'test_value', 'timestamp': '2025-09-20 13:07:00'}
    
    def update_timestamp(self, key):
        """
        STEP 3: Update timestamp for existing entry
        - Check if key exists in dictionary
        - Update only the timestamp, preserve original value
        - Return updated entry or None if key not found
        """
        if key in self.data:
            self.data[key]['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return self.data[key]
        return None
        # Expected output: {'value': 'existing_value', 'timestamp': '2025-09-20 13:07:01'}
    
    def remove_timestamp(self, key):
        """
        STEP 4: Remove timestamp from entry, keep only value
        - Extract the value from existing entry
        - Replace entry with value-only dictionary
        - Useful for converting timestamped entries to simple storage
        """
        if key in self.data:
            value = self.data[key]['value']
            self.data[key] = {'value': value}
            return self.data[key]
        return None
        # Expected output: {'value': 'existing_value'}
    
    def get_entry(self, key):
        """Get entry by key"""
        return self.data.get(key)
        # Expected output: {'value': 'test_value', 'timestamp': '2024-01-15 14:30:25'} or None
    
    def list_all(self):
        """List all entries"""
        return self.data
        # Expected output: {'key1': {'value': 'val1', 'timestamp': '2024-01-15 14:30:25'}, 'key2': {...}}
    
    def compare_timestamps(self, key1, key2):
        """
        Compare timestamps between two entries
        Returns:
        - 1 if key1 is newer than key2
        - -1 if key1 is older than key2  
        - 0 if timestamps are equal
        - None if either key doesn't exist or has no timestamp
        """
        if key1 not in self.data or key2 not in self.data:
            return None
            # Expected output: None (if either key doesn't exist)
        
        entry1 = self.data[key1]
        entry2 = self.data[key2]
        
        # Check if both entries have timestamps
        if 'timestamp' not in entry1 or 'timestamp' not in entry2:
            return None
            # Expected output: None (if either entry has no timestamp)
        
        # Parse timestamps and compare
        try:
            timestamp1 = datetime.strptime(entry1['timestamp'], "%Y-%m-%d %H:%M:%S")
            timestamp2 = datetime.strptime(entry2['timestamp'], "%Y-%m-%d %H:%M:%S")
            
            if timestamp1 > timestamp2:
                return 1
                # Expected output: 1 (key1 is newer)
            elif timestamp1 < timestamp2:
                return -1
                # Expected output: -1 (key1 is older)
            else:
                return 0
                # Expected output: 0 (timestamps are equal)
                
        except ValueError:
            return None
            # Expected output: None (if timestamp format is invalid)
    
    def get_newest_entry(self):
        """
        Find the entry with the most recent timestamp
        Returns tuple: (key, entry) or (None, None) if no timestamped entries
        """
        newest_key = None
        newest_timestamp = None
        
        for key, entry in self.data.items():
            if 'timestamp' not in entry:
                continue
                
            try:
                current_timestamp = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
                if newest_timestamp is None or current_timestamp > newest_timestamp:
                    newest_timestamp = current_timestamp
                    newest_key = key
            except ValueError:
                continue
        
        if newest_key:
            return (newest_key, self.data[newest_key])
        return (None, None)
        # Expected output: ('user2', {'value': 'Jane Smith', 'timestamp': '2024-01-15 15:45:30'})
    
    def get_oldest_entry(self):
        """
        Find the entry with the oldest timestamp
        Returns tuple: (key, entry) or (None, None) if no timestamped entries
        """
        oldest_key = None
        oldest_timestamp = None
        
        for key, entry in self.data.items():
            if 'timestamp' not in entry:
                continue
                
            try:
                current_timestamp = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
                if oldest_timestamp is None or current_timestamp < oldest_timestamp:
                    oldest_timestamp = current_timestamp
                    oldest_key = key
            except ValueError:
                continue
        
        if oldest_key:
            return (oldest_key, self.data[oldest_key])
        return (None, None)
        # Expected output: ('user1', {'value': 'John Doe', 'timestamp': '2024-01-15 14:30:25'})

# Test application
if __name__ == "__main__":
    tm = TimestampManager()
    
    print("=== Timestamp Manager Test ===")
    
    # Test adding entries
    print("\n1. Adding entries:")
    print(tm.add_entry("user1", "John Doe"))
    print(tm.add_entry("user2", "Jane Smith"))
    
    # Test updating timestamp
    print("\n2. Updating timestamp for user1:")
    print(tm.update_timestamp("user1"))
    
    # Test removing timestamp
    print("\n3. Removing timestamp from user2:")
    print(tm.remove_timestamp("user2"))
    
    # Test getting specific entry
    print("\n4. Getting user1 entry:")
    print(tm.get_entry("user1"))
    
    # Test listing all entries
    print("\n5. All entries:")
    print(tm.list_all())
    
    # Test non-existent key
    print("\n6. Getting non-existent key:")
    print(tm.get_entry("user3"))
    
    # Test timestamp comparison functions
    print("\n7. Timestamp comparison tests:")
    
    # Add a third entry for better testing
    import time
    time.sleep(1)  # Ensure different timestamp
    tm.add_entry("user3", "Bob Johnson")
    
    # Compare timestamps
    print(f"Comparing user1 vs user3: {tm.compare_timestamps('user1', 'user3')}")
    print(f"Comparing user3 vs user1: {tm.compare_timestamps('user3', 'user1')}")
    print(f"Comparing user2 vs user1 (user2 has no timestamp): {tm.compare_timestamps('user2', 'user1')}")
    print(f"Comparing non-existent keys: {tm.compare_timestamps('user4', 'user5')}")
    
    # Find newest and oldest entries
    print(f"\nNewest entry: {tm.get_newest_entry()}")
    print(f"Oldest entry: {tm.get_oldest_entry()}")
    
    print("\n=== Test Complete ===")
    
    # Show interpretation of comparison results
    print("\nComparison result meanings:")
    print("  1: First key is newer than second key")
    print(" -1: First key is older than second key") 
    print("  0: Timestamps are equal")
    print("None: Keys don't exist or missing timestamps")