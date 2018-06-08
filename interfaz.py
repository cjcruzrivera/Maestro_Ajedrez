try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


tablero = [[0,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,1,0],
           [0,0,0,0,0,0,0,0]]

gui = Tk()
gui.title('Ajedrez')
gui.geometry("680x680")

blanco = PhotoImage(file='blanco.gif')
negro = PhotoImage(file='negro.gif')
reina_b = PhotoImage(file='reina_blanca.gif')

frame = Frame(gui)

for i in range(0,8):
    for j in range(0,8):
        if (i + j)%2 == 0:
            label = Label(frame,width=80,height=80, image=blanco)
            if(tablero[i][j]==1):
                reina = Label(label,width=70,height=70, image=reina_b)           
                reina.pack()
            label.grid(row=i,column=j)
        else:
            label = Label(frame,width=80,height=80, image=negro)
            label.grid(row=i,column=j)


frame.pack()


def key(event):
    if str(event.char) == 'q' or str(event.char) == 'Q':
        gui.quit()

gui.bind("<Key>", key)



gui.mainloop()