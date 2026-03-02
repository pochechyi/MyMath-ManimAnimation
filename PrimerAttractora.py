import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go


##################################
###  РЕШАЕМ СИСТЕМУ УРАВНЕНИЙ  ###
##################################

# Система уравнений:
def DequanLi(XYZ, t, alpha, beta, delta, epsilon, rho, xi):
    x, y, z = XYZ
    x_dt = alpha*(y - x) + delta*x*z
    y_dt = rho*x + xi*y -x*z
    z_dt = beta*z + x*y  - epsilon*x*x
    return x_dt, y_dt, z_dt

# Параметры системы и начальные условия:
alpha = 40
beta = 1.833
delta = 0.16
epsilon = 0.65
rho = 55
xi = 20

x_0, y_0, z_0 = 0.01, 0, 0

# Максимальное время и общее количество
# временных точек:
tmax, n = 50, 40000

# Интегрируем систему уравнений в каждой точке
# временного интервала t:
t = np.linspace(0, tmax, n)
f = odeint(DequanLi, (x_0, y_0, z_0), t,
           args=(alpha, beta, delta, epsilon, rho, xi))





#######################
###  ВИЗУАЛИЗИРУЕМ  ###
#######################

# Массив, отвечающий за изменение цвета:
c = np.linspace(0, 1, n)

# Готовим данные для отрисовки:
DATA = go.Scatter3d(x=x_0, y=y_0, z=z_0,
                    line=dict(color= c,
                              width=3,
                              # Выбираем цветовую палитру:
                              # Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,
                              # Reds,Blues,Picnic,Rainbow,Portland,Jet,
                              # Hot,Blackbody,Earth,Electric,Viridis,Cividis.
                              colorscale="Cividis"),
                    #  Рисуем только линии:
                    mode='lines')

fig = go.Figure(data=DATA)

# Задаем параметры отрисовки:
fig.update_layout(width=1000, height=1000,
                  margin=dict(r=10, l=10, b=10, t=10),
                  # Устанавливаем цвет фона:
                  paper_bgcolor='rgb(0,0,0)',
                  scene=dict(camera=dict(up=dict(x=0, y=0, z=1),
                                         eye=dict(x=0, y=1, z=1)),
                             # Устанавливаем пропорциональное
                             # соотношение осей друг к другу:
                             aspectratio = dict(x=1, y=1, z=1),
                             # Отображаем, как указано в "aspectratio"
                             aspectmode = 'manual',
                             # Скрываем оси:
                             xaxis=dict(visible=False),
                             yaxis=dict(visible=False),
                             zaxis=dict(visible=False)
                            )
                 )

######################
#!!  ВОСТОРГАЕМСЯ  !!#
######################

fig.show()
