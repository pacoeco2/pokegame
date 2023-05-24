import tkinter as tk
import random as rd
from PIL import Image, ImageTk
import tkinter.font as tF  
#import pygame as pg
import time

juego = tk.Tk()
juego.title("Pokemón")
juego.geometry("500x500")

#Asigna un total de vida, atque y defensa
class pokemon:
    def __init__(self, HP, defensa, ataque):
        self.HP = HP
        self.defensa = defensa
        self.ataque = ataque

MOP = tk.Label()
MOD = tk.Label()
CRT = tk.Label()

#Probabilidad de hacer golpe crítico
def Crítico(CRT, text, delay):
       for i in range(len(text)):
        CRT.config(text = CRT.cget("text")+text[i])
        CRT.update()
        time.sleep(delay)
        CRT.after(1250, lambda: CRT.config(text = ''))

#Imprime el texto lentamente cuando seleccionas un movimiento
def Label_por_letra(MOP, text, delay): #Label en donde se escribe, texto a escribir, tiempo que tarda entre letra y letra
    for i in range(len(text)): #Usamos un for para recorrer el texto
        MOP.config(text=MOD.cget("text") + text[i]) #cget obtiene el texto actual que se declaró al mandar a llamar la función, y lo va imprimiendo conforme lo recorre
        MOP.update() #Va imprimiendo las letras sin quedarse en espera hasta que pase el tiempo total, como en los pokemon 
        time.sleep(delay) #Tiempo que se va a "dormir" entre letra y letra
        MOP.after(3500, lambda: MOP.config(text='')) #after ejecuta un comando sobre que hacer una vez que se ha hecho lo que que hizo con el label, primero el tiempo que va a tardar, después el comando; lambda actúa como una función, solo que declarada en la misma línea de código, siempre y cuando sean simples y cortas, aunque se puede declarar una función aparte y mandarla a llamar 

#Función que puede ser mandada a llamar en lugar del lambda        
#def after():
     #MOP.config(text='')

def Label_por_letra(MOD, text, delay):
    for i in range(len(text)):
        MOD.config(text=MOD.cget("text") + text[i]) 
        MOD.update()
        time.sleep(delay)
        MOD.after(3500, lambda: MOD.config(text = ''))

#Música de fondo (usa Pygame), comentado hasta que nos den luz verda para usar Pygame
#ruta_musica = "C:\Códigos\Python\PokePro\Mega Man Zero - Crash (Boss Battle) [8BIT].wav"
#pg.mixer.init()
#pg.mixer.music.load(ruta_musica) #Carga la música desde la ruta, puede ser declarada ahí mismo o declararla en una variable y usarla en la función
#pg.mixer.music.play(-1) #Declara el número de veces a repetir la música, -1 significa indefinido, entra en loop cada vez que termine la conción


diglett=pokemon(120,30,40)
pikachu=pokemon(150,40,60)

#Movimientos que Diglett puede hacer
def GolpeRoca():
        Crt = rd.randint(1,10) #Valor que define si sale crítico o no
        if(Crt == 2 or Crt == 5):
         Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.1) #Label en donde se escribe, texto a escribir, tiempo de escritura que manda a "dormir" la consola entre letra y letra
         Crítico(CRT, "¡Golpe Crítico!", 0.05) #Lo mismo que el anterior
         pikachu.HP = pikachu.HP - 24
         PikHP2.configure(text=pikachu.HP)
        else:
         pikachu.HP = pikachu.HP - 12
         Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.1)
         PikHP2.configure(text=pikachu.HP) 
        

def Cuchillada():
        Crt = rd.randint(1,10)
        if(Crt == 2 or Crt == 5):
         pikachu.HP = pikachu.HP - 18
         Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.1)
         Crítico(CRT, "¡Golpe Crítico!", 0.05)
         PikHP2.configure(text=pikachu.HP)
        else:
         pikachu.HP = pikachu.HP - 9
         Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.1)
         PikHP2.configure(text=pikachu.HP)
        


def Fisura():
        Crt = rd.randint(1,10)
        if(Crt == 2 or Crt == 5):
         Label_por_letra(MOD, "Diglett ha usado Fisura", 0.1)
         Crítico(CRT, "¡Golpe Crítico!", 0.05)
         pikachu.HP = pikachu.HP - 28
         PikHP2.configure(text=pikachu.HP)
        else:
         Label_por_letra(MOD, "Diglett ha usado Fisura", 0.1)
         pikachu.HP = pikachu.HP - 14
         PikHP2.configure(text=pikachu.HP)
        


def Terremoto():
        Crt = rd.randint(1,10)
        if(Crt == 2, Crt == 5):
         Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.1)
         Crítico(CRT, "¡Golpe Crítico!", 0.05)
         pikachu.HP = pikachu.HP - 38
         PikHP2.configure(text=pikachu.HP)
        else:
              Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.1)
              pikachu.HP = pikachu.HP - 19
              PikHP2.configure(text=pikachu.HP)
      
