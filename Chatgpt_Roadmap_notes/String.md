 # Strings
      variables do not store data.
      Objects store data.
      Variables store references.
-- Python does not allow a string literal to continue onto the next line like that without tripe quotes
# Valid:
    text = """He said "I'm learning Python."""" # If both comes in a line
    msg = 'He said "Hello"'    # when want double quotes can use single out
    name = "I'm Elavarasi"     # when want single can use double quotes outside
-------------------------------------------------------------------------------------------------------------------------------
# Indexing 
     Python counts the offset (distance) from the beginning.
     +ve & -ve indexing
     -Length = Last index + 1
     -Last Index = Length - 1
# Slicing 
      Slicing never changes the original string.
      It always creates a new string.
      # Nested Slicing
            Python never does both slices at the same time.
            It works left to right.
            # Example :
               word = "Elavarasi"
               print(word[1:5][2:3])                     # Output is : v
            # Reason : first slice creates a new string -> lava
                       Now Python forgets the original string.
                       It now works on "lava"
                       New indexes are created.

+---+---+---+---+
| l | a | v | a |       -> The indexes have reset.
+---+---+---+---+
  0   1   2   3
          # Memory - So here python created 3 string objects
          # Examples :
          
                    word = "Developer"
                    print(word[::-1][3:7])
                      
                    word = "Python"
                    print(word[:4][::-1])
           # Indexing vs Slicing :
                # --- Slicing
                     word = "Python"
                     print(word[10:])     # ""
                # --- Indexing
                      word = "Python"\
                      print(word[10])      # Error

 # Rule
  
          -If the stop index is greater than the length, Python quietly adjusts it to the end of the string.
          -

# String Immutability
           - Immutable means that once a string object is created, the existing object cannot be modified.
            - However, the variable can be reassigned to a new string object.
           - Example : 
                   word = "Python"
                   old = word
                   word = word + "3"
                   print(old)
                   print(word)
# What happens in memory?

Initially:

          ┌──────────┐
word ───► │ "Python" │
          └──────────┘
              ▲
              │
old ──────────┘

Both word and old reference the same "Python" object.

Then:

word = word + "3"
Python does not modify the existing "Python" string.
It creates a new string object "Python3" and makes word reference it:

old  ─────► "Python"

word ─────► "Python3"

