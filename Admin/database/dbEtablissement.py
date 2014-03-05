__author__ = 'Joel CORNET'
from Admin.database.models import Etablissement

class dbEtablissement:

    def save(self,etablissement):
        etablissement.save()

    def modify(self,id,nom,lieu,date):
        Etablissement.objects.filter(id=id).update(nom=nom,lieu=lieu,date=date)

    def returnOne(self,id):
        try:
            etablissement = Etablissement.objects.get(id=id)
            return etablissement
        except:
            return None

    def delete(self,id):
        Etablissement.objects.filter(id=id).delete()

    def returnAll(self):
        list = Etablissement.objects.all()
        return list

    def searchEtab(self,nom):
        etablissement = Etablissement.objects.get(nom=nom)
        return etablissement

    # def search(self,nom,lieu):
    #     etablissement = Etablissement.objects.get(nom=nom,lieu)
    #     return etablissement

    def isExist(self,nom,lieu):
        try:
            etab = Etablissement.objects.get(nom=nom,lieu=lieu)
            return True
        except:
            return False


