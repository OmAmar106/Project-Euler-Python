
for i in range(1,500):
    for j in range(1,500):
        if int(((i*i)+(j*j))**0.5)==((i*i)+(j*j))**0.5 and i+j+int(((i*i)+(j*j))**0.5)==1000 and i!=j and i!=(int(((i*i)+(j*j))**0.5)) and j!=int(((i*i)+(j*j))**0.5):
            # print(i,j,int(((i*i)+(j*j))**0.5))
            print(i*j*int((i*i+j*j)**0.5))

