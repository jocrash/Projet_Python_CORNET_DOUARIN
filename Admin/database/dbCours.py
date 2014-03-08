__author__ = 'Joel CORNET'

from Admin.database.models import Cours

class dbCours:

    def save(self,cours):
        cours.save()

    def modify(self,id,idcours,professeur,etablissement,titre,creditECTS,public,prerequis,objectif,description,plan,formatcours,ressources,evaluation,date):
        Cours.objects.filter(id=id).update(idcours=idcours,professeur=professeur,etablissement=etablissement,titre=titre,creditECTS=creditECTS,public=public,prerequis=prerequis,objectif=objectif,description=description,plan=plan,formatcours=formatcours,ressources=ressources,evaluation=evaluation,date=date)

    def returnOne(self,id):
        try:
            idcours = Cours.objects.get(id=id)
            return idcours
        except:
            return None

    def delete(self,id):
        Cours.objects.filter(id=id).delete()

    def returnAll(self):
        list = Cours.objects.all()
        return list

    def fiche(self,id,objectif,description,plan,formatcours,ressources,evaluation,date):
        Cours.objects.filter(id=id).update(objectif=objectif,description=description,plan=plan,formatcours=formatcours,ressources=ressources,evaluation=evaluation,date=date)

    def isExist(self,idcours,professeur,etablissement,titre):
        try:
            etab = Cours.objects.get(idcours=idcours,professeur=professeur,etablissement=etablissement,titre=titre)
            return True
        except:
            return False

