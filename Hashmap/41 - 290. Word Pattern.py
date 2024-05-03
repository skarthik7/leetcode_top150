def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    p_to_s = {}
    s_to_p = {}
    for char, word in zip(pattern, words):
        if (char in p_to_s and p_to_s[char] != word) or (word in s_to_p and s_to_p[word] != char):
            return False
        p_to_s[char] = word
        s_to_p[word] = char

    return True