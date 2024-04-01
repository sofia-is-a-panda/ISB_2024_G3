import tkinter
def dibujarBandera(canvas,x0,y0,x1,y1):
    largo=x1-x0
    canvas.create_rectangle(x0,y0,x0+largo/3,y1,fill="red")
    canvas.create_rectangle(x0+largo/3,y0,x0+2*largo/3,y1,fill="white")
    canvas.create_rectangle(x0+2*largo/3,y0,x0+largo,y1,fill="red")
canvas=tkinter.Canvas(width=400,height=400,bg="lightblue")
canvas.pack()
'''
canvas.create_rectangle(50,50,150,100,fill="blue",outline="black",width=5)
canvas.create_rectangle(150,50,250,100,fill="yellow",outline="black",width=5)
canvas.create_rectangle(50,100,150,150,fill="red",outline="black",width=5)


canvas.create_rectangle(100,50,200,200)
canvas.create_oval(100,50,200,100)

canvas.create_oval(80,80,260,260,width=1)#cara
canvas.create_oval(120,120,140,140,width=1)#ojo
canvas.create_oval(200,120,220,140,width=1)

canvas.create_text(50,70,text="Hola")

canvas.create_text(100,70,text="Pyhthon",font="Arial 40")
canvas.create_text(200,150,text="Tkinter",font="Arial 40 bold",fill="red",angle=90)
'''
dibujarBandera(canvas,100,100,400,400)
