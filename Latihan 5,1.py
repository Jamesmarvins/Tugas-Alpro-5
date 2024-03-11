def perkalian(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + perkalian(a, b - 1)
    else:
        return -perkalian(a, -b)

print("6 x 5 =", perkalian(6, 5))
print("7 x 10 =", perkalian(7, 10))