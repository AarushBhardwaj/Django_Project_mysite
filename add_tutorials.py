#!/usr/bin/env python
"""Script to add Python basics tutorials to the database."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')

import django
django.setup()

from django.utils import timezone
from main.models import TutorialSeries, Tutorial

# Get the Python Basics series
basics_series = TutorialSeries.objects.get(tutorial_series="Python Basics")

# Define all tutorials
tutorials = [
    {
        "title": "Introduction & Setup",
        "slug": "python-introduction-setup",
        "content": """
<h5>Welcome to Python!</h5>
<p>Python is one of the most popular programming languages in the world. It's known for its simple, readable syntax that makes it perfect for beginners while being powerful enough for experts.</p>

<h5>Installing Python</h5>
<p>To get started, you need to install Python on your computer:</p>
<ol>
    <li>Visit <a href="https://python.org/downloads" target="_blank">python.org/downloads</a></li>
    <li>Download the latest version (Python 3.x)</li>
    <li>Run the installer and <strong>check "Add Python to PATH"</strong></li>
    <li>Click "Install Now"</li>
</ol>

<p>To verify installation, open a terminal/command prompt and type:</p>
<pre><code>python --version</code></pre>

<h5>Choosing an IDE</h5>
<p>An IDE (Integrated Development Environment) makes coding easier. Here are popular choices:</p>

<h6>VS Code (Recommended for beginners)</h6>
<ul>
    <li>Free and lightweight</li>
    <li>Download from <a href="https://code.visualstudio.com" target="_blank">code.visualstudio.com</a></li>
    <li>Install the "Python" extension for syntax highlighting and debugging</li>
</ul>

<h6>PyCharm</h6>
<ul>
    <li>Full-featured Python IDE</li>
    <li>Community Edition is free</li>
    <li>Download from <a href="https://jetbrains.com/pycharm" target="_blank">jetbrains.com/pycharm</a></li>
</ul>

<h6>IDLE</h6>
<ul>
    <li>Comes bundled with Python</li>
    <li>Simple and good for quick testing</li>
</ul>

<h5>Your First Python Program</h5>
<p>Create a new file called <code>hello.py</code> and add:</p>
<pre><code>print("Hello, World!")</code></pre>
<p>Run it with: <code>python hello.py</code></p>

<p>Congratulations! You've written your first Python program!</p>
"""
    },
    {
        "title": "Basic Syntax",
        "slug": "python-basic-syntax",
        "content": """
<h5>Python Syntax Basics</h5>
<p>Python has a clean, readable syntax. Let's explore the fundamentals.</p>

<h5>Indentation</h5>
<p>Python uses <strong>indentation</strong> (whitespace) to define code blocks, unlike other languages that use braces <code>{}</code>.</p>

<pre><code># Correct indentation
if True:
    print("This is indented")
    print("Same block")

# Wrong indentation (will cause an error)
if True:
print("Error!")  # IndentationError</code></pre>

<p><strong>Important:</strong> Use 4 spaces for each indentation level. Most editors do this automatically.</p>

<h5>Comments</h5>
<p>Comments help explain your code. Python ignores them when running.</p>

<pre><code># This is a single-line comment

# You can have multiple
# single-line comments

\"\"\"
This is a multi-line comment
(also called a docstring).
It can span multiple lines.
\"\"\"

print("Hello")  # Comments can also go at the end of a line</code></pre>

<h5>The print() Function</h5>
<p>The <code>print()</code> function displays output to the screen.</p>

<pre><code># Basic printing
print("Hello, World!")

# Printing multiple items
print("Hello", "World")  # Output: Hello World

# Printing numbers
print(42)
print(3.14)

# Printing with variables
name = "Alice"
print("Hello,", name)  # Output: Hello, Alice

# Using f-strings (formatted strings)
age = 25
print(f"I am {age} years old")  # Output: I am 25 years old

