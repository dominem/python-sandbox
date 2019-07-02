def data_reverse_old(data):
    chunks = [data[i:i+8] for i in range(0, len(data), 8)]
    return [bit for byte in reversed(chunks) for bit in byte]


def data_reverse(data):
    return [b for i in range(len(data)-8, -1, -8) for b in data[i:i+8]]


data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

print(data1)
print(data2)
print(data_reverse(data1))