#Imagen de Diglett
Diglett = Image.open('C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/SeekPng.com_diglett-png_2282423-removebg-preview.png')
Diglett = Diglett.resize((120,120))
DiglettTk = ImageTk.PhotoImage(Diglett)

DiglettLbl = tk.Label(juego, image=DiglettTk)
DiglettLbl.place(x=300, y = 10)

#Fuente de texto
Digfont = tF.Font(family = "Helvetica", size = 12)

#Vida de Diglett impresa en la interfaz
DigHP = tk.Label(juego, text = ' ', font = Digfont)
DigHP.place(x = 110, y = 50)
Barra = tk.Label(juego, text = "/")
Barra.place(x = 150, y =50)
DigHP2 = tk.Label(juego, text = diglett.HP, font = Digfont)
DigHP2.place(x = 170, y = 50)

DigLbl = tk.Label(juego, text = "Diglett Nvl 30", font=Digfont)
DigLbl.place(x = 110, y = 20)

#Caja clásica de Pokemón

Caja = Image.open('C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/DS DSi - Pokemon Platinum - Text Box Styles.png')
Caja = Caja.resize((500,100))
CajaTk = ImageTk.PhotoImage(Caja)

CajaLbl = tk.Label(juego, image=CajaTk)
CajaLbl.place(x = 0, y=400)

#Imagen de Pikachu
Pikachu = Image.open('C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/imgbin_pikachu-sprite-pokémon-png.png')
Pikachu = Pikachu.resize((300,250))
PikachuTk = ImageTk.PhotoImage(Pikachu)
PikachuLbl = tk.Label(juego, image=PikachuTk)
PikachuLbl.place(x=0, y = 150)

#Vida de Pikachu
Digfont = tF.Font(family = "Helvetica", size = 12)
PikHP = tk.Label(juego, text = pikachu.HP, font = Digfont)
PikHP.place(x = 320, y = 250)
Barra = tk.Label(juego, text = "/")
Barra.place(x = 310, y =250)
PikHP2 = tk.Label(juego, text = ' ', font = Digfont)
PikHP2.place(x = 265, y = 250)

#Labels en donde se escriben los movimientos de Pikachu, Diglett y si sale crítico
MOP = tk.Label(juego, text = '', font = Digfont)
MOP.place(x = 250, y = 350)

MOD = tk.Label(juego, text = '', font = Digfont)
MOD.place(x = 250, y = 370)

CRT = tk.Label(juego, text = '', font = Digfont)
CRT.place(x = 250, y = 300)


PikLbl = tk.Label(juego, text = "Pikachu Nvl 30", font=Digfont)
PikLbl.place(x = 280, y = 210)
PikHPL = tk.Label(juego, text = "PS: ", font = Digfont)
PikHPL.place(x = 225, y = 250)
DigHPL = tk.Label(juego, text = "PS: ", font = Digfont)
DigHPL.place(x = 75, y = 50)

#Movimientos de Pikachu
def Arañazo():
        Crt = rd.randint(1,10)
        if(Crt == 2 or Crt ==5):    
         Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.1)
         Crítico(CRT, "¡Golpe Crítico!", 0.05)
         diglett.HP = diglett.HP - 18 #Daño crítico
         DigHP.configure(text = diglett.HP) #Actualiza la vida
        else:
             Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.1)
             diglett.HP = diglett.HP - 9 #Daño normal
             DigHP.configure(text = diglett.HP)
             
        Defi = rd.randint(1, 4) #Valor que define que movimiento va a usar Diglett en el sig. turno

        if(Defi == 1):
               GolpeRoca()

        elif (Defi == 2):
               Cuchillada()

        elif (Defi == 3):
               Fisura()

        elif (Defi == 4):
               Terremoto()

        if(pikachu.HP<=0):
               print("Pikachu ha sido derrotado")

def Impactrueno():
        Crt = rd.randint(1,10)
        if(Crt == 2 or Crt == 5):
             Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.1)
             Crítico(CRT, "¡Golpe Crítico", 0.05)
             diglett.HP = diglett.HP - 3
             DigHP.configure(text = diglett.HP)
        else:
         Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.1)
         diglett.HP = diglett.HP - 6
         DigHP.configure(text = diglett.HP)
        
        Defi = rd.randint(1, 4)

        if(Defi == 1):
               GolpeRoca()

        elif (Defi == 2):
               Cuchillada()

        elif (Defi == 3):
               Fisura()

        elif (Defi == 4):
               Terremoto()

        if(pikachu.HP<=0):
               print("Pikachu ha sido derrotado")

def ColaHierro():
        Crt = rd.randint(1,10)
        if(Crt == 2 or Crt == 5):
             Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.1)
             Crítico(CRT, "¡Golpe Crítico!", 0.05)
             diglett.HP = diglett.HP - 20
             DigHP.configure(text = diglett.HP)
        else:
         Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.1)
         diglett.HP = diglett.HP - 10
         DigHP.configure(text = diglett.HP)
         
       
        Defi = rd.randint(1, 4)

        if(Defi == 1):
               GolpeRoca()

        elif (Defi == 2):
               Cuchillada()

        elif (Defi == 3):
               Fisura()

        elif (Defi == 4):
               Terremoto()

        if(pikachu.HP<=0):
               print("Pikachu ha sido derrotado")

