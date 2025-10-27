# Strings are immutable, they cannot be changed
   
# Strings can be written in single or triple quotes
string = "Hello World"

# Slicing in Strings
print("Original string:", string)

# Basic Slicing - syntax: string[start:end]
# Note: end index is exclusive
print("\n--- Basic Slicing ---")
first_three = string[0:3]    # Get first 3 characters
print("First three chars:", first_three)

middle_part = string[4:10]   # Get characters from index 4 to 9
print("Middle part:", middle_part)

# Omitting start/end index
print("\n--- Omitting Indices ---")
from_start = string[:5]      # Same as string[0:5]
print("From start to 5:", from_start)

till_end = string[8:]        # From index 8 to end
print("From 8 to end:", till_end)

# Negative Indexing
print("\n--- Negative Indexing ---")
last_five = string[-5:]      # Last 5 characters
print("Last five chars:", last_five)

string2 = "Hello"
# Trick to tackel negative indexing questions 
print(string2[-4 : -1])
print(string2[1 : 4])


except_last = string[:-1]    # Everything except last character
print("Everything except last:", except_last)

# Step parameter - syntax: string[start:end:step]
print("\n--- Using Step Parameter ---")
every_second = string[::2]   # Every second character
print("Every second char:", every_second)

reversed_string = string[::-1] # Reverse the string
print("Reversed string:", reversed_string)