from tkinter import *
from tkinter import ttk
from Chaos import *  # import Chaos does't work since it's not a package, need to use from Chaos import *

#INCOMPATIBILITY BETWEEN TKINTER AND MATPLOTLIB.plt from Chaos.py


##################### Test import of Chaos Works ###############

# N = 1000
# x = Chaos(0.1, 2.5)
# x.plotting_r(N)
# x.r = 4
# x.plotting_x(250)

###############################################################

def calculate(): #CAN:T IMPORT CHAOS SO THIS DOESNT WORK
    try:
        x = Chaos(r_selected.get(), x_selected.get())
        x.plotting_x(250)
        x.plotting_x(1000)
    except:
        pass


root = Tk()
root.title("plots of Chaos Theory for x = x * r (1 - x )")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

r_selected = DoubleVar()
x_selected = DoubleVar()

ttk.Label(mainframe, text="Select r").grid(column=1, row=1, sticky=W)
r_entry = ttk.Entry(mainframe, width=7, textvariable=r_selected)
r_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Select initial value of x").grid(column=1, row=2, sticky=W)
r_entry = ttk.Entry(mainframe, width=7, textvariable=x_selected)
r_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


# print(float(r_selected.get()))

root.mainloop()
# print(float(x_selected.get()))

#PRESS SHIFT 2 TIMES TO SEARCH EVERYWHERE
#TODO