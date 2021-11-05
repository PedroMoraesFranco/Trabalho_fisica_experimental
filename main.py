#######################################################################################################################################
##########Este código pega os dados obtidos pelo tracker e trabalha eles para nos fornecer um valor estimado da gravidade #############
#######################################################################################################################################

# Bibliotecas importadas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#########################################################################################################################################
plt.rcParams.update({'font.size':16}) # Definição de parametros de todos os plots

dados = pd.read_csv('dados2',sep=';',header=1,decimal=',',dtype=float) # Coleta de dados usando o arquivo gerado pelo tracker
tamanho = dados.shape[0] # Definindo o tamanho 
t_step=dados['t'][1] # Definindo t_step com base na lista t do arquivo
dados.head(27)
vx,x0=np.polyfit(dados['t'],dados['x'],1) # Definindo V em x e x inicial
funcx = lambda t: vx*t+x0 # Definindo a função x(t)

# Grafico de x(t)
plt.scatter(dados['t'],dados['x'],color='black') 
plt.plot(dados['t'],dados['t'].apply(funcx),color='red',linestyle='solid')
plt.ylabel('x(m)')
plt.xlabel(r't(s)')

vx.mean() # V em x médio

c1,c2,c3=np.polyfit(dados['t'],dados['y'],2) # Definindo as constantes C1, C2 e C3
funcy = lambda t: c1*t**2+c2*t+c3 # Definindo a função y(t)
# Gráfico y(t)
plt.scatter(dados['t'],dados['y'],color='black')
plt.plot(dados['t'],dados['t'].apply(funcy),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r't(s)')

g=-c1*2 # Calculando a gravidade
erro1=(9.81-g)/9.81
erro1.round(2) # Calculando o erro relativo da gravidade encontrada

p1,p2,p3=np.polyfit(dados['x'],dados['y'],2) # Definindo as constantes p1, p2 e p3
trajetoria = lambda t: p1*t**2+p2*t+p3 # Definindo a função y(x)

# Gráfico y(x)
plt.scatter(dados['x'],dados['y'],color='black')
plt.plot(dados['x'],dados['x'].apply(trajetoria),color='red',linestyle='solid')
plt.ylabel('y(m)')
plt.xlabel(r'x(m)')

# Definindo os arrays que seram preenchidos pelas velocidades
vx = np.zeros(tamanho)
vy = np.zeros(tamanho)

# Preenchendo os arrays:
# V inicial
vx[0]=(dados['x'][1]-dados['x'][0])/t_step
vy[0]=(dados['y'][1]-dados['y'][0])/t_step
# V final
vx[-1]=(dados['x'][tamanho-1]-dados['x'][tamanho-2])/t_step
vy[-1]=(dados['y'][tamanho-1]-dados['y'][tamanho-2])/t_step
# Demais 'V's
for i in range(1,tamanho-1):
    vx[i]=(dados['x'][i+1]-dados['x'][i-1])/t_step
    vy[i]=(dados['y'][i+1]-dados['y'][i-1])/t_step
    
# V em x médio
vx.mean()

# Gráfico V em x(t)
plt.scatter(dados['t'],vx, color='black')
plt.ylabel(r'$V_x$ (m/s)')
plt.xlabel(r't(s)')
plt.ylim(-8,0)
plt.plot([dados['t'].min(),dados['t'].max()],[vx.mean(),vx.mean()],color='red', linestyle='solid')


a,vy0=np.polyfit(dados['t'],vy,1) # Definindo aceleração e V em y inicial
reta= lambda x: a*x +vy0 # Definindo a função V em y(t)

# Gráfico V em y(t)
plt.scatter(dados['t'],vy,color='black')
plt.plot(dados['t'],dados['t'].apply(reta), color='red', linestyle='solid')
plt.ylabel(r'$v_y$ (m/s)')
plt.xlabel(r't(s)')


g2=-a # Gravidade obtida pela aceleração estimada
erro2 = (9.81-g2)/9.81 # Erro relativo a gravidade encontrada acima
erro2.round(2)
