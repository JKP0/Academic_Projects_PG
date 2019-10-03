import numpy as np

def func(V):
    return (((V[0])**2-V[1])**2+(1-V[0])**2)
def gradf(V):
    return (np.array([4*(V[0]**3)-4*V[0]*V[1]+2*V[0]-2, -2*(V[0]**2)+2*V[1]]))
def hesf(V):
    return (np.array([[12*(V[0]**2)-4*V[1]+2, -4*V[0]], [-4*V[0], 2]]))
