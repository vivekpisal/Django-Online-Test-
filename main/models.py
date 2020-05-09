from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
# Create your models here.


class Info(models.Model):
	li=models.OneToOneField(User,on_delete=models.CASCADE,related_name='info')
	email=models.EmailField(unique=True)
	phone=models.IntegerField()
	ch=(('student','student'),('teacher','teacher'))
	SorT=models.CharField(max_length=10,choices=ch,default='student')
	profile=models.ImageField(upload_to='images/profile/',default='download_40S1UkL.png')
	role=(('male','Male'),('female','Female'),('other','Other'))
	Gender=models.CharField(max_length=20,choices=role,default='male')


	def __str__(self):
		return (f'EMAIL:{self.email}  ROLE: {self.SorT}')



class Post(models.Model):
	li=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
	text=models.TextField()
	location=models.CharField(max_length=20,blank=True)
	datetime=models.DateTimeField(default=timezone.now)
	pic=models.ImageField(upload_to='images/post/')

	
	def __str__(self):
		return self.location



class Group(models.Model):
	li=models.ForeignKey(User,on_delete=models.CASCADE,related_name='group')
	name=models.CharField(max_length=20,unique=True)
	role=(('school','school'),('college','college'),('higher studies','higher studies'))
	stream=models.CharField(max_length=30,choices=role)
	groupicon=models.ImageField(upload_to='images/group/',default='download.png')
	description=models.CharField(max_length=20)
	grkey=models.TextField(unique=True,default=random.randint(100000,10000000))


	def __str__(self):
		return self.name



class Members(models.Model):
	li=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='member',default=None)
	name=models.CharField(max_length=30)


	def __str__(self):
		return (f'GROUP_NAME:{self.li}   MEMBER:{self.name}')




class Notice(models.Model):
	li=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='notice')
	text=models.TextField()


	def __str__(self):
		return (f'{self.li}')



class Poll(models.Model):
	li=models.ForeignKey(Group,on_delete=models.CASCADE)
	question=models.CharField(max_length=100)
	option_one=models.CharField(max_length=30)
	option_two=models.CharField(max_length=30)
	option_three=models.CharField(max_length=30)
	count_one=models.IntegerField(default=0)
	count_two=models.IntegerField(default=0)
	count_three=models.IntegerField(default=0)


	def __str__(self):
		return self.question



