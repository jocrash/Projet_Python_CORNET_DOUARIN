__author__ = 'Joel CORNET'

from Admin.database.models import Users

class dbUsers:

    def save(self,users):
        users.save()

    def modify(self,id,nom,prenom,username,password,date):
        Users.objects.filter(id=id).update(nom=nom,prenom=prenom,username=username,password=password,date=date)

    def returnOne(self,username):
        try:
            user = Users.objects.get(username=username)
            professeur=user.professeur
            return professeur
        except:
            return None

    def delete(self,id):
        Users.objects.filter(id=id).delete()

    def returnAll(self):
        list = Users.objects.all()
        return list

    def searchEtab(self,nom):
        professeur = Users.objects.get(nom=nom)
        return professeur

    def isExist(self,username):
        try:
            etab = Users.objects.get(username=username)
            return True
        except:
            return False


