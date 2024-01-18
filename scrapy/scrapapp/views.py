from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib import messages
from .models import *
import pandas as pd

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    def post(self,request:Request):
        # serializer = SignUpSerializer(data=request.data)
        data=request.data
        serializer=self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# def register(request):     
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         state = request.POST.get('state')
#         country = request.POST.get('country')
#         password = request.POST.get('password')
#         confirmpassword = request.POST.get('repassword')
#         if password == confirmpassword:
#             if User.objects.filter(username=username).exists():      
#                 messages.info(request,"Username already exist")
#                 return redirect('registerpage')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     print("email already exists")
#                     return redirect('registerpage')
#                 else:
#                     user = User.objects.create_user(username=username,email=email,password=password)
#                     user.save()
#                     data = Profile(user = user,name=username,state=state,country=country,phone = phone)
#                     print(data)
#                     data.save()    
#                     messages.info(request,"info add")
#                     return redirect('registerpage')

#         else:
#             messages.info(request,"password does not match")
#             return redirect('registerpage')

#     return render(request,'register.html')



def register(request):     
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        country = request.POST.get('country')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('repassword')
        if password == confirmpassword:
            poke = pd.read_csv("D:\\scrapy\\scrapy\\scrapapp\\excel\\namelist.csv")
            data_in_file = poke.loc[poke['Name']==username]
            if data_in_file.empty:
                if User.objects.filter(username=username).exists():      
                    messages.info(request,"Username already exist")
                    return redirect('registerpage')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.info(request,"email already exist")
                        return redirect('registerpage')
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save()
                        data = Profile(user = user,name=username,state=state,country=country,phone = phone)
                        print(data)
                        data.save()    
                        messages.info(request,"info add")
                        return redirect('registerpage')
                    
            else:
                state_in_file = data_in_file['State'].values[0]
                country_in_file = data_in_file['Country'].values[0]
                if state == state_in_file:
                    if country == country_in_file:
                        messages.info(request,"sorry as you are a criminal you cannot register bye")
                        return redirect('registerpage')
                    
                    else:
                        if User.objects.filter(username=username).exists():      
                            messages.info(request,"Username already exist")
                            return redirect('registerpage')
                        else:
                            if User.objects.filter(email=email).exists():
                                messages.info(request,"email already exist")
                                return redirect('registerpage')
                            else:
                                user = User.objects.create_user(username=username,email=email,password=password)
                                user.save()
                                data = Profile(user = user,name=username,state=state,country=country,phone = phone)
                                print(data)
                                data.save()    
                                messages.info(request,"info add")
                                return redirect('registerpage')
                            
                else:
                    if User.objects.filter(username=username).exists():      
                        messages.info(request,"Username already exist")
                        return redirect('registerpage')
                    else:
                        if User.objects.filter(email=email).exists():
                            messages.info(request,"email already exist")
                            return redirect('registerpage')
                        else:
                            user = User.objects.create_user(username=username,email=email,password=password)
                            user.save()
                            data = Profile(user = user,name=username,state=state,country=country,phone = phone)
                            data.save()    
                            messages.info(request,"info add")
                            return redirect('registerpage')
        else:
            messages.info(request,"password does not match")
            return redirect('registerpage')
                            
           
    return render(request,'register.html')