from EulersMethod import euler_method, euler_method_table_gen
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd
import numpy as np

# oxygen(kg) a person consumes per year
L = 740

# oxygen(kg) per douglas fir tree produces per year
o = 100

# human population relative growth factor
a = 0.021

# plant population relative growth factor
b = 0.039

# surface area of space colony in km^2
surface_area = 1294.99

# number of douglas-fir trees per hecta acre
tree_density = 2960

# hecta acre to km^2
ha_to_km2 = 0.01

# max number of plants
max_plants = tree_density * ha_to_km2 * surface_area

print(max_plants)

def population_dynamics(t, S):
    n, p = S
    return [a*n - ((a * (n**2)) / ( (o/L)*p) ),
            b*p - (b * (p**2)) / max_plants]

n_0 = 1000
p_0 = 1000*L/o
S_0 = [n_0, p_0]
tf = 400

pd.set_option('display.max_columns', None)

t = np.linspace(0, tf, tf+1)

eulerSol = euler_method(population_dynamics, S_0, 0, tf, 1)
n_list = []
p_list = []
for data in eulerSol[1]:
    n_list.append(data[0])
    p_list.append(data[1])

rungeKuttaSol = solve_ivp(population_dynamics, t_span=(0, max(t)), y0=S_0, t_eval=t).y

df = pd.DataFrame(euler_method_table_gen(population_dynamics, S_0, 0, tf, 1))
print(df.head())

percent_error = np.multiply(np.divide(np.subtract(rungeKuttaSol[0], n_list), rungeKuttaSol[0]), 100)
#Plotting method changes based off which figure we are graphing
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(t, percent_error, label = "Percent Difference")
plt.ylabel('% Error')
#plt.plot(t, rungeKuttaSol[0], label = "Number of Humans")
#plt.plot(t, np.multiply(p_list, 1), label = "Tree Population")
#plt.plot(t, np.multiply(rungeKuttaSol[1], (o/L)), label = "Carrying Capacity")
plt.legend()

#plt.ylabel('Number of Trees')
#plt.ylabel('Number of Humans')
plt.xlabel('Time Passed (Years)')
#plt.title("Human Population [Explicit Runge-Kutta]")
#plt.title("Human Population [Euler's Method h=1]")
#plt.title("Tree Population [Euler's Method h=1]")

plt.title("% Error of Euler's Method compared to Explicit Runge-Kutta")

#plt.show()