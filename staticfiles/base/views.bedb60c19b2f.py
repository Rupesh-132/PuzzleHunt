from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from puzzlehunt import settings
from base.models import Question

from django.core.mail import send_mail
from django.urls import reverse



# Create your views here.



def home(request):
    return render(request,"authentication/index.html")



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if User.objects.filter(username = username):
            messages.error(request,'user already exists')
            return redirect('home')
        
        if User.objects.filter(email = email):
            messages.error(request,"Email already registered")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request,"User name must be under 10 characters")

        
        if pass1!=pass2:
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric!")
            return redirect('home')
        

        myuser = User.objects.create_user(username,email,pass1)
       
        myuser.save()

        # messages.success(request,"Your account has been succefully created.")

        return redirect('signin')
    

    return render(request,"authentication/signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1  = request.POST['pass1']

        user = authenticate(username = username,password = pass1)

        if user is not None:
            login(request,user)
           
            return render(request,'authentication/index.html')
        else:
            messages(request,"Bad Credentials!")
            return redirect('home')

    return render(request,"authentication/signin.html")


def signout(request):

    logout(request)
    
    return redirect('home')


def restart(request):

    return redirect('signout')

def play(request):
    
    questionData = Question.objects.all()
    print(questionData)
    
    data = []

    for question in questionData:
        data.append({
            "question":question.puzzle,
            "ans":question.ans
        })

    payload = {'data':data}
    #print(type(payload))

    return render(request,'puzzles/puzzle1.html',payload)

def checkanspuzzle1(request):

    questionData = Question.objects.all()
    #print(questionData)
    
    data = []

    for question in questionData:
        data.append({
            'uuid':question.uid,
            "question":question.puzzle,
            "ans":question.ans
        })

    
    
    flag = False

    payload = {'data':data}

    if request.method == "POST":
        user_ans = request.POST.get('ans')
        

        if user_ans.lower() == data[0]['ans']:
            flag = True
        
            new_payload = {'data':data,'flag':flag}
            return render(request,"puzzles/puzzle2.html",new_payload)
        else:
            #messages.error(request,"Nice try!! think harder now")
            #return redirect(request. META['HTTP_REFERER'])
            payload = {'data':data,'flag':flag}
            print(flag)
            pass
        


    return render(request,"puzzles/puzzle1.html",payload)


def puzzle1hint(request):
    return render(request,"puzzles/puzzle1hint.html")

def imghintpuzz1(request):
    return render(request,'puzzles/imghintpuzz1.html')




def checkanspuzz2(request):

    questionData = Question.objects.all()
    #print(questionData)
    
    data = []

    for question in questionData:
        data.append({
            'uuid':question.uid,
            "question":question.puzzle,
            "ans":question.ans
        })
    

    payload = {'data':data}
   
    #print(data[0])
   
    if request.method == "POST":
        user_ans = request.POST.get('ans')
        #print(user_ans)
        #print(data[1]['ans'])

        if user_ans.lower() == data[1]['ans']:
            #print('yes matched')
            return render(request,"puzzles/puzzle3.html",payload)
        else:
             pass
             #messages.error(request, "Incorrect answer. Please try again.")
        
    return render(request,'puzzles/puzzle2.html',payload)
        

def playcrossword(request):
     return render(request,'puzzles/crossWord.html')

   
def checkanspuzz3(request):

    questionData = Question.objects.all()
    #print(questionData)
    
    data = []

    for question in questionData:
        data.append({
            'uuid':question.uid,
            "question":question.puzzle,
            "ans":question.ans
        })
    

    payload = {'data':data}
   
    #print(data[0])
   
    if request.method == "POST":
        user_ans = request.POST.get('ans')
        #print(type(user_ans))
        #print(type(data[2]['ans']))

        if user_ans == data[2]['ans']:
            #print('yes matched')
            return render(request,"puzzles/puzzle4.html",payload)
        else:
            pass
             #messages.error(request, "Incorrect answer. Please try again.")
        
    return render(request,'puzzles/puzzle4.html',payload)
        
def puzzle3hint(request):
    return render(request,'puzzles/puzzle3hint.html')



def checkanspuzz4(request):

    questionData = Question.objects.all()
    #print(questionData)
    
    data = []

    for question in questionData:
        data.append({
            'uuid':question.uid,
            "question":question.puzzle,
            "ans":question.ans
        })
    

    payload = {'data':data}
   
    #print(data[0])
   
    if request.method == "POST":
        user_ans = request.POST.get('ans')
        #print(type(user_ans))
        print(data[3]['ans'])

        if user_ans.lower() == data[3]['ans']:
            print('yes matched')
            return render(request,"puzzles/congratulations.html",payload)
        else:
            pass
             #messages.error(request, "Incorrect answer. Please try again.")
        
    return render(request,'puzzles/puzzle4.html',payload)




def puzzle4hint(request):
    return render(request,'puzzles/puzzle4hint.html')