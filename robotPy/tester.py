from random import randint
from chatGPTsol import calc
from testAnswer import check_calc

n = randint(3, 1e5)
a = [0] * n
b = []
for j in range(n):
    a[j] = randint(1, 1e9)
    l = randint(0, n-2)
    r = randint(l, n-1)
    b.append((l, r))
sol = check_calc(a, b)
student_sol = calc(a, b)
if not isinstance(student_sol, list) or len(student_sol) != len(sol):
    print("Wrong Output")
if student_sol != sol:
    print("Wrong Output")
print("Correct answer")

