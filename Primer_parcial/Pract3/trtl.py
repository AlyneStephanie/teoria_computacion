from turtle import Screen, Turtle
from random import randint

WIDTH, HEIGHT = 1000, 900
CURSOR_SIZE = 20

screen = None
turtle = None


def start():
    global screen
    global turtle

    pos_ini_x = -400
    pos_ini_y = 250

    screen = Screen()
    screen.setup(WIDTH, HEIGHT)

    turtle = Turtle()
    turtle.shape('arrow')
    turtle.color('black')
    turtle.speed('fastest')
    turtle.points = 0  # user defined property


    # Palabra start
    turtle.penup()
    turtle.setpos(pos_ini_x, pos_ini_y + 43)
    turtle.pendown()
    turtle.write("Start", move=False, align='left', font=('Arial', 11, 'normal'))

    # Línea y flecha
    turtle.penup()
    turtle.setpos(pos_ini_x + 50, pos_ini_y + 50)
    turtle.pendown()
    turtle.forward(50)
    turtle.dot(8, "black")

    # Círculo para Estado Ready
    turtle.penup()
    turtle.setpos(pos_ini_x + 154, pos_ini_y)
    turtle.pendown()
    turtle.circle(50)
    
    # Etiqueta para estado Ready
    turtle.penup()
    turtle.setpos(pos_ini_x + 137, pos_ini_y + 43)
    turtle.pendown()
    turtle.write("Ready", move=False, align='left', font=('Arial', 11, 'normal'))

    # Línea y flecha
    turtle.penup()
    turtle.setpos(pos_ini_x + 204, pos_ini_y + 50)
    turtle.pendown()
    turtle.forward(200)
    turtle.dot(8, "black")

    # Etiqueta para Data In
    turtle.penup()
    turtle.setpos(pos_ini_x + 280, pos_ini_y + 60)
    turtle.pendown()
    turtle.write("Data in", move=False, align='left', font=('Arial', 11, 'normal'))

    # Etiqueta para 1000000 strings
    turtle.penup()
    turtle.setpos(pos_ini_x + 250, pos_ini_y + 20)
    turtle.pendown()
    turtle.write("1_000_000 strings", move=False, align='left', font=('Arial', 11, 'normal'))

    # Etiqueta para 64 bits
    turtle.penup()
    turtle.setpos(pos_ini_x + 280, pos_ini_y)
    turtle.pendown()
    turtle.write("64 bits", move=False, align='left', font=('Arial', 11, 'normal'))

    # Círculo para Sending
    turtle.penup()
    turtle.setpos(pos_ini_x + 458, pos_ini_y)
    turtle.pendown()
    turtle.circle(50)
    
    # Etiqueta para sending
    turtle.penup()
    turtle.setpos(pos_ini_x + 434, pos_ini_y + 43)
    turtle.pendown()
    turtle.write("Sending", move=False, align='left', font=('Arial', 11, 'normal'))
    
    # Flecha circular para Timeout
    turtle.penup()
    turtle.setpos(pos_ini_x + 508, pos_ini_y + 50)
    turtle.pendown()
    turtle.circle(50, 270)
    
    # Etiqueta para Timeout
    turtle.penup()
    turtle.setpos(pos_ini_x + 558, pos_ini_y + 143)
    turtle.pendown()
    turtle.write("Timeout", move=False, align='left', font=('Arial', 11, 'normal'))

    # Etiqueta para 0.003 s
    turtle.penup()
    turtle.setpos(pos_ini_x + 558, pos_ini_y + 163)
    turtle.pendown()
    turtle.write("0.003 s", move=False, align='left', font=('Arial', 11, 'normal'))

    # Cabeza de flecha del Timeout
    turtle.penup()
    turtle.setpos(pos_ini_x + 458, pos_ini_y + 100)
    turtle.pendown()
    turtle.dot(8, "black")
    
    # Flecha curva del Acknowledgment
    turtle.penup()
    turtle.setpos(pos_ini_x + 150, pos_ini_y)
    turtle.pendown()
    turtle.dot(8, "black")
    turtle.circle(150, 180)
    
    # Etiqueta del Acknowledgement
    turtle.penup()
    turtle.setpos(pos_ini_x + 250, pos_ini_y - 175)
    turtle.pendown()
    turtle.write("Acknowledgment", move=False, align='left', font=('Arial', 11, 'normal'))

    # Cuadro del autómata de la paridad
    turtle.penup()
    turtle.setpos(pos_ini_x + 50, pos_ini_y - 195)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(750)

    turtle.penup()
    turtle.setpos(pos_ini_x + 50, pos_ini_y - 195)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(470)

    turtle.penup()
    turtle.setpos(pos_ini_x + 800, pos_ini_y - 665)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(470)

    turtle.penup()
    turtle.setpos(pos_ini_x + 800, pos_ini_y - 665)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(750)

    # Etiqueta Start del Autómata de la paridad
    turtle.penup()
    turtle.setpos(pos_ini_x + 150, pos_ini_y - 307)
    turtle.pendown()
    turtle.write("Start", move=False, align='left', font=('Arial', 11, 'normal'))

    # Flecha hacia q0
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 190, pos_ini_y - 300)
    turtle.pendown()
    turtle.forward(50)
    turtle.dot(8, "black")

    # Círculo del q0 del autómata de la paridad
    turtle.penup()
    turtle.setpos(pos_ini_x + 280, pos_ini_y - 340)
    turtle.pendown()
    turtle.circle(40)

    # Círculo interno del q0 del autómata de la paridad
    turtle.penup()
    turtle.setpos(pos_ini_x + 280, pos_ini_y - 330)
    turtle.pendown()
    turtle.circle(30)

    # Etiqueta de q0
    turtle.penup()
    turtle.setpos(pos_ini_x + 275, pos_ini_y - 307)
    turtle.pendown()
    turtle.write("q0", move=False, align='left', font=('Arial', 11, 'normal'))
    
    # Arcos de q0 a q1 
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 220)
    turtle.pendown()
    turtle.circle(-120, 60)

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 220)
    turtle.pendown()
    turtle.circle(-120, -60)

    # Arcos de q1 a q0
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 380)
    turtle.pendown()
    turtle.circle(120, 60)

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 380)
    turtle.pendown()
    turtle.circle(120, -60)

    # cabeza de flecha de q1 a q0
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 314, pos_ini_y - 320)
    turtle.pendown()
    turtle.dot(8, "black")

    # cabeza de flecha de q0 a q1
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 520, pos_ini_y - 280)
    turtle.pendown()
    turtle.dot(8, "black")


    # Círculo del estado q1
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 557, pos_ini_y - 340)
    turtle.pendown()
    turtle.circle(40)
    
    # Etiqueta del estado q1
    turtle.penup()
    turtle.setpos(pos_ini_x + 552, pos_ini_y - 307)
    turtle.pendown()
    turtle.write("q1", move=False, align='left', font=('Arial', 11, 'normal'))


    # --------------------

    
    # Círculo del q3 del autómata de la paridad
    turtle.penup()
    turtle.setpos(pos_ini_x + 280, pos_ini_y - 600)
    turtle.pendown()
    turtle.circle(40)

    # Etiqueta de q3
    turtle.penup()
    turtle.setpos(pos_ini_x + 275, pos_ini_y - 567)
    turtle.pendown()
    turtle.write("q2", move=False, align='left', font=('Arial', 11, 'normal'))
    
    # Arcos de q2 a q3 
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 480)
    turtle.pendown()
    turtle.circle(-120, 60)

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 480)
    turtle.pendown()
    turtle.circle(-120, -60)

    # Arcos de q3 a q2
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 640)
    turtle.pendown()
    turtle.circle(120, 60)

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 417, pos_ini_y - 640)
    turtle.pendown()
    turtle.circle(120, -60)

    # cabeza de flecha de q2 a q3
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 314, pos_ini_y - 580)
    turtle.pendown()
    turtle.dot(8, "black")

    # cabeza de flecha de q3 a q2
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 520, pos_ini_y - 540)
    turtle.pendown()
    turtle.dot(8, "black")


    # Círculo del estado q3
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 557, pos_ini_y - 600)
    turtle.pendown()
    turtle.circle(40)
    
    # Etiqueta del estado q3
    turtle.penup()
    turtle.setpos(pos_ini_x + 552, pos_ini_y - 567)
    turtle.pendown()
    turtle.write("q3", move=False, align='left', font=('Arial', 11, 'normal'))


    # --------------------

    # Arcos de q3 a q2 
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 595, pos_ini_y - 560)
    turtle.pendown()
    turtle.circle(130, 180)

    # Flecha de q0 hacia q2
    turtle.penup()
    turtle.setheading(270)
    turtle.setpos(pos_ini_x + 280, pos_ini_y - 340)
    turtle.pendown()
    turtle.forward(180)
    turtle.dot(8, "black")

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(pos_ini_x + 243, pos_ini_y - 300)
    turtle.pendown()
    turtle.circle(-130, -180)

    # Flecha de q1 hacia q3
    turtle.penup()
    turtle.setheading(270)
    turtle.setpos(pos_ini_x + 552, pos_ini_y - 340)
    turtle.pendown()
    turtle.dot(8, "black")
    turtle.forward(180)

    # Etiquetas 1's
    turtle.penup()
    turtle.setpos(pos_ini_x + 413, pos_ini_y - 217)
    turtle.pendown()
    turtle.write("1", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 413, pos_ini_y - 377)
    turtle.pendown()
    turtle.write("1", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 413, pos_ini_y - 477)
    turtle.pendown()
    turtle.write("1", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 413, pos_ini_y - 637)
    turtle.pendown()
    turtle.write("1", move=False, align='left', font=('Arial', 11, 'normal'))


    # Etiquetas 0's
    turtle.penup()
    turtle.setpos(pos_ini_x + 104, pos_ini_y - 433)
    turtle.pendown()
    turtle.write("0", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 270, pos_ini_y - 433)
    turtle.pendown()
    turtle.write("0", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 542, pos_ini_y - 433)
    turtle.pendown()
    turtle.write("0", move=False, align='left', font=('Arial', 11, 'normal'))

    turtle.penup()
    turtle.setpos(pos_ini_x + 713, pos_ini_y - 433)
    turtle.pendown()
    turtle.write("0", move=False, align='left', font=('Arial', 11, 'normal'))

    # ---------------------------

    turtle.penup()
    turtle.setpos(pos_ini_x + 300, pos_ini_y - 180)
    screen.mainloop()

def stop():
    print("Stopping turtle")
    screen.bye()

if __name__ == '__main__':
    start()