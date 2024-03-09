if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    def coord(x,y,z,n):
        m=[]
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if i+j+k != n:
                        m.append([i,j,k])
        return(m)
    print(coord(x,y,z,n))