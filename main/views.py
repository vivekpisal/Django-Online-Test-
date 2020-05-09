from django.shortcuts import render,redirect
from .forms import InfoForm,PostForm,GroupForm,NoticeForm,PollForm
from .models import Info,Post,User,Group,Members,Notice,Poll
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url='/login/')
def info(response):
	if response.method=='POST':
		if response.user.is_authenticated:
			form=InfoForm(response.POST,response.FILES)
			if form.is_valid():
				e=form.cleaned_data['email']
				p=form.cleaned_data['phone']
				g=form.cleaned_data['Gender']
				ro=form.cleaned_data['SorT']
				pr=form.cleaned_data['profile']
				f=Info(li=response.user,email=e,phone=p,SorT=ro,profile=pr,Gender=g)
				f.save()
				return HttpResponseRedirect("profile")
	else:
		form=InfoForm()
	return render(response,'main/infoform.html',{'form':form})





def register(response):
	if response.method=='POST':
		form=UserCreationForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		if not response.user.is_authenticated:
			form=UserCreationForm()
			return render(response,'main/register.html',{'form':form})
		else:
			return redirect('home')
	return redirect('login')





@login_required(login_url='/login/')
def home(request):
	if Info.objects.filter(li=request.user).exists():
		return render(request,'main/home.html')
	else:
		return redirect('info')





def login(response):
	if response.user.is_authenticated:
		return redirect('home')
	else:
		return HttpResponseRedirect('/login/')





@login_required(login_url='/login/')
def addpost(response):
	if response.method=='POST':
		form=PostForm(response.POST,response.FILES)
		if form.is_valid:
			t=response.POST['text']
			l=response.POST['location']
			p=response.FILES['pic']
			temp=Post(li=response.user,text=t,location=l,pic=p)
			temp.save()
			return redirect('home')
	else:
		form=PostForm()
		return render(response,'main/addpost.html',{'form':form})



 

@login_required(login_url='/login/')
def profile(response):
	if response.method=='POST':
		if response.user.is_authenticated:
			a=Info.objects.get(li=response.user)
			a.profile=response.FILES['profile']
			a.save()
			return HttpResponseRedirect('profile')
	return render(response,'main/profile.html',{'x':3})





@login_required(login_url='/login/')
def search(response):
	if response.method=='POST':
		f=response.POST['search']
		if User.objects.filter(username=f):
			data=User.objects.filter(username__iexact=f)
			data1=Info.objects.filter(li=data[0])
			data2=Post.objects.filter(li=data[0])
			return render(response,"main/search.html",{'data':data,'data1':data1,'data2':data2,'f':f})
		else:
			return render(response,"main/profile.html",{'x':0})
	else:
		return render(response,"main/profile.html",{'x':1})





@login_required(login_url='/login/')
def addgrp(request):
	if request.method=='POST':
		form=GroupForm(request.POST)
		if form.is_valid:
			name=request.POST['name']
			st=request.POST['stream']
			description=request.POST['description']
			gi=request.POST['groupicon']
			temp=Group(li=request.user,name=name,stream=st,description=description,groupicon=gi)
			temp.save()
			temp1=Members(li=temp,name=request.user)
			temp1.save()
			return HttpResponseRedirect('mygrp')
	else:
		form=GroupForm()
		return render(request,'main/addgrp.html',{'form':form})




@login_required(login_url='/login/')
def mygrp(request):
	if request.method=='POST':
		f=request.POST['number']
		ser=Group.objects.filter(grkey=f)
		temp=Members(li=ser[0],name=request.user)
		temp.save()
		data=Members.objects.filter(name=request.user)
		return render(request,'main/mygrp.html',{'data':data})
	else:
		data=Members.objects.filter(name=request.user)
		return render(request,'main/mygrp.html',{'data':data})





@login_required(login_url='/login/')
def viewgrp(request,id,name):
	data=Group.objects.filter(id=id)
	data1=Members.objects.filter(li__name=name)
	data2=Notice.objects.filter(li__name=data[0])
	data3=Poll.objects.filter(li__name=data[0])
	context={'data':data,'data1':data1,'id':id,'data2':data2,'data3':data3}
	return render(request,'main/viewgrp.html',context)





@login_required(login_url='/login/')
def addnotice(request,id):
	if request.method=='POST':
		form=NoticeForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			data=Group.objects.filter(id=id)
			post.li=data[0]
			post.save()
			return redirect('home')
	else:
		form=NoticeForm()
	return render(request,'main/addnotice.html',{'form':form})




@login_required(login_url='/login/')
def takepoll(request,id):
	if request.method=='POST':
		form=PollForm(request.POST)
		if form.is_valid():
			poll=form.save(commit=False)
			data=Group.objects.filter(id=id)
			poll.li=data[0]
			poll.save()
			return redirect('mygrp')
	else:
		form=PollForm()
	return render(request,'main/takepoll.html',{'form':form})




@login_required(login_url='/login/')
def givepollans(request,id):
	if request.method=='POST':
		poll=Poll.objects.filter(id=id)
		data=request.POST['option_one']
		for i in poll:
			if i.option_one==data:
				i.count_one+=1
			elif i.option_two==data:
				i.count_two+=1
			elif i.option_three==data:
				i.count_three+=1
		i.save()
		poll=Poll.objects.filter(id=id)
		return render(request,'main/showvotes.html',{'data':poll})

	data=Poll.objects.filter(id=id)
	return render(request,'main/givepollans.html',{'data':data})