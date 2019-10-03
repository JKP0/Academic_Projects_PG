import numpy as np
from numpy.linalg import inv
from InputFunction import func, gradf, hesf

#def newton(X, mxiter=30, err=0.001, miter_LS=30,rho_LS=0.15, sigma_LS=0.30, err_LS=10**-4):
def newton(X, mxiter=30, err=0.0001, LSf='1', LSP={}):
    l=[]
    vals = []
    ovfs = []
    
    i=0
    while (i < mxiter):
        i += 1
        vals.append(X)
        ovfs.append(func(X))
        d=inv(hesf(X)).dot(gradf(X))
        l.append(np.array([X, -d]))
        if(LSf=='1'):
            step=0.10
        else:
            if(bool(LSP)):
                step=LSf(X, -d, LSP)
            else:
                step=LSf(X, -d) 
        
        temp = X-step*d
        if (np.abs(func(temp)-func(X))<err):
            break;
        X=temp
    
    if(i==mxiter):
        print("Algorithm failed to converge in. You may try by increasing 'maXiter'"
              " maXimum of iteration")
    return (np.array(vals), np.array(ovfs), i, np.array(l))
