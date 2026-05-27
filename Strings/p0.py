class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        # Store last occurrence of lowercase letters
        # and first occurrence of uppercase letters
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                lower_char = ch.lower()
                if lower_char not in first_upper:
                    first_upper[lower_char] = i

        count = 0

        # Check condition for each character
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1

        return count