# Print with custom separator
print("a", "b", "c", sep="-")  # Output: a-b-c

# Print without newline at the end
print("Hello ", end="")
print("World")  # Output: Hello World (on same line)</code></pre>

<h5>Case Sensitivity</h5>
<p>Python is case-sensitive. <code>Name</code>, <code>name</code>, and <code>NAME</code> are different variables.</p>

<pre><code>name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)  # Alice
print(Name)  # Bob
print(NAME)  # Charlie</code></pre>
"""
    },
    {
        "title": "Variables & Data Types",
        "slug": "python-variables-data-types",
        "content": """
<h5>Variables in Python</h5>
<p>Variables store data that can be used and changed throughout your program.</p>

<pre><code># Creating variables (no need to declare type)
name = "Alice"
age = 25
height = 5.6
is_student = True

# Variables can be reassigned
age = 26
age = "twenty-six"  # Can even change type (not recommended)</code></pre>

<h5>Variable Naming Rules</h5>
<ul>
    <li>Must start with a letter or underscore (_)</li>
    <li>Can contain letters, numbers, and underscores</li>
    <li>Case-sensitive (<code>age</code> ≠ <code>Age</code>)</li>
    <li>Cannot use Python keywords (<code>if</code>, <code>for</code>, <code>class</code>, etc.)</li>
</ul>

<pre><code># Good variable names
user_name = "Alice"
userAge = 25
_private = "hidden"
MAX_SIZE = 100

# Bad variable names (will cause errors)
# 2fast = "error"      # Can't start with number
# my-var = "error"     # Can't use hyphens
# class = "error"      # Can't use keywords</code></pre>

<h5>Data Types</h5>

<h6>Integers (int)</h6>
<p>Whole numbers without decimals.</p>
<pre><code>age = 25
year = 2024
negative = -10
big_number = 1_000_000  # Underscores for readability

print(type(age))  # &lt;class 'int'&gt;</code></pre>

<h6>Floats (float)</h6>
<p>Numbers with decimal points.</p>
<pre><code>price = 19.99
pi = 3.14159
scientific = 1.5e10  # Scientific notation (1.5 × 10^10)

print(type(price))  # &lt;class 'float'&gt;</code></pre>

<h6>Strings (str)</h6>
<p>Text data enclosed in quotes.</p>
<pre><code># Single or double quotes
name = "Alice"
message = 'Hello, World!'

# Multi-line strings
paragraph = \"\"\"This is a
multi-line
string.\"\"\"

# String operations
greeting = "Hello"
print(greeting + " World")  # Concatenation: Hello World
print(greeting * 3)         # Repetition: HelloHelloHello
print(len(greeting))        # Length: 5
print(greeting[0])          # Indexing: H
print(greeting[1:4])        # Slicing: ell

print(type(name))  # &lt;class 'str'&gt;</code></pre>

<h6>Booleans (bool)</h6>
<p>True or False values.</p>
<pre><code>is_active = True
is_admin = False

# Result of comparisons
print(5 > 3)   # True
print(5 == 3)  # False

print(type(is_active))  # &lt;class 'bool'&gt;</code></pre>

<h5>Type Conversion</h5>
<pre><code># Convert between types
num_str = "42"
num_int = int(num_str)    # String to int: 42
num_float = float(num_str) # String to float: 42.0

age = 25
age_str = str(age)        # Int to string: "25"

print(bool(1))   # True
print(bool(0))   # False
print(bool(""))  # False (empty string)
print(bool("a")) # True (non-empty string)</code></pre>

<h5>Checking Types</h5>
<pre><code>x = 42
print(type(x))              # &lt;class 'int'&gt;
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False</code></pre>
"""
    },
    {
        "title": "Operators",
        "slug": "python-operators",
        "content": """
<h5>Python Operators</h5>
<p>Operators are symbols that perform operations on values and variables.</p>

