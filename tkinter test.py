import tkmacosx
import tkinter


root = tkinter.Tk()
root.geometry('500x500')

button = tkmacosx.Button(root,bg='red',fg='black',text='Test',width=10)
button.pack()

root.mainloop()