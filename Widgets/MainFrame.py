import tkinter
from tkinter import RAISED, BOTH, VERTICAL, RIGHT, Y, END, LEFT

from Widgets.CheckButton import CheckButton
from bd import DbCommands
from config import *
from utils import packer


class MainFrame(tk.Frame):
    frameList = []

    def get_row(self):
        return len(self.frameList)

    def create_notes(self):
        all_notes = DbCommands.get_all_notes()
        for i in range(len(all_notes)):
            self.create_new_note_frame(all_notes[i], i)

    def create_new_note_frame(self, note, row):
        new_note_frame = tkinter.Frame(master=frame,
                                       borderwidth=5,
                                       relief=RAISED,
                                       height=9
                                       )
        new_note_frame.note = note

        new_note_label = tkinter.Label(master=new_note_frame,
                                       text=note.text[:10],
                                       )
        text_area = tkinter.Text(master=new_note_frame,
                                 height=9,
                                 width=49
                                 )
        text_area.bind('<FocusOut>', self.save_note)

        new_note_frame.checkButton = CheckButton(master=new_note_frame)
        self.frameList.append(new_note_frame)
        text_area.insert(END, note.text)
        new_note_frame.grid(row=row, column=0)
        packer(new_note_label, text_area)

    def create_note(self):
        note = DbCommands.create_note()
        self.create_new_note_frame(note, row=self.get_row())

    def save_note(self,event):
        text = event.widget.get("1.0", "end-1c")
        DbCommands.update_note(event.widget.master.note.id, text)


    def delete_notes(self):
        for note_frame in self.frameList:
            if note_frame.checkButton.var.get() == 1:
                DbCommands.delete_note(note_frame.note.id)
                self.frameList.remove(note_frame)
                note_frame.grid_forget()
        #self.create_notes()


mainFrame = MainFrame(master=window,
                    width=WIDTH,
                    height=0.95 * HIGHT,
                    background='light sky blue',
                    borderwidth=5,
                    relief=RAISED
)



canvas = tkinter.Canvas(master=mainFrame, width=WIDTH, height=0.9*HIGHT)
frame = tkinter.Frame(master=canvas)
frame.columnconfigure(0, weight=1)
scrollbar = tkinter.Scrollbar(master=mainFrame, orient=VERTICAL, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(fill=BOTH)

canvas.create_window((0, 0), window=frame, anchor='nw')

def conf(event):
    canvas.configure(scrollregion=canvas.bbox('all'))
frame.bind('<Configure>', conf)

ctrlFrame = tk.Frame(master=window,
                     width=WIDTH,
                     #height=1,
                     background='gainsboro',
                     borderwidth=5,
                     relief=RAISED
)

createNoteButton = tk.Button(master=ctrlFrame,
                             width=int(0.015 * WIDTH),
                             height=int(0.009 * WIDTH),
                             background='dark sea green',
                             borderwidth=3,
                             relief=RAISED,
                             command=mainFrame.create_note
)

deleteNoteButton = tk.Button(master=ctrlFrame,
                             width=int(0.015 * WIDTH),
                             height=int(0.009 * WIDTH),
                             background='IndianRed1',
                             borderwidth=3,
                             relief=RAISED,
                             command=mainFrame.delete_notes
)




deleteNoteButton.pack(side=LEFT, padx=10)
createNoteButton.pack(side=RIGHT, padx=10)
