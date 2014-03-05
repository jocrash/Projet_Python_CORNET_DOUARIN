__author__ = 'Joel CORNET'
from Admin.database.models import Programme

class dbProgramme:

    def save(self,programme):
        programme.save()

    def modify(self,id,domaine,mention,specialite,typecours,langue,date):
        Programme.objects.filter(id=id).update(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue,date=date)

    def returnOne(self,id):
        try:
            programme = Programme.objects.get(id=id)
            return programme
        except:
            return None

    def delete(self,id):
        Programme.objects.filter(id=id).delete()

    def returnAll(self):
        list = Programme.objects.all()
        return list

    def isExist(self,domaine,mention,specialite,typecours,langue):
        try:
            etab = Programme.objects.get(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue)
            return True
        except:
            return False

