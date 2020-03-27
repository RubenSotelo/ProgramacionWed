from django.shortcuts import render
#librerias de funcionamiento 
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

#accion que tiene la vista se tienen en la vista con cada archivo html
    #crear una clase para la vista
class DashboardClass(View):
    URL='Dashboard/dashboard.html'
    def get(self,request,*args,**kwargs):
        # retorno la direcion de la carpeta para cada html
        return render(request,self.URL,{'mensage':'Bienvenido'}) 
    def post(self,request,*args,**kwargs):
        return redirect('Login:Login')
        
        # me redirigo en la urls de dashboard
        