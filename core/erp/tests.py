from config.wsgi import *
from core.erp.models import Type, Employee

# Create your tests here.

#funcion listar

#query= Type.objects.all()
#print(query)

#funcion incersion
#t=Type(name='carnicero').save()

#funcion actualizacion
# try:
#     T=Type.objects.get(pk=1)
#     T.name='Presidente'
#     T.save()
# except Exception as e:
#     print(e)


#funcion eliminacion
#T=Type.objects.get(pk=1)
#T.delete()

#obj = Type.objects.filter(name__in=['hfjdjd','Analista datos']).count()
# for i in  Type.objects.filter(name__endswith='o')[2:3]:
#     print(i)

