__author__ = 'Joel CORNET'

from database.models import Cours

class dbCours:

    def save(self,cours):
        cours.save()

    def modify(self,id,id_cours,professeur,id_etablissement,titre,credit,public,prerequis,objectif,description,plan,formatcours,ressources,evaluation,date):
        Cours.objects.filter(id=id).update(idcours=id_cours,professeur=professeur,etablissement=id_etablissement,titre=titre,creditECTS=credit,public=public,prerequis=prerequis,objectif=objectif,description=description,plan=plan,formatcours=formatcours,ressources=ressources,evaluation=evaluation,date=date)

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

    def isExist(self,idcours,professeur,etablissement,titre):
        try:
            etab = Cours.objects.get(idcours=idcours,professeur=professeur,etablissement=etablissement,titre=titre)
            return True
        except:
            return False

