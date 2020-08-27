from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import CreateForm,Member,Studymaterial,Event,Registeredevent,Tutor,Timeline
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
#Home Page

def Home(request):
    tutors=Tutor.objects.all().order_by('-pub_date')
    time=Timeline.objects.all().order_by('chapter')
    try:
        user=Member.objects.all().get(username=request.user.username)

        reg_events=user.registeredevent_set.all()
        return render(request,'home.html',{'user':user,'event':reg_events,'tutors':tutors,'times':time})
    except:
        return render(request,'home.html',{'tutors':tutors,'times':time})
#authentication
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    #if(request.user.is_authenticated):
    #    return redirect('home')
    if request.method=='POST':
        form=CreateForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = form.cleaned_data.get('username')

            login(request,Member.objects.all().get(username=user))
            messages.success(request,"success")
            return redirect('home')
        else:
            errors=form.errors
            form = CreateForm()
            return render(request,'signup.html',{'form':form,'errors':errors})
    form = CreateForm()
    return render(request,'signup.html',{'form':form,'errors':form.errors})
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method=='POST'):
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"Username or password is incorrect!!")
            return redirect('login')
    return render(request,'login.html',{})
#studymaterial
@login_required(login_url='login')
def StudyMaterial(request):
    html=Studymaterial.objects.all().filter(relation="html")
    git=Studymaterial.objects.all().filter(relation="git")
    panda=Studymaterial.objects.all().filter(relation="panda")
    ui=Studymaterial.objects.all().filter(relation="ui")
    sql=Studymaterial.objects.all().filter(relation="sql")

    return render(request,'studymaterial.html',{'html':html,'git':git,'panda':panda,'ui':ui,'sql':sql})
@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')
#data admin
def AdminData(request,val):
    if(val=="all"):
        members=Member.objects.all()
        i=0
        data={}
        i=0
        for user in members:
           data[i]={'name':user.fullname,'email':user.email,'institution':user.institution,'mobile':user.mobile_no} 
           i+=1
        return JsonResponse({'users':data})
    event=Event.objects.all().get(name=val)
    ls=Registeredevent.objects.all().filter(event=event)
    data={}
    i=0
    for item in ls:
        data[i]={'name':item.user.fullname,'event':item.event.name,'email':item.user.email,'institution':item.user.institution,'mobile':item.user.mobile_no}
        i+=1
    return JsonResponse({'pyweek':data})
@login_required(login_url='login')
def EventRegister(request):
    workshops=Event.objects.all().filter(relate="ws")
    competitions=Event.objects.all().filter(relate="comp")
    selfs=Event.objects.all().filter(relate="self")
    mem=Member.objects.all().get(username=request.user.username)
    regs=mem.registeredevent_set.all()
    regs=[reg.event for reg in regs]
    print(regs)
    return render(request,'events.html',{"workshops":workshops,'competitions':competitions,'selfs':selfs,'user':mem,'regs':regs,})
@login_required(login_url='login')
def Confirm(request):
        if(request.is_ajax and request.method=="GET"):
            try:
                event=Event.objects.all().get(name=request.GET['name'])
            except:
                return JsonResponse({"success":"Error"})
            user=Member.objects.all().get(username=request.user.username)
            if(user.registeredevent_set.all().filter(event=event)):
                return JsonResponse({"success":"Already registered"})
            else:
                if(user.pycoins<int(request.GET['pytokens'])):
                    return JsonResponse({"success":"not enough coins"})
                user.pycoins -= int(request.GET['pytokens'])
                user.registeredevent_set.create(event=event)
                user.save()
                message="""
                Hello {name}

                The coordinators of PyWeek2020 thank you for registering in {event} event/competition.
                We hope you have a great experience and learn something new out of it.

                further details please join the WhatsApp link as well as the telegram link given below.
                WhatsApp:{link}
                Telegram:{t_link}

                PyWeek wishes you happy coding 🙌.
                With ❤️ and Python
                #pyweek  #pyweek2020
                """.format(name=user.fullname,event=event.name,link=event.link,t_link=event.t_link)
                send_mail("PyWeek2020 Event registration details",message,request.user.email,[request.user.email],fail_silently=False)
                return JsonResponse({"success":"Registration successful"})
def Install(request):
    return redirect('https://niranjanprof.github.io/Python-Requirements/')
