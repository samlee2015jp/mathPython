def eGCD(a, b):
    if b == 0:
        return a
    else:
        return eGCD(b, a%b)

result = eGCD(25, 15)
print('The GCD is ', result)