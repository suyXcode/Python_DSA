# You want Group Anagrams without using inbuilt functions (like sorted()), as shown in the image.

# We’ll do it the correct interview way using Hash Map (dict) + character frequency.

# 🔹 Problem Recap (from image)

# Input

# ["eat", "tea", "tan", "ate", "nat", "bat"]


# Output (any order)

# [["bat"], ["nat", "tan"], ["eat", "tea", "ate"]]




def groupAnagrams(words):
    mp = {}   # hash map

    for word in words:
        # Step 1: count characters manually
        count = [0] * 26   # for a–z

        for ch in word:
            index = ord(ch) - ord('a')
            count[index] += 1

        # Step 2: convert list to tuple (hashable)
        key = tuple(count)

        # Step 3: group words
        if key not in mp:
            mp[key] = []
        mp[key].append(word)

    # Step 4: collect result
    result = []
    for val in mp.values():
        result.append(val)

    return result
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]
))