<h5>Arithmetic Operators</h5>
<p>Used for mathematical calculations.</p>
<pre><code>a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor Division: 3 (rounds down)
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 1000 (10^3)

# Order of operations (PEMDAS)
result = 2 + 3 * 4    # 14 (not 20)
result = (2 + 3) * 4  # 20 (parentheses first)</code></pre>

<h5>Assignment Operators</h5>
<p>Used to assign and update values.</p>
<pre><code>x = 10      # Assign 10 to x

x += 5      # x = x + 5  → 15
x -= 3      # x = x - 3  → 12
x *= 2      # x = x * 2  → 24
x /= 4      # x = x / 4  → 6.0
x //= 2     # x = x // 2 → 3.0
x %= 2      # x = x % 2  → 1.0
x **= 3     # x = x ** 3 → 1.0</code></pre>

<h5>Comparison Operators</h5>
<p>Used to compare values. Returns True or False.</p>
<pre><code>a = 10
b = 5

print(a == b)   # Equal to: False
print(a != b)   # Not equal to: True
print(a > b)    # Greater than: True
print(a < b)    # Less than: False
print(a >= b)   # Greater than or equal: True
print(a <= b)   # Less than or equal: False

# Comparing strings (alphabetically)
print("apple" < "banana")  # True
print("A" < "a")           # True (uppercase comes first)</code></pre>

<h5>Logical Operators</h5>
<p>Used to combine conditional statements.</p>
<pre><code>x = True
y = False

# and - Both must be True
print(x and y)  # False
print(x and x)  # True

# or - At least one must be True
print(x or y)   # True
print(y or y)   # False

# not - Reverses the boolean
print(not x)    # False
print(not y)    # True

# Practical example
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True

# Short-circuit evaluation
# Python stops evaluating as soon as result is determined
print(False and print("Won't print"))  # False
print(True or print("Won't print"))    # True</code></pre>

<h5>Identity Operators</h5>
<pre><code>a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same values)
print(a is b)   # False (different objects in memory)
print(a is c)   # True (same object)
print(a is not b)  # True</code></pre>

<h5>Membership Operators</h5>
<pre><code>fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works with strings too
print("a" in "apple")  # True</code></pre>
"""
    },
    {
        "title": "Data Structures",
        "slug": "python-data-structures",
        "content": """
<h5>Python Data Structures</h5>
<p>Data structures help you organize and store collections of data.</p>

<h5>Lists</h5>
<p>Ordered, mutable (changeable) collections. Use square brackets <code>[]</code>.</p>
<pre><code># Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Accessing elements (0-indexed)
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)

# Slicing
print(fruits[0:2])  # ['apple', 'banana']

# Modifying lists
fruits[0] = "apricot"        # Change item
fruits.append("date")        # Add to end
fruits.insert(1, "blueberry") # Insert at position
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove and return last item
del fruits[0]                # Delete by index

# List operations
print(len(fruits))           # Length
print("apple" in fruits)     # Check membership
fruits.sort()                # Sort in place
fruits.reverse()             # Reverse in place
new_list = fruits.copy()     # Create a copy

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]</code></pre>

<h5>Tuples</h5>
<p>Ordered, immutable (unchangeable) collections. Use parentheses <code>()</code>.</p>
<pre><code># Creating tuples
point = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Note the comma for single-item tuple

# Accessing elements
print(colors[0])   # red
print(colors[-1])  # blue

# Tuples are immutable
# colors[0] = "yellow"  # Error!

# Tuple unpacking
x, y = point
print(x)  # 10
print(y)  # 20

# Use cases: coordinates, RGB colors, returning multiple values
def get_dimensions():
    return (1920, 1080)

width, height = get_dimensions()</code></pre>

<h5>Dictionaries</h5>
<p>Key-value pairs, unordered. Use curly braces <code>{}</code>.</p>
<pre><code># Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
empty_dict = {}

