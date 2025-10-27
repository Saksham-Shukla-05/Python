# Common String Functions in Python



text = "Hello World! Python Programming"
text_with_spaces = "   Python is Amazing   "
mixed_case = "PyThOn"
numbers = "12345"
words = ["Python", "is", "awesome"]

# 1. Basic String Operations
print("--- Basic String Operations ---")
print(f"Length: {len(text)}")  # Get length of string
print(f"Convert to upper: {text.upper()}")  # Convert to uppercase
print(f"Convert to lower: {text.lower()}")  # Convert to lowercase
print(f"Title case: {text.title()}")  # Capitalize first letter of each word
print(f"Capitalize: {text.capitalize()}")  # Capitalize first letter of string

# 2. String Checking Methods
print("\n--- String Checking Methods ---")
print(f"Is alphanumeric? {text.isalnum()}")  # Check if string is alphanumeric
print(f"Is alphabetic? {text.isalpha()}")    # Check if string contains only letters
print(f"Is numeric? {numbers.isnumeric()}")   # Check if string contains only numbers
print(f"Is lowercase? {text.islower()}")      # Check if string is all lowercase
print(f"Is uppercase? {text.isupper()}")      # Check if string is all uppercase

# 3. String Search and Replace
print("\n--- String Search and Replace ---")
print(f"Count 'o': {text.count('o')}")        # Count occurrences
print(f"Find 'World': {text.find('World')}")  # Find first occurrence (returns index)
print(f"Replace: {text.replace('World', 'Python')}")  # Replace substring
print(f"Split words: {text.split()}")          # Split string into list
print(f"Join words: {''.join(words)}")         # Join list into string

# 4. String Formatting and Cleaning
print("\n--- String Formatting and Cleaning ---")
print(f"Strip whitespace: '{text_with_spaces.strip()}'")    # Remove leading/trailing whitespace
print(f"Left strip: '{text_with_spaces.lstrip()}'")         # Remove leading whitespace
print(f"Right strip: '{text_with_spaces.rstrip()}'")        # Remove trailing whitespace
print(f"Center string: {text.center(40, '*')}")             # Center string with padding

# 5. String Checking Methods 
print("\n--- Advanced String Checking ---")
print(f"Starts with 'Hello': {text.startswith('Hello')}")   # Check start of string
print(f"Ends with 'ing': {text.endswith('ing')}")          # Check end of string
print(f"Find index: {text.index('World')}")                # Find index (raises error if not found)
print(f"Swap case: {mixed_case.swapcase()}")               # Swap case of each character

# 6. String Partition and Splitting
print("\n--- String Partition and Splitting ---")
print(f"Partition at 'World': {text.partition('World')}")   # Split into 3 parts at first occurrence
print(f"Split lines: {text.splitlines()}")                  # Split at line boundaries
print(f"Split with maxsplit: {text.split(' ', 1)}")        # Split with maximum splits

# 7. String Alignment
print("\n--- String Alignment ---")
print(f"Left justify: {text.ljust(30, '-')}")    # Left justify with padding
print(f"Right justify: {text.rjust(30, '-')}")   # Right justify with padding
print(f"Zero fill: {'123'.zfill(5)}")           # Pad with zeros on the left

# 8. String Translation and Encoding
print("\n--- String Translation ---")
trans_table = str.maketrans("aeiou", "12345")    # Create translation table
print(f"Translated: {text.translate(trans_table)}")  # Apply translation
print(f"Encoded as ASCII: {text.encode('ascii', 'ignore')}")  # Encode string
