#Data type ----------------------------------

#numeric------------------------------------------------

age = 13
b = 12.8
e = 3.14 + 6j
print(f"age:{age}, float:{b},complex num:{e}, type of : {type(age)}, imaginary: {e.imag}, real number : {e.real}")

#-------------------------------------------------------

str1 = "Indian country"
str2 = 'Indian Country New'
str3 = '''Indian Country Triple'''
concat = str1 + " " + str2
slicing_ = str3[0:8]
uppper = str3.upper()
lowerr = str3.lower()
splitoperation = str3.split(", ")
joinn = "-".join(lowerr)
repeat = "SHukla" * 3
def hello():
    return "Hello Python"  # Make sure it returns a value

print(f"Concat: {concat}, Repeat: {repeat}, Slicing_Num: {slicing_}, upper: {uppper}, lower: {lowerr}, splitoperation: {splitoperation}, joinn: {joinn}, fn Call: {hello()}")

#----------------------------------------------------

my_list = [1,2,'Python',4.3,3,2]
my_list.append('new')
print(my_list[1:3])
my_list.remove(2)   # only removes first occurence of 2
poped = my_list.pop() # removes the last element 
newl = [3,4,5,2,1]
newl.sort()
for new in newl:
    print(new, end=" ")
print("\npoped element --> ", poped)
for lis in my_list:
    print(lis,end=" ")
    
#-----------------------------------

# Performance: Lists are backed by dynamic arrays, so accessing elements by index is O(1) (constant time), 
#   but insertions/removals (except at the end) may take O(n) time due to shifting of elements.
#Memory Efficiency: Lists are dynamic arrays, which means they allocate extra space as they grow.

#Common Use Cases:
#Use lists when you need an ordered, dynamic collection of elements.
#Use for operations like sorting, filtering, or processing a sequence of items.

#--------------------------------------------------

my_tuple = (1,2, "Hai", "9.3")
first, second, name, flo = my_tuple  # unpacking 
print("\n")
is_tuple = (8) # int
is_tuple =(8,) # tuple needs comma for one single element
print(type(is_tuple))
print(first)
# my_tuple[0] = 100  tuple does't support item assignment means 
print("\n")
for t in my_tuple:
    print(t , end=" ")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

my_tuple = (1, 2, 3, 'Python')
print(2 in my_tuple)  # Output: True

#Tuples vs Lists:
## Tuples are immutable, while lists are mutable. immutable means cannot modified or change
## Tuples use less memory and are faster to process than lists.
## Lists are more flexible but come with performance trade-offs.(like )


nested_tuple = ((1, 2), (3, 4), (5, 6))

# Accessing elements of nested tuples
print(nested_tuple[1])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3

# -------------------------------------------------------
#Key Features of Sets:
#Unordered: Sets do not maintain any particular order.
#Unique Elements: Sets automatically eliminate duplicates.
#Mutable: Sets are mutable, meaning you can add or remove elements.
#No Indexing: You can't access elements using an index.

# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
# Adding elements to a set using add()
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4}

# Duplicates are automatically removed
my_set_with_duplicates = {1, 2, 2, 3}
print(my_set_with_duplicates)  # Output: {1, 2, 3}

# Remove an element
my_set = {1, 2, 3, 4}
my_set.remove(3)  # Removes 3
print(my_set)  # Output: {1, 2, 4}

# Discard an element (no error if the element doesn't exist)
my_set.discard(5)  # No error, even though 5 is not in the set
#-----------------------------------------------------------------
'''
Key Features of Dictionary:
Key-Value Pairs: Each element consists of a key and a corresponding value.
Unordered: Dictionaries do not maintain any specific order (since Python 3.7, insertion order is preserved).
Mutable: You can modify dictionaries (add, update, or remove key-value pairs).
Unique Keys: Keys must be unique; if you use a duplicate key, the last value assigned will overwrite the previous one.
Efficient: Accessing values by keys is very fast, on average O(1).
'''
# Creating a dictionary with key-value pairs
my_dict = {'name': 'Hari', 'age': 25, 'language': 'Python'}
print(my_dict)  # Output: {'name': 'Hari', 'age': 25, 'language': 'Python'}

