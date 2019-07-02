def longest_consec(strarr, k):
    strings = [''.join(strarr[i:i+k]) for i in range(0, len(strarr) - k + 1)]
    return '' if k <= 0 else max(strings or [''], key=len)


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(longest_consec([], 3))
