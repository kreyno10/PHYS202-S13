from numpy import *

def dipolePotential(x,y,q,d):
    """this returns the potntial due to two points"""
    k = 8.9e9
    V = (k*q/ (x**2 + (y - d)**2)**(1/2.)) - (k*q/ (x**2 + (y + d)**2)**(1/2.))
    return V

def pointPotential(x,y,q,posx,posy):
    """this returns the potential of this point"""
    k = 8.9e9
    V = (k*q/(x**2 + (y - (posx**2 + posy**2)**(1/2.))**2))
    return V

def pointField(x,y,q,Xq,Yq):
    """this returns the electric field components Ex,Ey"""
    k = 8.99 *10**9
    Ex(x,y) = k*q*(x - Xq) / sqrt((x-Xq)**2 + (y - Yq)**2)
    Ey(x,y) = k*q*(y-Yq) / sqrt((x-Xq)**2 + (y - Yq)**2)
    E = [Ex,Ey]
    return E
