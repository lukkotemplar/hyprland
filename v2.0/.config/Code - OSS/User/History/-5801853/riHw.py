def romanToInt(s: str) -> int:
    romans = dict()
    romans['I'] = 1
    romans['V'] = 5
    romans['X'] = 10
    romans['L'] = 50
    romans['C'] = 100
    romans['D'] = 500
    romans['M'] = 1000
    i = len(s)-1
    a = 0
    while(i >= 0):
        a = a + romans[s[i]]
        if(str(romans[s[i]] - romans[s[i-1]]).startswith("4") or str(romans[s[i]] - romans[s[i-1]]).startswith("9")):
            a = a - romans[s[i-1]]
            i = i - 2
        else:
            i = i - 1
    return a

print(romanToInt("LX"))
        