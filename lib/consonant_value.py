def solve(s):
    def value_of_substring(sub):
        return sum(ord(c) - ord('a') + 1 for c in sub)

    consonant_substrings = s.split('a')  # Split the string at vowels

    max_value = 0
    for sub in consonant_substrings:
        if sub:
            sub_value = value_of_substring(sub)
            max_value = max(max_value, sub_value)

    return max_value

print(solve("zodiacs"))
print(solve("strength"))
print(solve("Essence"))