# Creating an empty dictionary
empty_dict = {}
# Accessing values using keys
print(my_dict['name'])  # Output: 'Hari'

# Using the get() method (prevents KeyError if the key doesn't exist)
print(my_dict.get('age'))  # Output: 25
print(my_dict.get('salary', 'Not Available'))  # Output: 'Not Available'
my_dict['salary'] = 30000
print(my_dict)
# Checking if a key exists
if 'name' in my_dict:
    print("Key 'name' exists")
    
# Get all keys
print("keys", my_dict.keys())  # Output: dict_keys(['name', 'age'])

# Get all values

print("gosh value::" , my_dict.values())  # Output: dict_values(['Hari', 26])

# Get all key-value pairs
print(my_dict.items())  # Output: dict_items([('name', 'Hari'), ('age', 26)])

for value in my_dict.values():
    print("iterating values " , value)
    
'''
1. O(1) – Constant Time
Meaning: The operation takes the same amount of time, regardless of the size of the input.
Examples:
Accessing an element by index in a list or array (my_list[5]).
Inserting or deleting an element in a hash-based collection like a dictionary or set (on average).
When it's best: O(1) is the best time complexity because the operation is done in constant time, regardless of input size. It’s highly efficient.
2. O(log n) – Logarithmic Time
Meaning: The operation time increases logarithmically with the size of the input.

Examples:

Searching in a balanced binary search tree (e.g., a binary search on a sorted array).
Operations in binary heap data structures.
When it's good: O(log n) is very efficient, especially with large inputs. Algorithms that reduce the problem size significantly in each step (like binary search) have logarithmic complexity.

3. O(n) – Linear Time
Meaning: The operation time increases linearly with the size of the input.
Examples:
Searching for an element in an unsorted list.
Iterating through a list or an array.
When it's acceptable: O(n) is reasonable for operations where you need to examine every element (like looping through a list). While it’s not as fast as O(1) or O(log n), it’s still manageable for moderate-sized inputs.
4. O(n log n) – Linearithmic Time
Meaning: The operation is a combination of linear and logarithmic growth.

Examples:

Efficient sorting algorithms, such as Merge Sort, Heapsort, or Quicksort (average case).
Some divide-and-conquer algorithms.
When it's decent: O(n log n) is the best you can get for general-purpose sorting algorithms. It’s much better than O(n²) for large inputs.

5. O(n²) – Quadratic Time
Meaning: The time grows quadratically with the size of the input.

Examples:

Bubble sort, Selection sort, and Insertion sort (in their worst forms).
Nested loops where both loops iterate over the same dataset.
When it's bad: O(n²) is typically considered inefficient for large datasets because the number of operations grows rapidly as input size increases. It’s fine for small datasets but becomes prohibitive for larger ones.

6. O(2ⁿ) – Exponential Time
Meaning: The time doubles with each addition to the input size.

Examples:

Solving the Traveling Salesman Problem using brute force.
Recursive algorithms that solve problems like the Fibonacci sequence without memoization.
When it's very bad: Exponential time is impractical for even moderately sized inputs. These algorithms can become computationally infeasible very quickly.

7. O(n!) – Factorial Time
Meaning: The time grows factorially as the input size increases.

Examples:

Solving combinatorial problems (e.g., generating all permutations of a set).
When it's terrible: O(n!) is the worst-case time complexity and is generally avoided in practical applications.

Comparison: Which Time Complexity is Better?
Best: O(1) is the best because it guarantees constant time for operations regardless of the input size. This is the most efficient time complexity.

Very Good: O(log n) is excellent, especially when working with large data, as it scales much better than linear time.

Good: O(n) is acceptable for operations that must examine each element of the input, though it can become slow for very large datasets.

Decent: O(n log n) is the best achievable time complexity for sorting and many divide-and-conquer algorithms.

Poor: O(n²) and worse should generally be avoided for large datasets as they become inefficient very quickly.

Practical Summary:
Prefer O(1) when possible, as it’s the fastest and doesn’t depend on the input size.
O(log n) is great for efficient searching algorithms like binary search.
O(n) is manageable for small to moderately sized datasets.
O(n log n) is generally acceptable for algorithms like sorting.
O(n²) or worse should be avoided unless dealing with small datasets or there is no better alternative.
'''








