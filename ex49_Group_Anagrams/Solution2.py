from collections import defaultdict

def groupAnagrams(strs):
    # Initialize a default dictionary to hold lists of anagrams
    anagrams = defaultdict(list)
    
    # Iterate over each string in the list
    for s in strs:
        # Sort the string and use it as the key
        sorted_str = ''.join(sorted(s))
        # Append the original string to the corresponding list in the dictionary
        anagrams[sorted_str].append(s)
    
    # Return the list of anagram groups
    return list(anagrams.values())

# Example usage:
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

strs2 = [""]
print(groupAnagrams(strs2))
# Output: [['']]

strs3 = ["a"]
print(groupAnagrams(strs3))
# Output: [['a']]