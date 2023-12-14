import numpy as np
import matplotlib.pyplot as plt

def RK4(I,dt,T,a):
    Nt = int(T/dt)
    T = Nt*dt
    t = np.linspace(0,T,Nt+1)
    y = np.zeros(Nt+1)
    y[0] = I
    for n in range(0,Nt):
        k0 = -a*y[n]
        k1 = -a*(y[n] + 0.5*dt*k0)
        k2 = -a*(y[n] + 0.5*dt*k1)
        k3 = -a*(y[n] +dt*k2)

        y[n+1] = y[n] + dt*((1/6)*k0 + (1/3)*(k1+k2) + (1/6)*k3)

    return y,t

I = 1
T = 10
dt = 0.01
a = 0.5
y,t = RK4(I,dt,T,a)


plt.plot(t,y)
plt.show()