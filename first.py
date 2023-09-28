from matplotlib import pyplot as plt

def mkm(alfa,beta,m,n):
    bsv = []
    for _ in range(n):
        alfa = alfa * beta % m
        bsv.append(alfa/m)
    return bsv

def maclaren(beta,c,k,n):
    V = []
    for i in range(k):
        V.append(beta[i])

    mcl = []
    for i in range(n):
        s = int (c[i] * k)       
        alfa = V[s]
        mcl.append(alfa)       
        if i+k < n:            
            V[s] = beta[i+k]    
    return mcl

if __name__ == '__main__':
    alfa1 = 134168531
    c1 = 636304951
    m = 2**31
    bsv1 = mkm(alfa1,max(c1,m-c1),m,1000)
    print(bsv1[0])
    print(bsv1[14])
    alfa2 = 190406421
    c2 = 49098763
    bsv2 = mkm(alfa2,max(c2,m-c2),m,1000)
    k = 96
    mcl = maclaren(bsv1,bsv2,k,1000)
    print(mcl[0])
    print(mcl[14])
    fig, axs = plt.subplots(1, 2)
    axs[0].hist(bsv1, bins=10)
    axs[1].hist(mcl, bins=10)
    plt.show()