def Electrobola():
        Crt = rd.randint(1,5)
        if(Crt == 2 or Crt==5):
         Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.1)
         Crítico(CRT, "¡Golpe Crítico!", 0.1)
         diglett.HP = diglett.HP - 8
         DigHP.configure(text = diglett.HP)
        else:
              Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.1)
              diglett.HP = diglett.HP - 4
              DigHP.configure(text = diglett.HP)
              
        Defi = rd.randint(1, 4)
        
        if(Defi == 1):
               GolpeRoca()

        elif (Defi == 2):
               Cuchillada()

        elif (Defi == 3):
               Fisura()

        elif (Defi == 4):
               Terremoto()

        if(pikachu.HP<=0):
               print("Pikachu ha sido derrotado")

#Contadores de movimientos y usos máximos 
TPA = 25
TPI = 18
TPC = 15
TPE = 15
click_contA = 0
click_contI = 0
click_contC = 0
click_contE = 0
clicks_maxA  = 25
clicks_maxI = 18
clicks_maxC = 15
clicks_maxE = 15               

#Contabiliza los movimientos que ha hecho Pikachu, desabilita el botón si lo ha usado un máximo de veces
def click_max1():
 global click_contA #Al declarar global antes de una variable, quiero decir que quiero modificar la variable con mismo nombre en lugar de declararla solo como si fuera global, aunque de todas formas tengo que declarala antes de la función, le asigné 0 porque si la dejo así no funciona
 global TPA
 click_contA += 1 #Contador de clicks
 TPA = TPA - 1 #Valor que imprime cuantas veces faltan antes de que se quede sin movimientos
 contador.config(text="TP: "+str(TPA))
 if click_contA >= clicks_maxA:
      boton_aranazo.config(state = tk.DISABLED) #Deshabilita el botón definitivamente al alcanzar el mínimo de TP
 

def click_max2():
 global click_contI
 global TPI
 click_contI += 1
 TPI = TPI - 1 
 contador2.config(text="TP: "+str(TPI))
 if click_contI >= clicks_maxI:
      boton_Impactrueno.config(state = tk.DISABLED)

def click_max3():
 global click_contC
 global TPC
 click_contC += 1
 TPC = TPC - 1
 contador3.config(text="TP: "+str(TPC))
 if click_contC >= clicks_maxC:
      boton_ColaHierro.config(state = tk.DISABLED)

def click_max4():
 global click_contE
 global TPE
 click_contE += 1
 TPE = TPE - 1
 contador4.config(text="TP: "+str(TPE))
 if click_contE >= clicks_maxE:
      boton_Electrobola.config(state = tk.DISABLED)

#Comando de comandos, solo se puede asignar un comando a la vez por botón, así que estas funciones ejecutan todos los comandos que deberían ejecutarse al presionar un botón
def Cuadruple_ComandoA():
     hide()
     Arañazo()
     click_max1()
     show()

def Cuadruple_ComandoI():
     hide()
     Impactrueno()
     click_max2()
     show()

def Cuadruple_ComandoC():
     hide()
     ColaHierro()
     click_max3()
     show()

def Cuadruple_ComandoE():
     hide()
     Electrobola()
     click_max4()
     show()

#Deshabilita todos los botones durante un movimiento
def hide():
     boton_aranazo.configure(state="disabled")
     boton_ColaHierro.configure(state="disabled")
     boton_Electrobola.configure(state="disabled")
     boton_Impactrueno.configure(state="disabled")

#Habilita los botones al terminar el movimiento
def show():
     boton_aranazo.configure(state="normal")
     boton_ColaHierro.configure(state="normal")
     boton_Electrobola.configure(state="normal")
     boton_Impactrueno.configure(state="normal")

#Labels donde se van imprimiendo los TP restantes
contador = tk.Label(juego, text = "TP: 25")
contador.place(x = 50, y = 470)

contador2 = tk.Label(juego, text= "TP: 18")
contador2.place(x = 150, y = 470)

contador3 = tk.Label(juego, text="TP: 15")
contador3.place(x = 250, y = 470)

contador4 = tk.Label(juego, text="TP: 15")
contador4.place(x = 350, y = 470)

#Botones de movimientos
boton_aranazo = tk.Button(juego, text = "Arañazo", command = Cuadruple_ComandoA)
boton_aranazo.place(x = 50, y = 420)

boton_Impactrueno = tk.Button(juego, text = "Impactrueno", command = Cuadruple_ComandoI)
boton_Impactrueno.place(x = 150, y = 420)

boton_ColaHierro = tk.Button(juego, text = "Cola de Hierro", command = Cuadruple_ComandoC)
boton_ColaHierro.place(x = 250, y = 420)

boton_Electrobola = tk.Button(juego, text = "Electrobola", command = Cuadruple_ComandoE)
boton_Electrobola.place(x = 350, y = 420)


juego.mainloop()