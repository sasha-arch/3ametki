from tkinter import BOTH, BOTTOM
from config import *
from Widgets.MainFrame import mainFrame, ctrlFrame
def main():

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(0, weight=1)
   #mainFrame.grid(column=0, row=0, sticky=N)
   #ctrlFrame.grid(column=0, row=1, sticky=S)

    mainFrame.pack(fill=BOTH)
    ctrlFrame.pack(fill=BOTH, side=BOTTOM)

    window.title('3ametki')
    window.geometry(f'{WIDTH}x{HIGHT}')
    mainFrame.create_notes()
    window.mainloop()

if __name__ == '__main__':
    main()

