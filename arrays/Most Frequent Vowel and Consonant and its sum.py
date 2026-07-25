vowels = {'a','e','i','o','u'}
vow = {}
cons = {}

for ch in s:
    if ch in vowels:
        vow[ch] = 1 + vow.get(ch, 0)
    else:
        cons[ch] = 1 + cons.get(ch, 0)

vowcount = max(vow.values()) if vow else 0
conscount = max(cons.values()) if cons else 0

print(vowcount + conscount)