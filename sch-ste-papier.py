# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import time

print(
"******************************************************\n"
"* Ich heiße German Kafo Tsakou (lakaf2035@gmail.com) *\n"
"*               Willkommen                           *\n"
"******************************************************\n");time.sleep(0.3)

#Einleitung 
print(
"*********************\n"
"*SCHERE STEIN PAPIER*\n"
"*********************\n"
)
print(
"*************************\n"
"* So geht es:           *\n");time.sleep(0.6)
print( 
"*************************\n"
"* Schere schlägt Papier *\n"
"* Stein schlägt Schere  *\n"
"* Papier schlägt Stein  *\n"
"* Gleich=> Unentschieden*\n"
"*************************\n"
);time.sleep(0.5)

print(

"**  los  +++  geht ++   **\n");time.sleep(0.6)

#Variation
figuren = ("Schere", "Stein", "Papier")


def spiel():
    Spieler_A=figuren[2] #immer Papier
    u=0; #Unentschieden
    a=0; #Spieler_A gewinnt
    b=0; #Spieler_A gewinnt
    
    for i in range(100):
        if (u<32 and a<31 and b<37):
            Spieler_B=figuren[random.randint(0,2)] #zufällig 
        elif(u==32 and a<31 and b<37):
            Spieler_B=figuren[random.randint(0,1)] #zufällig
        elif(b==37 and a<31 and u<32):
            Spieler_B=figuren[random.randint(1,2)] #zufällig
        elif(a==30 and b<37 and u<32):
            Spieler_B=figuren[random.randint(0,2,2)] #zufällig
        elif(a<31 ):
            Spieler_B=figuren[1] 
        elif( b<37 ):
            Spieler_B=figuren[0] 
        elif( u<32):
            Spieler_B=figuren[2] 
  

        if  Spieler_A == Spieler_B:
            print(i+1,") Unendschieden, Spieler_A und Spieler_B hatten beide", Spieler_A,"genommen.\n")
            u +=1
        elif Spieler_B == "Stein":
            print(i+1,") Spieler_A hat gewonnen,er hat " ,Spieler_A, " genommen und spieler_B hat " ,Spieler_B, " genommen.\n" )
            a +=1
        elif Spieler_B == "Schere":
            print(i+1,") Spieler_B hat gewonnen,er hat ", Spieler_B ," genommen und spieler_A hat ",Spieler_A," genommen.\n" )
            b +=1
    print(
    "*****************************\n"
    "*    Das Endergebnis  ist:  *\n"
    "*****************************\n");time.sleep(0.6)
    print(
    "*   Spieler_A : ",a,"Sieg   *\n"  );time.sleep(0.3)
    print(
    "*   Spieler_B : ",b,"Sieg   *\n" );time.sleep(0.3)
    print(
    "*   Unentschieden: ",u,"Mal *\n" 
    "*****************************\n");time.sleep(0.3)
    
    N=int(input("Wollen sie noch eine Runde? \n 1 für Ja und andere für nein \n")) #noch mal spielen
   
    if N==1 :
        print(

        "**  los  +++  geht ++   **\n");time.sleep(0.4)
        spiel()
    else:
        print("danke tschüss");time.sleep(0.3)
        exit
    
        
        
spiel() #Execution of the game    
        