import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':16})

dados = pd.read_csv('dados2',sep=';',header=1,decimal=',',dtype=float)
tamanho = dados.shape[0]
t_step=dados['t'][1]
dados.head(27)
vx,x0=np.polyfit(dados['t'],dados['x'],1)
funcx = lambda t: vx*t+x0

plt.scatter(dados['t'],dados['x'],color='black')
plt.plot(dados['t'],dados['t'].apply(funcx),color='red',linestyle='solid')
plt.ylabel('x(m)')
plt.xlabel(r't(s)')
vx.mean()

c1,c2,c3=np.polyfit(dados['t'],dados['y'],2)
funcy = lambda t: c1*t**2+c2*t+c3
plt.scatter(dados['t'],dados['y'],color='black')
plt.plot(dados['t'],dados['t'].apply(funcy),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r't(s)')
g=-c1*2
erro1=(9.81-g)/9.81
erro1.round(2)

p1,p2,p3=np.polyfit(dados['x'],dados['y'],2)
trajetoria = lambda t: p1*t**2+p2*t+p3
plt.scatter(dados['x'],dados['y'],color='black')
plt.plot(dados['x'],dados['x'].apply(trajetoria),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r'x(m)')

vx = np.zeros(tamanho)
vy = np.zeros(tamanho)

vx[0]=(dados['x'][1]-dados['x'][0])/t_step
vy[0]=(dados['y'][1]-dados['y'][0])/t_step


vx[-1]=(dados['x'][tamanho-1]-dados['x'][tamanho-2])/t_step
vy[-1]=(dados['y'][tamanho-1]-dados['y'][tamanho-2])/t_step

for i in range(1,tamanho-1):
    vx[i]=(dados['x'][i+1]-dados['x'][i-1])/t_step
    vy[i]=(dados['y'][i+1]-dados['y'][i-1])/t_step

vx.mean()

plt.scatter(dados['t'],vx, color='black')
plt.ylabel(r'$V_x$ (m/s)')
plt.xlabel(r't(s)')
plt.ylim(-8,0)
plt.plot([dados['t'].min(),dados['t'].max()],[vx.mean(),vx.mean()],color='red', linestyle='solid')

a,vy0=np.polyfit(dados['t'],vy,1)
reta= lambda x: a*x +vy0

plt.scatter(dados['t'],vy,color='black')
plt.plot(dados['t'],dados['t'].apply(reta), color='red', linestyle='solid')

plt.ylabel(r'$v_y$ (m/s)')
plt.xlabel(r't(s)')

g2=-a

erro2 = (9.81-g2)/9.81
erro2.round(2)
