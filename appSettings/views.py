from django.shortcuts import render
from .models import Setting

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class SettingsView(APIView):
    def get(self, request, format=None):
        settingsDict = {}
        #{"NAME":"VALUE", "NAME2": "VALUE2"}
        try:
            settingObjects = Setting.objects.all()
            
            for setting in settingObjects:
                settingsDict[setting.name] = setting.value
                
            return Response(settingsDict, status=201)
        except:
            
            return Response(status=400)
        
    def post(self, request, format=None):
        # This view we are going to create a new settings in db
        
        #JSON Object: {'settings': [{"NAME": "VALUE"}, {"NAME2" : "VALUE2"}]}
        settings = request.data['settings']
        bad_setting = []
        for setting in settings:
            try:
                new_setting = Setting.objects.create(name=setting['NAME'], value=setting['VALUE'] )
                
                new_setting.save()
            except:
                bad_setting.append(setting)
        if len(bad_setting) > 0:
            return Response({"Invalid Settigns":bad_setting}, status=200)
        else:
            return Response(status=200)