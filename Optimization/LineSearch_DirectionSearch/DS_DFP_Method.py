import numpy as np
from numpy.linalg import inv
from InputFunction import func, gradf, hesf
from numpy.linalg import norm as L2

def hessupd(Bi, yi, yj):
    p=yj-yi
    q=gradf(yj)-gradf(yi)
    r1=np.dot(p,q)
    r2=np.dot(q, np.dot(Bi, q))
    t1=np.outer(p, p)/r1
    t2=np.dot(np.dot(Bi, np.outer(q, q)), Bi)/r2
    return (Bi+t1-t2)
#def newton(X, mxiter=30, err=0.001, miter_LS=30,rho_LS=0.15, sigma_LS=0.30, err_LS=10**-4):
def DFP(X, mxiter=30, DIH=1, dimf=2, err=0.0001, LSf='1', LSP={}):
    valsX = [X]
    l=[]
    vals = []
    ovfs = []
    if(DIH==0):
        Bi=B0=inv(hesf(X))
    elif(DIH==1):
        Bi=B0=np.identity(dimf, dtype = float)
    Y=X
    i, j, k=0, 1, 1
    while (i < mxiter):
        i += 1
        vals.append(Y)
        ovfs.append(func(Y))
        gr=gradf(Y)
        if(L2(gr)<err):
            break;
        
        d=np.dot(Bi, gr)
        l.append(np.array([Y, -d]))
        if(LSf=='1'):
            step=0.10
        else:
            if(bool(LSP)):
                step=LSf(Y, -d, LSP)
            else:
                step=LSf(Y, -d) 
        
        temp = Y-step*d
        if (np.abs(func(temp)-func(Y))<err):
            break;
            
        if(j==dimf):
            k+=1
            j=1
            Bi=B0
            X=temp
            Y=X
            valsX.append(X)
            
        elif(j<dimf):
            Bj=hessupd(Bi, Y, temp)
            j+=1
            Bi=Bj
            Y=temp
    if(i==mxiter):
        print("Algorithm failed to converge in. Increasing 'maXiter' maXimum of iteration may give better result")        

    return (np.array(valsX), np.array(vals), np.array(ovfs), i, np.array(l))
