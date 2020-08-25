from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Member(User):
    mobile_no=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    fullname=models.CharField(max_length=200,default="Full name ")
    pycoins=models.IntegerField(default=500)
class CreateForm(UserCreationForm):
    class Meta:
        model=Member
        fields=['username','password1','password2','email','mobile_no','institution','fullname']
class Studymaterial(models.Model):
    name=models.CharField(max_length=50)
    image=models.TextField()
    link=models.TextField()
    rating=models.CharField(max_length=5)
    description=models.TextField(default="This will help you")
    image=models.TextField()
    relation=models.CharField(max_length=100,default="html+css/bootstrap/figma/git/sql/numpy")
    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=100)
    link=models.CharField(max_length=700,default="whatsapp link")
    t_link=models.CharField(max_length=700,default="telegram link")
    available=models.BooleanField()
    description=models.TextField(default="Description")
    pycoin_value=models.IntegerField()
    image=models.TextField()
    relate=models.CharField(max_length=100,default="ws/comp/self")
    def __str__(self):
        return self.name
class Registeredevent(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)+" joined "+str(self.event.name)

class Tutor(models.Model):
    name=models.CharField(max_length=100)
    field=models.CharField(max_length=100)
    image=models.TextField()
    description=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Timeline(models.Model):
    date=models.DateTimeField()
    level=models.CharField(max_length=100,default="beginner/Intermediate/Advance")
    tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE)
    chapter=models.IntegerField()
    name=models.CharField(max_length=100)
    image=models.TextField(default="niranja preferably square image inte link ")
    def __str__(self):
        return self.name
