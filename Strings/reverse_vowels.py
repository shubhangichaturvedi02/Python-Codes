"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""





def reverseVowels(s: str) -> str:
        vowels = set('aeiouAEIOU')  # Use a set for faster lookups
        s = list(s)  # Convert string to a list for in-place modifications
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1

            # Move right pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string

print(reverseVowels("IceCreAm"))
