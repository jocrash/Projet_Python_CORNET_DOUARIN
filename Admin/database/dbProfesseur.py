__author__ = 'Joel CORNET'
from Admin.database.models import Professeur
from Admin.database.models import CVprof

class dbProfesseur:

    def save(self,professeur):
        professeur.save()

    def modify(self,id,nom,prenom,cin,sexe,telephone,email,date):
        Professeur.objects.filter(id=id).update(nom=nom,prenom=prenom,cin=cin,telephone=telephone,email=email,date=date)

    def returnOne(self,id):
        try:
            professeur = Professeur.objects.get(id=id)
            return professeur
        except:
            return None

    def delete(self,id):
        Professeur.objects.filter(id=id).delete()

    def returnAll(self):
        list = Professeur.objects.all()
        return list

    def searchEtab(self,nom):
        professeur = Professeur.objects.get(nom=nom)
        return professeur

    def isExist(self,nom,prenom,cin,sexe,telephone,email):
        try:
            etab = Professeur.objects.get(nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email)
            return True
        except:
            return False

##### GESTION CV DU PROFESSEUR ####

    def saveCV(self,cv):
        cv.save()

    def returnCV(self,id):
        try:
            prof = Professeur.objects.get(id=id)
            cv = CVprof.objects.get(idprof_id=id)
            return cv
        except:
            return None

    ##def modifierCV(self,id):

    ##def deleteCV(self,id):


    def isCVExist(self,idprof,nom,prenom,cin,sexe,telephone,email,formation,etude,experience,langue,reference):
        try:
            etab = Professeur.objects.get(idprof=idprof,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,formation=formation,etude=etude,experience=experience,langue=langue,reference=reference)
            return True
        except:
            return False


