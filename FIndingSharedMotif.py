def long_substr(data):
    substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
    s = substrs(data[0])
    for val in data[1:]:
        s.intersection_update(substrs(val))
    return max(s, key=len)

res = long_substr(["GATTACA","TAGACCA","ATACA"])
print(res)


            