# Accessing values
print(person["name"])        # Alice
print(person.get("age"))     # 25
print(person.get("job", "N/A"))  # N/A (default if key missing)

# Modifying dictionaries
person["age"] = 26           # Update value
person["job"] = "Engineer"   # Add new key-value
del person["city"]           # Delete key-value
popped = person.pop("job")   # Remove and return value

# Dictionary methods
print(person.keys())         # dict_keys(['name', 'age'])
print(person.values())       # dict_values(['Alice', 26])
print(person.items())        # dict_items([('name', 'Alice'), ('age', 26)])

# Looping through dictionaries
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}</code></pre>

<h5>Sets</h5>
<p>Unordered collections of unique items. Use curly braces <code>{}</code>.</p>
<pre><code># Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 3, 3}  # Duplicates removed: {1, 2, 3}
empty_set = set()  # Not {} (that's an empty dict)

# Adding and removing
fruits.add("date")
fruits.remove("banana")  # Error if not found
fruits.discard("grape")  # No error if not found

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union: {1, 2, 3, 4, 5, 6}
print(a & b)   # Intersection: {3, 4}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric difference: {1, 2, 5, 6}

# Use case: removing duplicates from a list
my_list = [1, 2, 2, 3, 3, 3]
unique = list(set(my_list))  # [1, 2, 3]</code></pre>
"""
    },
    {
        "title": "Control Flow",
        "slug": "python-control-flow",
        "content": """
<h5>Control Flow in Python</h5>
<p>Control flow statements let your program make decisions and execute different code based on conditions.</p>

<h5>The if Statement</h5>
<pre><code>age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")</code></pre>

<h5>The if-else Statement</h5>
<pre><code>age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")</code></pre>

<h5>The if-elif-else Statement</h5>
<p>Use <code>elif</code> (else if) for multiple conditions.</p>
<pre><code>score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")  # Your grade is: B</code></pre>

<h5>Nested if Statements</h5>
<pre><code>age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")</code></pre>

<h5>Conditional Expressions (Ternary Operator)</h5>
<pre><code>age = 20

# Traditional way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (one line)
status = "adult" if age >= 18 else "minor"

print(status)  # adult</code></pre>

<h5>Multiple Conditions</h5>
<pre><code>age = 25
income = 50000

# Using 'and' - both must be True
if age >= 18 and income >= 30000:
    print("Loan approved")

# Using 'or' - at least one must be True
is_student = False
is_senior = True
if is_student or is_senior:
    print("You get a discount")

# Using 'not'
is_banned = False
if not is_banned:
    print("Access granted")</code></pre>

<h5>Checking Multiple Values</h5>
<pre><code>day = "Saturday"

# Instead of multiple 'or' conditions
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")

# Use 'in' with a tuple/list
if day in ("Saturday", "Sunday"):
    print("It's the weekend")

# Checking ranges
age = 25
if 18 <= age <= 65:
    print("Working age")</code></pre>

<h5>Truthy and Falsy Values</h5>
<pre><code># Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy

name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

# Practical use
items = ["apple", "banana"]
if items:  # True if list is not empty
    print(f"You have {len(items)} items")
else:
    print("Your list is empty")</code></pre>

<h5>Match Statement (Python 3.10+)</h5>
<pre><code>status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")</code></pre>
"""
    },
    {
        "title": "Loops",
        "slug": "python-loops",
        "content": """
<h5>Loops in Python</h5>
<p>Loops allow you to execute code repeatedly.</p>

<h5>The for Loop</h5>
<p>Iterate over a sequence (list, tuple, string, range, etc.).</p>
<pre><code># Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string
for char in "Hello":
    print(char)

# Using range()
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# Getting index with enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry</code></pre>

<h5>The while Loop</h5>
<p>Execute code while a condition is True.</p>
<pre><code># Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget to update the condition!

# User input example
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Infinite loop (use with caution)
# while True:
#     print("This runs forever!")
#     # Use break to exit</code></pre>

