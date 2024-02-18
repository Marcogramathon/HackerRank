n = int(input())
arr = map(int, input().split())
elem = list(arr)
men=elem[0]
may = elem[0]
for i in elem:
    if i > may:
        may = i
# print (may)
for j in elem:
    if j < men:
        men = j

for k in elem:
    if k/may != 1.0 :
        if k > men:
            men = k

print(men)
