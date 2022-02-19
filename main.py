import math
def calculate_fun(a,b,c):
    D = b **2 - 4*a*c
    if D > 0:
        x1 = (- b + math.sqrt(D)) /2*a
        x2 = (-b - math.sqrt(D)) / 2*a
        return x1, x2
    elif D == 0:
        x = (- b) / 2 * a
        return x
    else:
        return False


a = int(input())
b = int(input())
c = int(input())

result = calculate_fun(a,b,c)
print(result)





