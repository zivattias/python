def romanToInt(s: str) -> int:
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    t, p = 0, 0
    for c in reversed(s):
        if romans[c] < p:
            t -= romans[c]
        else:
            t += romans[c]
        p = romans[c]
    print("h")
    return t

print(romanToInt('MCMXCIV'))