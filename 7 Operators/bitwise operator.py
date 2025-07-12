'''Types of Bitwise Operators:
Bitwise AND (&): Returns 1 if both corresponding bits are 1, otherwise 0. 
Bitwise OR (|): Returns 1 if at least one of the corresponding bits is 1, otherwise 0. 
Bitwise XOR (^): Returns 1 if the corresponding bits are different (one is 0 and the other is 1), otherwise 0. 
Bitwise NOT (~): Inverts each bit (0 becomes 1, and 1 becomes 0). 
Left Shift (<<): Shifts bits to the left, filling the vacated positions with 0s. Effectively multiplies the number by 2 for each shift. 
Right Shift (>>): Shifts bits to the right. For unsigned integers, vacated positions are filled with 0s. For signed integers, the behavior (sign extension or zero-fill) depends on the language and the sign of the number. 
'''


a = 0b1010  # Binary representation of 10
b = 0b0110  # Binary representation of 6

print(bin(a & b))   # Output: 0b10 (Binary of 2)
print(bin(a | b))   # Output: 0b1110 (Binary of 14)
print(bin(a ^ b))   # Output: 0b1100 (Binary of 12)
print(bin(~a))     # Output: -0b1011 (Binary of -11)
print(bin(a << 1))  # Output: 0b10100 (Binary of 20)
print(bin(a >> 1))  # Output: 0b101 (Binary of 5)