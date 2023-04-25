import tkinter


class CheckButton():
    def __init__(self, master):
        self.var = tkinter.IntVar()
        self.checkButton = tkinter.Checkbutton(master=master, text='Delete', onvalue=1, offvalue=0, variable=self.var)
        self.checkButton.pack(side=tkinter.LEFT)

