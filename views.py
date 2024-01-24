# this file was created by me and it was not given or created by me..

from urllib import request
from string import punctuation
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 

     return render(request,"textutilites.html")
    # content = {
    #     "Data" : "Youtube is best ",
    #     "Roll_number":["1","2","3","4","5","6","7","8","9"],
    #     "first_name" : "Shivam",
    #     "last_name" : "Yadav",
    #     "variable_name" : " i am repeating this lecture."

    # }

   

#     return HttpResponse('''<nav style="margin:50px;"> <a href="www.google.com">Google</a><br>
# <a href="www.instagram.com">Instagram</a><br>
# <a href="www.facebook.com" >Facebook</a><br>
# <a href="www.whatsapp.com" >Whatsapp</a>''')
def removepunctuations(request):
    inputtext = request.GET.get('text','default')
    removepunctuations = request.GET.get('removepunctuations','off')
    capitalize =  request.GET.get('capitalize','off')
    spaceremover =  request.GET.get('spaceremover','off')


    if removepunctuations == 'on':
        punctuations = '''!@%^&$$*()_+-={}[];,#:></'''
        analyzed = ""
        for char in inputtext:
                if char not in punctuations:
                     analyzed =  analyzed + char

        user_text = {'Task':'Removed punctuations','analyzed_Text':analyzed}           
        return render(request,'analyzed2.html',user_text)
        
          
 
    if capitalize == 'on':
        analyzed = ""
        for char in inputtext:
                analyzed  = analyzed + char.upper()

        user_text = {'Task':'capitalized text','analyzed_Text':analyzed}  
        return render(request,'analyzed-2.html',user_text)
        #inputtext = analyzed

    if spaceremover == 'on':
         analyzed = ""
         for index,char in enumerate(inputtext):
            if( inputtext[index] == " " and inputtext[index+1] == " "):
              pass
            else:
              analyzed = analyzed + char

         user_text = {'Task': 'space remover','analyzed_Text':analyzed}
         return render(request,'analyzed-2.html',user_text)
         #inputtext =  analyzed

    else:  
        return HttpResponse("no output")

def capitalize(request):
    return HttpResponse("capitalize")

def spaceremover(request):
     return HttpResponse("spaceremover")






def about(request):
    return HttpResponse("This contains all information about  this page ")

def home(request):
    return HttpResponse("Welcome to the Homepage")
 










