import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator


#Считываем данные из файлов и преобразуем их для построения графика
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data.txt", dtype = int)
data_array = tmp[1] * data_array
time_array = np.arange(len(data_array))
time_array = [float(i) for i in time_array]
time_array = np.array(time_array, dtype = float)
time_array *= tmp[0]

#Считаем время разряда и заряда конденсатора
a = tmp[0] * np.argmax(data_array)
b = len(data_array)*tmp[0] - a
a = f'{a:.2f}'
b = f'{b:.2f}'
charge_time = 'Время заряда: ' + a
discharge_time = 'Время разряда: ' + b


#Настраиваем внешний вид графика
fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time_array, data_array, color='#DC143C', linestyle='-', linewidth=1, markevery = 10, marker='s', markersize=3, label = 'V(t)')
ax.set_xlim(0, 13)
ax.set_ylim(0, 3.3)
ax.set_xlabel('Время, с', fontsize = 16)
ax.set_ylabel('Напряжение, В', fontsize = 16)
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепи', fontsize = 20, loc = 'center', pad = 15.0)
ax.legend(loc = 'upper right')
ax.grid(visible=1, which='major', axis='both', linestyle = '-', linewidth = 2, color = '#C0C0C0')
ax.grid(visible=1, which='minor', axis='both', linestyle = '--', color = '#D3D3D3')
ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(0.500))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.text(9.05, 2.55, charge_time, fontsize = 12, color = '#252525')
ax.text(9.05, 2.05, discharge_time, fontsize = 12, color='#252525')


#Сохраняем график в svg формате
plt.savefig("graph.svg")

