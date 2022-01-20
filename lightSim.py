import turtle
from math import *
import time


while True:
    Turtles=[]
    Turtles_pos=[]
    Turtles_plus=[]
    Turtles_fin=[]

    event=0
    restart=0

    turt_num=100

    turts_x=0
    turts_y=0

    land_u=6#m/s
    sea_u=2#m/s


    #register stuff
    turtle.register_shape("lifeguard.gif")
    turtle.register_shape("gorgona.gif")


    #Screen Setup
    wn = turtle.Screen()
    wn.setup(width=1000,height=600)
    wn.bgpic("Beach-Background.gif")
    wn.listen()
    turtle.tracer(0,0)


    #questions
    turt_answer=wn.numinput("Light_Simulation","Enter lifeguard generation number",default=100,minval=1,maxval=1000)
    while turt_answer is None:
        turt_answer=wn.numinput("Light_Simulation","Enter lifeguard generation number",default=100,minval=1,maxval=1000)
    turt_num = int(turt_answer)

    sea_answer=wn.numinput("Light_Simulation","Enter number for sea velocity",default=2,minval=1,maxval=300) 
    while sea_answer is None:
        sea_answer=wn.numinput("Light_Simulation","Enter number for sea velocity",default=2,minval=1,maxval=300)
    sea_u = int(sea_answer)

    land_answer=wn.numinput("Light_Simulation","Enter number for land velocity",default=6,minval=1,maxval=300)
    while land_answer is None:
        land_answer=wn.numinput("Light_Simulation","Enter number for land velocity",default=6,minval=1,maxval=300)
    land_u = int(land_answer)
    
    wn.listen()
    #pen
    pen=turtle.Pen()
    pen.width(2)
    pen.up()
    pen.goto(-600,0)
    pen.down()
    pen.forward(1200)
    pen.up()
    pen.goto(0,200)
    pen.hideturtle()
    pen.write("Drag and drop the characters and then press {w} 2 times", align="center", font=("Arial",20,"normal"))


    #1st lifeguard
    lfg=turtle.Pen()
    lfg.shape("lifeguard.gif")
    lfg.up()

    turtle.update()

    def drag_handler(x, y):
        lfg.ondrag(None)
        #if y>0:
        lfg.goto(x, y)
        lfg.ondrag(drag_handler)
        
    def click_handler():
        global event
        event=event+1
        return event
    
    def click_handler2():
        global restart
        restart=restart+1
        return event
        
    while True:
        lfg.ondrag(drag_handler)
        turtle.update()
        wn.onkeypress(click_handler,"w")
        if event == 2 and abs(lfg.xcor())+abs(lfg.ycor())==0:
            event=0
        if event == 2:
            event=0
            break

    turts_x=lfg.xcor()
    turts_y=lfg.ycor()


    #endpoint
    endx=400
    endy=-256
    endp=turtle.Turtle()
    #endp.shape("circle")
    #endp.shapesize(0.08,0.08,0.08)
    endp.shape("gorgona.gif")
    endp.up()


    def drag_handler(x, y):
        endp.ondrag(None)
        if y<0:
            endp.goto(x, y)
        endp.ondrag(drag_handler)
        
    def click_handler():
        global event
        event=event+1
        return event
        
    while True:
        endp.ondrag(drag_handler)
        turtle.update()
        wn.onkeypress(click_handler,"w")
        if event == 2 :
            event=0
            break

    endx=endp.xcor()
    endy=endp.ycor()
    lfg.hideturtle()

    pen.undo()

    #max_angle_calculation
    junct=abs(turts_x - endx)#katw plevra toy trigwnou
    ypot=sqrt(junct**2+turts_y**2)#vriskei thn ypoteinoysa me pythagorio
    gwnia=degrees(asin(junct/ypot))#vriskei thn gwnia apenanti apo thn plevra junction
    swst_gwn=abs(gwnia-90)


    for i in range(turt_num):#ftiaxnei xelwnes
        name=str("turt"+str(i+1))
        name=turtle.Pen()
        name.shape("lifeguard.gif")
        name.up()
        name.goto(turts_x,turts_y)
        name.down()
        Turtles.append(name)
        Turtles_pos.append(0)

    for i in Turtles:#dinei thn swsth kai diaforetikh gwnia se kathe xelwna
        if turts_x<endx:
            i.right((Turtles.index(i))*(gwnia/turt_num)+swst_gwn)
        else:
            i.left((Turtles.index(i))*(gwnia/turt_num)+swst_gwn-180)


    while event==0:
        for t in Turtles:#kinhsh sto prwto yliko
            flag=0
            for o in range(int(land_u)):
                if t.ycor()<=0 and flag == 0:
                    Turtles.remove(t)
                    Turtles_plus.append(t)
                    t.left(t.towards(endx,endy) - t.heading())
                    flag=1
                elif flag == 0:
                    t.forward(1)
                    Turtles_pos[Turtles.index(t)]=(Turtles_pos[Turtles.index(t)]+1)
                
        for tp in Turtles_plus:#kinhsh sto deytero yliko
            flag=0
            for o in range(int(sea_u)):
                if tp.ycor()<=endy and flag == 0:
                    Turtles_plus.remove(tp)
                    Turtles_fin.append(tp)
                    flag=1
                    
                elif flag == 0:
                    tp.forward(1)
                    Turtles_pos[Turtles_plus.index(tp)]=(Turtles_pos[Turtles_plus.index(tp)]+1)

        if len(Turtles_fin)==(turt_num):
            event=1
        turtle.update()

    for e in Turtles_fin:#afhnei mono thn grhgoroterh diadromh 
        if Turtles_fin.index(e)<=0:
            print(e)
        else:
            for i in range(10000):
                e.undo()
            e.hideturtle()
            turtle.update()
            time.sleep(1/(turt_num*2))

    pen.write("This is the quickest Route", align="center", font=("Arial",20,"normal"))
    turtle.update()
    pen.goto(0,-200)
    pen.write("To Restart Press {r}", align="center", font=("Arial",20,"normal"))
    while True:
        turtle.update()
        wn.onkeypress(click_handler2,"r")
        if restart >= 1:
            break
    turtle. clearscreen()
    turtle.update()