<h5>The break Statement</h5>
<p>Exit the loop immediately.</p>
<pre><code># Find first even number
numbers = [1, 3, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
# Output: Found even number: 6

# Break in while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # Exit when count reaches 5</code></pre>

<h5>The continue Statement</h5>
<p>Skip the rest of the current iteration and continue with the next.</p>
<pre><code># Skip odd numbers
for i in range(10):
    if i % 2 != 0:
        continue  # Skip to next iteration
    print(i)  # Only prints: 0, 2, 4, 6, 8

# Skip specific items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)  # Prints: apple, cherry</code></pre>

<h5>The else Clause in Loops</h5>
<p>Execute code when the loop completes without hitting <code>break</code>.</p>
<pre><code># else with for loop
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # This runs

# else doesn't run if break is used
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")  # This does NOT run

# Practical use: search
numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found!")  # Runs because target wasn't found</code></pre>

<h5>Nested Loops</h5>
<pre><code># Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Looping through 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # New line after each row</code></pre>

<h5>Loop with zip()</h5>
<pre><code># Iterate over multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")</code></pre>
"""
    },
    {
        "title": "Functions",
        "slug": "python-functions",
        "content": """
<h5>Functions in Python</h5>
<p>Functions are reusable blocks of code that perform specific tasks.</p>

<h5>Defining and Calling Functions</h5>
<pre><code># Define a function
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
greet()  # Can call multiple times</code></pre>

<h5>Functions with Parameters</h5>
<pre><code># Single parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!

# Multiple parameters
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)  # 5 + 3 = 8</code></pre>

<h5>Return Values</h5>
<pre><code># Returning a value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Returning multiple values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")

# Early return
def is_adult(age):
    if age >= 18:
        return True
    return False</code></pre>

<h5>Default Parameter Values</h5>
<pre><code>def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Welcome") # Welcome, Charlie!</code></pre>

<h5>Keyword Arguments</h5>
<pre><code>def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments
describe_person("Alice", 25, "New York")

# Keyword arguments (order doesn't matter)
describe_person(age=30, city="Boston", name="Bob")

# Mixed (positional must come first)
describe_person("Charlie", city="Chicago", age=35)</code></pre>

<h5>*args and **kwargs</h5>
<pre><code># *args: Accept any number of positional arguments
def add_all(*args):
    return sum(args)

print(add_all(1, 2))        # 3
print(add_all(1, 2, 3, 4))  # 10

# **kwargs: Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC

# Combined
def example(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

example("first", 1, 2, 3, name="Alice", age=25)</code></pre>

<h5>Lambda Functions</h5>
<p>Small anonymous functions defined in one line.</p>
<pre><code># Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25

# Useful with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sort by custom key
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]</code></pre>

<h5>Docstrings</h5>
<pre><code>def calculate_area(length, width):
    \"\"\"
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area of the rectangle
    \"\"\"
    return length * width

# Access the docstring
print(calculate_area.__doc__)
help(calculate_area)</code></pre>
"""
    },
    {
        "title": "Modules & Packages",
        "slug": "python-modules-packages",
        "content": """
<h5>Modules and Packages</h5>
<p>Modules allow you to organize code and reuse functionality from Python's standard library or third-party packages.</p>

<h5>Importing Modules</h5>
<pre><code># Import entire module
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

# Import with alias
import math as m

print(m.pi)
print(m.sqrt(16))

# Import specific items
from math import pi, sqrt

print(pi)        # No need for math. prefix
print(sqrt(16))

# Import all (not recommended)
from math import *

print(pi)
print(sqrt(16))</code></pre>

<h5>Common Built-in Modules</h5>

<h6>math - Mathematical functions</h6>
<pre><code>import math

print(math.pi)           # 3.14159...
print(math.e)            # 2.71828...
print(math.sqrt(25))     # 5.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.pow(2, 3))    # 8.0
print(math.log(100, 10)) # 2.0
print(math.sin(math.pi/2)) # 1.0</code></pre>

