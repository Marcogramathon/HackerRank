n = input()
A = input()
A = A.split(" ")
AS = set(A)
nc = int(input())
s = 0

for i in range(nc):
    op = input()
    op = op.split(" ")
    B = input()
    B = B.split(" ")
    BS = set(B)
    if op[0] == "intersection_update":
        AS.intersection_update(BS)
    elif op[0] == "symmetric_difference_update":
        AS.symmetric_difference_update(BS)
    elif op[0] == "difference_update":
        AS.difference_update(BS)
    elif op[0] == "update":
        AS.update(BS)
    print(AS)
        
for j in AS:
    s += int(j)

print(s)