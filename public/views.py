from django.shortcuts import render
from .models import PublicData , PublicUpdate

def comparemachine(request):
    publicdata = PublicData.objects.all()
    publicupdate = PublicUpdate.objects.all()

    for i in publicdata:
        print("id : " + i.id +"         "+ "pb_name : " + i.pb_name)
    print("----------------------------------------------")    
    for i in publicupdate:
        print("id : " + i.id +"         "+ "pb_name : " + i.pb_name)

    for data in publicdata:
        for update in publicupdate:
            print(data.id + "   " + update.id)
    pass