alumnos = []
alumnos_ordenados = []
calf = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    alumnos.append(name)
    calf.append(score)

men = calf[0]
may = calf[0]

for i in calf:
    if i > may:
        may = i
        
for j in calf:
    if j < men:
        men = j

for k in calf:
    if k/men != 1.0 :
        if k < may:
            may = k

i = 0

for k in calf:
    if k == may:
        alumnos_ordenados.append(alumnos[i])
    i += 1

alumnos_ordenados.sort()

print( alumnos_ordenados )