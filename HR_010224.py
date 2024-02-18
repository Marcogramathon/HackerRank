n_e = input()
list_eng = input()
n_f = input()
list_fr= input()
c = ''
k = ''
l_e = []
l_f = []

for i in list_eng:
    if  i == ' ':
        l_e.append(c)
        c = ''
    else:
        c = c + i
        
l_e.append(c)


for i in list_fr:
    if  i == ' ':
        l_f.append(k)
        k = ''
    else:
        k = k + i

l_f.append(k)

n = len(l_e)

for j in l_e:
    if j in l_f:
        n = n - 1
        
print(n)