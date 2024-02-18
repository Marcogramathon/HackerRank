k = int(input())
R = input()
R = R.split(' ')
Rs = set(R)
c = 0

for i in Rs:
    for j in R:
        if i == j:
            c +=1
            
    if c != k:
        print(i)
        
    c = 0