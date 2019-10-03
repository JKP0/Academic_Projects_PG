import numpy as np
from InputFunction import func, gradf

def upd1(al1, al, f1, f, f1d):
    temp=1+((f1-f)/((al-al1)*f1d))
    temp1=al1+(0.5*((al-al1)/temp))
    return (temp1)
def upd2(al1, al, f1d, fd):
    temp=((al-al1)*fd)/(f1d-fd)
    temp1=al+temp
    return (temp1)
def LineSearchWP(X, d, pd={}):
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
            altemp=upd1(al1, al, f1, f, f1d)
            if(abs(al-altemp)<err):
                j=mxiter
            
            al2=al
            al=altemp
            
        #condition2
        elif(fd<c2*f1d):
            altemp=upd2(al1, al, f1d, fd)
            if(abs(al-altemp)<err):
                j=mxiter
                
            al1, f1, f1d= al, f, fd
            al=altemp

        #complement of both condition1 and condition2 holds 
        else:
            return (al)
            break;
        if(j==mxiter):
            return (al)
            break;
        
        if(i==mxiter):
            print("Algorithm failed to converge in Line-Search. You may try by increasing "
                  "'mxiter' maXimum of iteration for Line search")
            return (al)