<h6>random - Generate random numbers</h6>
<pre><code>import random

print(random.random())        # Random float 0.0 to 1.0
print(random.randint(1, 10))  # Random int from 1 to 10
print(random.uniform(1, 10))  # Random float from 1 to 10

# Random choice from list
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Shuffle a list
random.shuffle(fruits)
print(fruits)

# Random sample
print(random.sample(range(100), 5))  # 5 unique random numbers</code></pre>

<h6>datetime - Date and time</h6>
<pre><code>from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)                    # 2024-01-15 10:30:00.123456
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)               # 1990-05-15

# Date arithmetic
tomorrow = date.today() + timedelta(days=1)
print(tomorrow)

# Formatting dates
print(now.strftime("%Y-%m-%d"))      # 2024-01-15
print(now.strftime("%B %d, %Y"))     # January 15, 2024
print(now.strftime("%H:%M:%S"))      # 10:30:00

# Parsing dates
date_str = "2024-01-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed)</code></pre>

<h6>os - Operating system interface</h6>
<pre><code>import os

print(os.getcwd())           # Current working directory
print(os.listdir("."))       # List files in directory
print(os.path.exists("file.txt"))  # Check if file exists
print(os.path.join("folder", "file.txt"))  # Join paths

# os.mkdir("new_folder")     # Create directory
# os.remove("file.txt")      # Delete file
# os.rename("old.txt", "new.txt")  # Rename file</code></pre>

<h6>json - JSON encoding/decoding</h6>
<pre><code>import json

# Python dict to JSON string
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Alice", "age": 25}'

# JSON string to Python dict
json_str = '{"name": "Bob", "age": 30}'
data = json.loads(json_str)
print(data["name"])  # Bob

# Read/write JSON files
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)</code></pre>

<h5>Installing Third-Party Packages</h5>
<pre><code># Use pip to install packages
# pip install requests
# pip install numpy
# pip install pandas

import requests
response = requests.get("https://api.github.com")
print(response.status_code)</code></pre>

<h5>Creating Your Own Module</h5>
<pre><code># mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.PI)</code></pre>
"""
    },
    {
        "title": "File Handling",
        "slug": "python-file-handling",
        "content": """
<h5>File Handling in Python</h5>
<p>Python makes it easy to read from and write to files.</p>

<h5>Opening and Closing Files</h5>
<pre><code># Basic file opening
file = open("example.txt", "r")  # Open for reading
content = file.read()
file.close()  # Always close the file!

# Better way: using 'with' (auto-closes)
with open("example.txt", "r") as file:
    content = file.read()
# File is automatically closed here</code></pre>

<h5>File Modes</h5>
<pre><code># "r"  - Read (default). Error if file doesn't exist
# "w"  - Write. Creates file or overwrites existing
# "a"  - Append. Creates file or adds to end
# "x"  - Create. Error if file already exists
# "r+" - Read and write
# "b"  - Binary mode (e.g., "rb" for read binary)</code></pre>

<h5>Reading Files</h5>
<pre><code># Read entire file as string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read all lines as list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline

# Read line by line (memory efficient for large files)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read specific number of characters
with open("example.txt", "r") as file:
    chunk = file.read(10)  # Read first 10 characters
    print(chunk)</code></pre>

<h5>Writing Files</h5>
<pre><code># Write (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\\n")
    file.write("This is line 2\\n")

# Write multiple lines
lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append to existing file
with open("output.txt", "a") as file:
    file.write("This is appended\\n")</code></pre>

<h5>Working with File Paths</h5>
<pre><code>import os

# Get current directory
print(os.getcwd())

# Join paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # folder/subfolder/file.txt (or \\ on Windows)

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists!")

# Get file info
if os.path.isfile("example.txt"):
    print("It's a file")
