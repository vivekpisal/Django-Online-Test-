from django.forms import ModelForm
from .models import *


class InfoForm(ModelForm):
	class Meta:
		model=Info
		fields=['email','phone','profile','Gender','SorT']



class PostForm(ModelForm):
	class Meta:
		model=Post
		fields=['text','location','pic']



class GroupForm(ModelForm):
	class Meta:
		model=Group
		fields=['name','stream','description','groupicon']




class NoticeForm(ModelForm):
	class Meta:
		model=Notice
		fields=['text']



class PollForm(ModelForm):
	class Meta:
		model=Poll
		fields=['question','option_one','option_two','option_three']
