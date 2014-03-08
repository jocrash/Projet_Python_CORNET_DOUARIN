__author__ = 'Joel CORNET'

from Admin.database.models import Idcours

class dbIdcours:

    def save(self,idcours):
        idcours.save()

    def modify(self,id,id_etablissement,annee,semestre,nomcours,codecours,date):
        Idcours.objects.filter(id=id).update(etablissement=id_etablissement,annee=annee,semestre=semestre,nomcours=nomcours,codecours=codecours,date=date)

    def returnOne(self,id):
        try:
            idcours = Idcours.objects.get(id=id)
            return idcours
        except:
            return None

    def returnID(self,codecours):
        try:
            idcours = Idcours.objects.get(codecours=codecours)
            return idcours
        except:
            return None


    def delete(self,id):
        Idcours.objects.filter(id=id).delete()

    def returnAll(self):
        list = Idcours.objects.all()
        return list

    def isExist(self,id_etablissement,annee,semestre,nomcours,codecours):
        try:
            etab = Idcours.objects.get(etablissement=id_etablissement,annee=annee,semestre=semestre,nomcours=nomcours,codecours=codecours)
            return True
        except:
            return False