if os.path.isdir("myfolder"):
    print("It's a directory")

# Get file size
size = os.path.getsize("example.txt")
print(f"File size: {size} bytes")</code></pre>

<h5>Working with CSV Files</h5>
<pre><code>import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # Header
    writer.writerow(["Alice", 25, "NYC"])
    writer.writerow(["Bob", 30, "LA"])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Name', 'Age', 'City'], etc.

# Using DictReader/DictWriter
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")</code></pre>

<h5>Handling File Errors</h5>
<pre><code>try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")</code></pre>

<h5>Binary Files</h5>
<pre><code># Reading binary files (images, etc.)
with open("image.png", "rb") as file:
    data = file.read()

# Writing binary files
with open("copy.png", "wb") as file:
    file.write(data)</code></pre>
"""
    },
    {
        "title": "Exception Handling",
        "slug": "python-exception-handling",
        "content": """
<h5>Exception Handling in Python</h5>
<p>Exceptions are errors that occur during program execution. Python lets you handle them gracefully.</p>

<h5>Basic try-except</h5>
<pre><code># Without error handling
# number = int("hello")  # ValueError: invalid literal

# With error handling
try:
    number = int("hello")
except ValueError:
    print("That's not a valid number!")
    number = 0

print(f"Number is: {number}")</code></pre>

<h5>Handling Multiple Exceptions</h5>
<pre><code># Multiple except blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handle multiple exceptions the same way
try:
    # some code
    pass
except (ValueError, TypeError):
    print("Value or Type error occurred")</code></pre>

<h5>The else Clause</h5>
<p>Runs if no exception occurs.</p>
<pre><code>try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {number}")
    print("No errors occurred!")</code></pre>

<h5>The finally Clause</h5>
<p>Always runs, whether exception occurs or not. Useful for cleanup.</p>
<pre><code>try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup: closing file")
    # file.close()  # This would run even if error occurred

# Better to use 'with' statement for files
with open("example.txt", "r") as file:
    content = file.read()
# File automatically closed</code></pre>

<h5>Getting Exception Information</h5>
<pre><code>try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")

# Catch any exception
try:
    # risky code
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")</code></pre>

<h5>Common Built-in Exceptions</h5>
<pre><code># ValueError - Invalid value
int("hello")

# TypeError - Wrong type
"hello" + 5

# IndexError - Index out of range
lst = [1, 2, 3]
lst[10]

# KeyError - Dictionary key not found
d = {"a": 1}
d["b"]

# FileNotFoundError - File doesn't exist
open("nonexistent.txt")

# ZeroDivisionError - Division by zero
10 / 0

# AttributeError - Attribute doesn't exist
"hello".non_existent_method()

# ImportError - Module not found
import non_existent_module</code></pre>

<h5>Raising Exceptions</h5>
<pre><code>def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems too high!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)  # Age cannot be negative!</code></pre>

<h5>Custom Exceptions</h5>
<pre><code>class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)  # Cannot withdraw $150. Balance: $100</code></pre>

<h5>Best Practices</h5>
<pre><code># Be specific with exceptions
# Bad:
try:
    # code
    pass
except:  # Catches everything, even KeyboardInterrupt
    pass

# Good:
try:
    # code
    pass
except ValueError:
    # Handle specific error
    pass

# Use EAFP (Easier to Ask Forgiveness than Permission)
# Bad (LBYL - Look Before You Leap):
if key in dictionary:
    value = dictionary[key]

# Good (EAFP):
try:
    value = dictionary[key]
except KeyError:
    value = default_value</code></pre>
"""
    },
    {
        "title": "Classes & Objects",
        "slug": "python-classes-objects",
        "content": """
<h5>Object-Oriented Programming (OOP)</h5>
<p>OOP lets you create reusable, organized code using classes and objects.</p>

<h5>Classes and Objects Basics</h5>
<pre><code># A class is a blueprint
class Dog:
    pass

