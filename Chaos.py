""" This is a script that will present the client with a simple GUI where he can specify the parameter r and the boundaries of x which will be used as input into plotting the chaotic behavior. The equation for the logistic map is xn+1 = r * xn * ( 1 - xn )"""

import matplotlib.pyplot as plt

#PRESS SHIFT 2 TIMES TO SEARCH EVERYWHERE

class Chaos:

    def __init__(self,value_initial, r):
        self.r = r
        self.value = value_initial
        # self.total_value = []

    def update(self):
        self.value = self.r * self.value * (1 - self.value)

        return self.value

    def calc(self,steps):

        total_value =[]
        for i in range(steps):

            total_value.append(self.value)
            self.update()

            # print(i," ", total_value[i])
        return total_value

    def plotting_x(self,steps):

        val = self.calc(steps)
        ax = plt.axes()
        ax.plot(range(steps), val, color = 'green', linestyle = '-', linewidth = '1', marker = 'o', markersize = '5', alpha = 0.5) # or instead of color, linestyle and market use 'bo-'
        ax.set(xlabel = 'Number of Steps', ylabel = 'x', title = 'x as a function of the number of steps' )
        plt.show()

        return

    def plotting_r(self,steps):

        # r = 2.5
        # self.value =0.1

        fig, ax = plt.subplots()
        while self.r < 4:

            # self.r = r
            t = self.calc(steps)[950:]
            self.r += 0.005
            ax.plot([self.r] * len(t), t, '.', color='blue')

        plt.show()
        # print(roro, total)
        # print(roro)
        # ax = plt.axes()
        # ax.plot(roro,total) # , color = 'blue', linestyle = '-', linewidth = '1', marker = 'o', markersize = '5', alpha = 0.5) # or instead of color, linestyle and market use 'bo-'
            # ax.set(ylim =(0,0.5))
            # ax.set(xlabel = 'Number of Steps', ylabel = 'x', title = 'x as a function of the number of steps' )



        # plt.show()




######################################################
"""Client to test the class"""


if __name__ == '__main__':

    N = 1000
    x = Chaos(0.1,2.5)
    x.plotting_r(N)

    x.r = 4
    x.plotting_x(250)

    # ax = plt.axes()
    # ax.plot(roro,total) # , color = 'blue', linestyle = '-', linewidth = '1', marker = 'o', markersize = '5', alpha = 0.5) # or instead of color, linestyle and market use 'bo-'
    # ax.set(ylim =(0,0.5))
    # ax.set(xlabel = 'Number of Steps', ylabel = 'x', title = 'x as a function of the number of steps' )