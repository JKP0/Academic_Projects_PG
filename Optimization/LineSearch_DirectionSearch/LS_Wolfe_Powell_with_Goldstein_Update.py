#Modified Wolfe_Powell Algorithm.
import numpy as np
from InputFunction import func, gradf

#def MdLineSearchWP(X, d, mxiter=30, rho=0.15, sigma=0.30, err=0.0001):
def MdLineSearchWP(X, d, pd={}):
    dpd={'mxiter':30, 'rho':0.15, 'sigma':0.30, 'err':10**-4}
    if(bool(pd)):
        for key in pd.keys():
            dpd[key]=pd[key]
    
    al1, al2, al=0, np.inf, 0.5
    c1, c2=dpd['rho'], dpd['sigma']
    gf1=gradf(X)
    f1, f1d=func(X), gf1.dot(d)
    
    i, j, mxiter, err=0, 0, dpd['mxiter'], dpd['err']
    
    while(i<mxiter):
        i+=1
        f=func(X+al*d)
        g=gradf(X+al*d)
        fd=g.dot(d)
        
        #condition1
        if(f>f1+c1*al*f1d):
            al2=al
            altemp=(al1+al2)/2
            if(abs(al-altemp)<err):
                j=mxiter
            
            al=altemp
            
        #condition2
        elif(fd<c2*f1d):
            al1, f1, f1d= al, f, fd
            if(al2<np.inf):
                altemp=(al1+al2)/2
            else:
                altemp=2*al
            if(abs(al-altemp)<err):
                j=mxiter
            
            al=altemp

        #complement of both condition1 and condition2 holds 
        else:
            return (al)
            break;
        if(j==mxiter):
            return (al)
            break;
        
        if(i==mxiter):
            print("Algorithm failed to converge in LineSearch. You may try by increasing " 
                  "'mxiter' maXimum of iteration for Line search")
            return (al)