# An object is an instance of a class
my_dog = Dog()
your_dog = Dog()

print(type(my_dog))  # &lt;class '__main__.Dog'&gt;</code></pre>

<h5>The __init__ Method (Constructor)</h5>
<pre><code>class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

# Creating objects with attributes
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(buddy.name)  # Buddy
print(max_dog.age) # 5</code></pre>

<h5>Instance Methods</h5>
<pre><code>class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_human_age(self):
        return self.age * 7

buddy = Dog("Buddy", 3)
buddy.bark()  # Buddy says Woof!
print(buddy.get_human_age())  # 21</code></pre>

<h5>Class Attributes vs Instance Attributes</h5>
<pre><code>class Dog:
    species = "Canis familiaris"  # Class attribute (shared)

    def __init__(self, name):
        self.name = name  # Instance attribute (unique)

buddy = Dog("Buddy")
max_dog = Dog("Max")

print(buddy.species)   # Canis familiaris
print(max_dog.species) # Canis familiaris (same)

print(buddy.name)      # Buddy
print(max_dog.name)    # Max (different)</code></pre>

<h5>Encapsulation</h5>
<pre><code>class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Convention: single _ means "private"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 100)
account.deposit(50)      # Deposited $50
account.withdraw(30)     # Withdrew $30
print(account.get_balance())  # 120</code></pre>

<h5>Inheritance</h5>
<pre><code>class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Buddy says Woof!
cat.speak()  # Whiskers says Meow!

# Check inheritance
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True</code></pre>

<h5>Using super()</h5>
<pre><code>class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.name)   # Buddy
print(buddy.breed)  # Golden Retriever</code></pre>

<h5>Special Methods (Dunder Methods)</h5>
<pre><code>class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # For print()
        return f"'{self.title}' by {self.author}"

    def __repr__(self):  # For debugging
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):  # For len()
        return self.pages

    def __eq__(self, other):  # For ==
        return self.title == other.title and self.author == other.author

book = Book("Python 101", "John Doe", 300)
print(book)       # 'Python 101' by John Doe
print(len(book))  # 300

book2 = Book("Python 101", "John Doe", 300)
print(book == book2)  # True</code></pre>

<h5>Class Methods and Static Methods</h5>
<pre><code>class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):  # Alternative constructor
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def pepperoni(cls):
        return cls(["mozzarella", "pepperoni"])

    @staticmethod
    def calculate_area(radius):  # Utility function
        return 3.14159 * radius ** 2

# Using class methods
pizza1 = Pizza.margherita()
print(pizza1.ingredients)  # ['mozzarella', 'tomatoes']

# Using static methods
area = Pizza.calculate_area(10)
print(f"Area: {area}")</code></pre>
"""
    },
]

# Delete existing tutorials in Python Basics series (except original ones we want to keep)
# Keep tutorial ID 2 (Print Tutorial) as it's the original
Tutorial.objects.filter(tutorial_series=basics_series).exclude(id=2).delete()

# Add new tutorials
from datetime import timedelta
base_time = timezone.now()

for i, tut in enumerate(tutorials):
    # Check if tutorial already exists
    if not Tutorial.objects.filter(tutorial_slug=tut["slug"]).exists():
        Tutorial.objects.create(
            tutorial_title=tut["title"],
            tutorial_slug=tut["slug"],
            tutorial_content=tut["content"],
            tutorial_series=basics_series,
            tutorial_published=base_time + timedelta(minutes=i)
        )
        print(f"Created: {tut['title']}")
    else:
        print(f"Already exists: {tut['title']}")

print("\nDone! Added all Python basics tutorials.")

# List all tutorials in Python Basics
print("\n=== Python Basics Tutorials ===")
for t in Tutorial.objects.filter(tutorial_series=basics_series).order_by('tutorial_published'):
    print(f"  - {t.tutorial_title}")
