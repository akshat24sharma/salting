from django.shortcuts import render
from .models import salting
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import saltingform
import hashlib
import random
# Create your views here.

def saltpost(request):
    context = {
         "salting": salting.objects.last(),
         
         
    }
    
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('password'):
            post=salting()
            post.username=request.POST.get('username')
            post.password=request.POST.get('password')
            str=post.password
            
            rand = random.randint(1, 5)
            rand2=random.randint(6,10)
            rand3=random.randint(1,10)
            salt = str[rand:rand2]
            result = hashlib.md5(str.encode())
            hashed=result.hexdigest()
            str1=list(hashed)
            str1.insert(rand3, salt + "HERE")
            
            join= ''.join(str1)
            post.password=join
            post.salt=salt
            post.salt_pos=rand3
            

            
            post.save()
            return HttpResponseRedirect("/")
     
    
    return render (request,"salt.html",context)

def second(request):

         user=salting()
       
            
         try:
             use=salting.objects.all()
         except:
              raise Http404("no user")
         return render(request, "second.html",{"user":use})

def login(request):
    log=salting()

    try:
     login=salting.objects.all()
    except:
        raise Http404("no user")

    return render(request,"login.html",{"user1":salting.objects.all()})


    


    



  


