s = input("Enter a string: ")

ans = ""
seen = set()

for ch in s:
    if ch not in seen:
        seen.add(ch)
        ans += ch

print(ans)