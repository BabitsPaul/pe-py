def power_set(s):
    for l in range(1, len(s)):
        for o in range(0, len(s) - l):
            yield s[o:o + l]
