from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
	path('info',views.info,name='info'),
	path('',views.home,name='home'),
	path('register',views.register,name='register'),
	path('',views.login,name='login'),
	path('addpost',views.addpost,name='addpost'),
	path('profile',views.profile,name='profile'),
	path('search',views.search,name='search'),
	path('addgrp',views.addgrp,name='addgrp'),
	path('mygrp',views.mygrp,name='mygrp'),
	path('mygrp/<int:id>/<str:name>',views.viewgrp,name='viewgrp'),
	path('addnotice/<int:id>',views.addnotice,name='addnotice'),
	path('takepoll/<int:id>',views.takepoll,name='takepoll'),
	path('givepollans/<int:id>',views.givepollans,name='givepollans')
]



if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)



