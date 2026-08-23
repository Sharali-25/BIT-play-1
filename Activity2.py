n = int(input("Enter a number (8 or 14)"))
temp = n
pos = 0
while temp > 0:
    print(" binary:", bin(temp)[2:], " last bit:", temp & 1)
    if temp & 1:
        break
    pos = pos+ 1
    temp >>= 1
print(" first set bit in", n, "is at position", pos)