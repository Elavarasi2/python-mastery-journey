# What is an iterable?
    An iterable is an object that lets you access one item at a time.
# Examples :
    "Python"        # String
     [1, 2, 3]       # List
     (10, 20, 30)    # Tuple
      {"a", "b"}      # Set
      {"x":1,"y":2}   # Dictionary
      range(5)        # Range object
    
| Iterable                          | Iterator                              |
| --------------------------------- | ------------------------------------- |
| Collection of items               | Object that visits one item at a time |
| Can create an iterator            | Created from an iterable              |
| Doesn't remember current position | Remembers current position            |
| Example: list, string, tuple      | Used internally by `for`              |

# Common Mistake
Many people think for loop reads directly from the string.
Actually

for
↓
creates iterator
↓
iterator gives one item at a time
↓
loop ends
The Iterator does the work

# Python lets us create an iterator ourselves using:

# --> iter()
and get values one by one using:
# --> next()

The for loop asks the iterator, and the iterator gives the next character from the iterable.
----------------------------------------------------------------------------------------------------------------------------------    
