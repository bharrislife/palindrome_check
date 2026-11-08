"""
Chapter 2: Palindrome Check
From "Learn Python and Get a Job... Guaranteed" by Betty Harris
Interview Framework Series — Python interview question #2

Builds on Chapter 1: compare a string to its own reverse.
Run it from the command line:
    python3 palindrome_check.py
"""

import re


def is_palindrome(s):
    """Check if a string reads the same forwards and backwards. O(n) time, O(n) space."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(s):
    """
    Check with two pointers, walking inward from both ends.
    O(n) time, O(1) space — no reversed copy is built.
    """
    cleaned = s.lower().replace(" ", "")
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_phrase(phrase):
    """Ship It project: Palindrome Phrase Checker. Handles punctuation, case and spaces."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("Madam"))
    # Output: True

    print(is_palindrome("Was it a car or a cat I saw"))
    # Output: True

    print(is_palindrome_two_pointer("Madam"))
    # Output: True

    for phrase in ["A man, a plan, a canal: Panama",
                   "Was it a car or a cat I saw?",
                   "Hello world",
                   "No lemon, no melon"]:
        print("Palindrome" if is_palindrome_phrase(phrase) else "Not a palindrome",
              "-", phrase)

