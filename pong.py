import turtle

#creamos la ventana donde va ser el juego
wn = turtle.Screen()
wn.delay(100)
wn.title("Pong by Luciana")
wn.bgcolor("black")#el color que queramos
wn.setup(width=800, height=600)#tamaño de la ventana7
wn.tracer(0)#para que no se recargue la pantalla

#Score
score_a = 0
score_b = 0

# Paleta A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")#por default viene 20px x 20px por lo que abajo lo agrandamos
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")#por default viene 20px x 20px por lo que abajo lo agrandamos
paddle_b.color("lightblue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")#por default viene 20px x 20px 
ball.color("lightgreen")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4 #cada vez que la pelota se mueve, se mueve cada 2 px (hay que poner ese numero segun la velocidad q lo mueva tu compu)
ball.dy = -0.4 #cada vez que la pelota se mueve, se mueve cada 2 px (hay que poner ese numero segun la velocidad q lo mueva tu compu)


# Pen. Va a marcar los puntos de los jugadores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #no lo queremos ver, solo lo que va a escribir
pen.goto(0,260) #chequear el tamaño que le dimos a la ventana y decidir donde lo queremos
pen.write("Jugador A: 0   Jugador B: 0", align="center", font=("Courier", 24, "normal")) #default score


#Funciones para mover las paletas con el teclado arriba y abajo
def paddle_a_up():
    y = paddle_a.ycor() # el metodod ycor() nos devuelve la coordenada y donde se encuentra la paleta
    y += 20 #para arriba el valor de y aumenta y para abajo decrece
    paddle_a.sety(y)  #le decimos a la paleta que su nuevo valor es la segunda y

def paddle_a_down():
    y = paddle_a.ycor() # el metodod ycor() nos devuelve la coordenada y donde se encuentra la paleta
    y -= 20 #para arriba el valor de y aumenta y para abajo decrece
    paddle_a.sety(y)  #le decimos a la paleta que su nuevo valor es la segunda y

def paddle_b_up():
    y = paddle_b.ycor() # el metodod ycor() nos devuelve la coordenada y donde se encuentra la paleta
    y += 20 #para arriba el valor de y aumenta y para abajo decrece
    paddle_b.sety(y)  #le decimos a la paleta que su nuevo valor es la segunda y

def paddle_b_down():
    y = paddle_b.ycor() # el metodod ycor() nos devuelve la coordenada y donde se encuentra la paleta
    y -= 20 #para arriba el valor de y aumenta y para abajo decrece
    paddle_b.sety(y)  #le decimos a la paleta que su nuevo valor es la segunda y

#union con el teclado
wn.listen() #este metodo es para que la venata "escuche" cuando estan tocando el teclado
wn.onkeypress(paddle_a_up, "w") #cuando el usuario presiones w, llama a la funcion paddle_a_up() y sube
wn.onkeypress(paddle_a_down, "s") #cuando el usuario presiones s, llama a la funcion paddle_a_down() y baja
wn.onkeypress(paddle_b_up, "Up") #cuando el usuario presione fecha arriba, llama a la funcion paddle_b_up() y sube
wn.onkeypress(paddle_b_down, "Down") #cuando el usuario presiones flecha abajo, llama a la funcion paddle_b_down() y baja


# Main game loop (para que la pantalla quede abierta todo el tiempo)
while True:
    wn.update()
    #Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Limites de Bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)#para que pierda
        ball.dx *= -1
        score_a +=1 #aumenta en uno el score si sale del limite de 390
        pen.clear() #para que no se printee encima suyo todo el tiempo
        pen.write(f"Jugador A:{score_a}   Jugador B: {score_b}", align="center", font=("Courier", 24, "normal")) #default score
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 #aumenta en uno el score si sale del limite de 390
        pen.clear() #para que no se printee encima suyo todo el tiempo
        pen.write(f"Jugador A:{score_a}   Jugador B: {score_b}", align="center", font=("Courier", 24, "normal")) #default score

    # colision entre paleta y pelota
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): #mide el tamañod e la paleta y ubicacion
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): #mide el tamañod e la paleta y ubicacion
        ball.setx(-340)
        ball.dx *= -1