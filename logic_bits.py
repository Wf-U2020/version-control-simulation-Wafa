# Logical Operators Example

print("Logical Operators Demo")

bool1 = input("Enter first boolean value (True/False): ") == "True"
bool2 = input("Enter second boolean value (True/False): ") == "True"

print("\nResults:")
print("bool1 and bool2 =", bool1 and bool2)
print("bool1 or bool2  =", bool1 or bool2)
print("not bool1       =", not bool1)
print("not bool2       =", not bool2)
# Bitwise Operators Example

print("\nBitwise Operators Demo")

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("a =", a, "=", bin(a))
print("b =", b, "=", bin(b))

print("\na & b =", a & b, "=", bin(a & b))
print("a | b =", a | b, "=", bin(a | b))
print("a ^ b =", a ^ b, "=", bin(a ^ b))
print("~a    =", ~a, "=", bin(~a))
print("a << 1 =", a << 1, "=", bin(a << 1))
print("a >> 1 =", a >> 1, "=", bin(a >> 1))
