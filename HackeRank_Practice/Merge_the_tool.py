# # Merge the Tools

# ## Problem

# Divide the string into equal-sized substrings and remove duplicate characters from each substring while preserving the order of their first occurrence.

# ## Concepts Used

# - String slicing
# - range()
# - for loop
# - Dictionary
# - dict.fromkeys()
# - join()

# ## What I Learned

# - Break a difficult problem into smaller problems.
# - Solve the simpler version first.
# - Build the algorithm before writing Python code.
# - Read the problem statement carefully. I initially misunderstood the meaning of `k` and corrected it after testing.

# -------------------------------------------------- SOLUTION ---------------------------------------------
def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    # s = l // k --------------- the line i misunderstood and then commented
    for i in range(0,l,k):
        store = string[i:i+k]
        print("".join(dict.fromkeys(store)))
    

    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

