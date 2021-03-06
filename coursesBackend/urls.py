"""coursesBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework import routers
from courses.views import CourseViewSet
from chatbox.views import ChatboxFormViewSet
from . import settings

#routers: used for dynamic endpoints (ex. localhost8000)
#generates many urls

# CREATE A ROUTER
router = routers.SimpleRouter()

#Registering /courses endpoint
router.register('courses', CourseViewSet)
router.register('chatbox', ChatboxFormViewSet)

urlpatterns = [
    path('', include(router.urls)), #include those urls generated by router
    path('admin/', admin.site.urls),
] 

#for allowing django to process image urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
