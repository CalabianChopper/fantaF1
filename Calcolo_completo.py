#Librerie
# from flask import Flask
# from flask import render_template
import pandas as pd
import numpy as np


# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('temp1.html')


#Ottenimento dati
#TODO Prendere file xlsx e trasformarlo in un DataFrame
#TODO Estrazione Vettori singoli
dizionario = {"nome" : ["Verstappen",
                   "Russell",
                   "Hamilton",
                   "Ocon","Alonso",
                   "Stroll",
                   "Sainz Jr.",
                   "Albon",
                   "Hulkenberg",
                   "Magnussen",
                   "Leclerc",
                   "Norris",
                   "Gasly",
                   "De Vries",
                   "Tsunoda",
                   "Piastri",
                   "Yu Zhou",
                   "Sargeant",
                   "Bottas",
                   "Perez"],
         "punti" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
lista_piloti_pl1 = []
lista_piloti_pl2 = []
lista_piloti_pl3 = []
lista_piloti_sprint = []

#Calcolo prova libera 1
def pl1 (dizionario, lista_piloti_pl1):
    
    for i in range(0, len(lista_piloti_pl1)):
        if(lista_piloti_pl1[i] == nome_pilota):
            if(i<16):
                return 2
            else:
                return 0
            
#Calcolo prova libera 2
def pl2 (nome_pilota, lista_piloti_pl2):
    for i in range(0, len(lista_piloti_pl2)):
        if(lista_piloti_pl2[i] == nome_pilota):
            if(i<8):
                return 4
            else:
                return 0
            
#Calcolo prova libera 3
def pl3 (nome_pilota, lista_piloti_pl3):
    if not lista_piloti_pl3:
        return 0
    else:
        for i in range(0, len(lista_piloti_pl3)):
            if(lista_piloti_pl3[i] == nome_pilota):
                if(i<4):
                    return 6
                else:
                    return 0
                
#Calcolo qualifica sprint
def sprint(nome_pilota, lista_piloti_sprint):
    if not lista_piloti_sprint:
        return 0
    else:
        for i in range(0, len(lista_piloti_sprint)):
            if(lista_piloti_sprint[i] == nome_pilota):
                if (i==0):
                    return 8
                elif(i==1):
                    return 7
                elif(i==2):
                    return 6
                elif(i==3):
                    return 5
                elif(i==4):
                    return 4
                elif(i==5):
                    return 3
                elif(i==6):     
                    return 2
                elif(i==7):
                    return 1
                else:
                    return 0
                
#Calcolo prove libere
def punti_prove_libere (nome_pilota, lista_piloti_pl1, lista_piloti_pl2, lista_piloti_pl3, lista_piloti_sprint):
    somma_prove_libere = 0
    somma_prove_libere += pl1(nome_pilota, lista_piloti_pl1)
    somma_prove_libere += pl2(nome_pilota, lista_piloti_pl2)
    somma_prove_libere += pl3(nome_pilota, lista_piloti_pl3)
    somma_prove_libere += sprint(nome_pilota, lista_piloti_sprint)
    return somma_prove_libere

