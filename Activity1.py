print("SET A BIT - OR turns it ON")
print("5 = ", bin(5)[2:])
print("5 | 2 = ",5|2,"Binary = ", bin(5|2)[2:] )
print("ZERO A BIT - AND turns it OFF")
print("7 = ", bin(7)[2:])
print("7 & 5 = ",7&5,"Binary = ", bin(7&5)[2:] )


n = int(input("Enter a number (4or6), power of 2 , there's only one BIT that is on:"))
if n>0 and (n&(n-1)) == 0:
    print(" ", n, " binary:", bin(n)[2:],"it is power of 2")
else:
    print(" ", n," binary:", bin(n)[2:]," it is not power of 2")
