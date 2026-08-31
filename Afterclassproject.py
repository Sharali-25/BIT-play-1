switch_value = 45
def show_bits(number):
    return bin(number)[2:]
print("Switch value = ",switch_value)
print("Binary form = ",show_bits(switch_value))

binary_value = show_bits(switch_value)
set_bits = binary_value.count("1")
zero_bit = binary_value.count("0")
print("set bit / ON switches = ",set_bits)
print("zero bits / OFF switches = ", zero_bit)