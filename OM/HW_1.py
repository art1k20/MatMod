import numpy as np
import math 

def targetfunction(x,y): #обчислення заданої функції в точках
    return (x - 7)**2 + (y - 6)**2 + math.atan(((x-2)**2) *(y - 1)**2)

def Xgradfunction(x,y):#обчислення х-кординати градієнту в точках
    return 2*(-7 + x + ((-2 + x)*(-1 + y)**2)/(1 + ((-2 + x)**4) *(-1 + y)**4))

def Ygradfunction(x,y):#обчислення у-кординати градієнту в точках
    return 2*(-6 + (((-2 + x)**2) *(-1 + y))/(1 + (-2 + x)**4 *(-1 + y)**4) + y)

def graddescent(x_initial, y_initial, epsilon, learningrate):#функція обчислення мінімуму
    x = x_initial #початкові значення х
    y = y_initial #початкові значення у

    iteration = 0 #лічильник ітерацій

    print(f'"Номер ітерації "{iteration}" :x="{x}" y="{y} ", f(x,y)="{targetfunction(x,y)} \n')

    while (math.sqrt(Xgradfunction(x,y)**2 + Ygradfunction(x,y)**2) > epsilon): #цикл обчислення
        temp_x = x - learningrate * Xgradfunction(x,y)
        temp_y = y - learningrate * Ygradfunction(x,y)
        x = temp_x
        y = temp_y

        iteration+=1

        print(f'"Номер ітерації "{iteration}" :x="{x}" y="{y} ", f(x,y)="{targetfunction(x,y)} \n')


x_initial = 0#початкові значення х
y_initial = 0#початкові значення у
epsilon  = 0.01
learningrate = 0.01

print(graddescent(x_initial, y_initial, epsilon, learningrate))

