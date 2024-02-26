a = 18
b = 20

divisor = min(a, b)

while divisor > 0:
    if a%divisor == 0 and b%divisor == 0:
        print('The GCD is ', divisor)
        break
    divisor -= 1