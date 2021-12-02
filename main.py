# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#########################################################################################################################################
# Definindo funções
def funcx(t,vx,x0):
    f = vx*t+x0
    return f

def funcy(t,c1,c2,c3):
    f = c1*t**2+c2*t+c3
    return f

def trajetoria(t,p1,p2,p3):
    f = p1*t**2+p2*t+p3
    return f

def reta(t,a,vy0):
    f = a*t +vy0 
    return f
#########################################################################################################################################
plt.rcParams.update({'font.size':16}) # Definição de parametros de todos os plots
dados = np.loadtxt('dados.txt', skiprows=1) # Coleta de dados usando o arquivo gerado pelo tracker
t = dados[:,0]
x = dados[:,1]
y = dados[:,2]
tamanho = dados.shape[0] # Definindo o tamanho 
t_step=t[0] # Definindo t_step com base na lista t do arquivo
vx,x0=np.polyfit(t,x,1) # Definindo V em x e x inicial
vx.mean() # V em x médio
c1,c2,c3=np.polyfit(t,y,2) # Definindo as constantes C1, C2 e C3
p1,p2,p3=np.polyfit(x,y,2) # Definindo as constantes p1, p2 e p3
# Definindo os arrays que seram preenchidos pelas velocidades
vx1 = np.zeros(tamanho)
vy = np.zeros(tamanho)
# Preenchendo os arrays:
# V inicial
vx1[0]=(x[1]-x[0])/t_step
vy[0]=(y[1]-y[0])/t_step
# V final
vx1[-1]=(x[tamanho-1]-x[tamanho-2])/t_step
vy[-1]=(y[tamanho-1]-y[tamanho-2])/t_step
# Demais 'V's
for i in range(1,tamanho-1):
    vx1[i]=(x[i+1]-x[i-1])/(2*t_step)
    vy[i]=(y[i+1]-y[i-1])/(2*t_step) 

# V em x médio
vx1.mean()
a,vy0=np.polyfit(t,vy,1) # Definindo aceleração e V em y inicial
#########################################################################################################################################
# Grafico de x(t)
plt.scatter(t,x,color='black') 
plt.plot(t,funcx(t,vx,x0),color='red',linestyle='solid')
plt.ylabel('x(m)')
plt.xlabel(r't(s)')

# Gráfico y(t)
plt.scatter(t,y,color='black')
plt.plot(t,funcy(t,c1,c2,c3),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r't(s)')

# Gráfico y(x)
plt.scatter(x,y,color='black')
plt.plot(x,trajetoria(x,p1,p2,p3),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r'x(m)')

# Gráfico V em x(t)
plt.scatter(t,vx1, color='black')
plt.ylabel(r'$V_x$ (m/s)')
plt.xlabel(r't(s)')
plt.ylim(-10,10)
plt.plot([t.min(),t.max()],[vx1.mean(),vx1.mean()],color='red', linestyle='solid')

# Gráfico V em y(t)
plt.scatter(t,vy,color='black')
plt.plot(t,reta(t,a,vy0), color='red', linestyle='solid')
plt.ylabel(r'$v_y$ (m/s)')
plt.xlabel(r't(s)')
#########################################################################################################################################
g=-c1*2 # Calculando a gravidade
erro1=(9.81-g)/9.81
erro1.round(2) # Calculando o erro relativo da gravidade encontrada

g2=-a # Gravidade obtida pela aceleração estimada
erro2 = (9.81-g2)/9.81 # Erro relativo a gravidade encontrada acima
erro2.round(2)
print(g)
print(erro1)
print(g2)
print(erro2)