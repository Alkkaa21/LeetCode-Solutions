l = 0
res = 0
zero_count = 0

for r in range(len(signal)):
    if signal[r] == 0:
        zero_count += 1

    while zero_count > 1:
        if signal[l] == 0:
            zero_count -= 1
        l += 1

    res = max(res, (r - l + 1) - 1)

print(res)