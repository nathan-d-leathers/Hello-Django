"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
import math

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.http import HttpResponse

def rootRouteHandler(request):
    response = HttpResponse("<h1>Welcome to the internet</h1>") # every request must receive one response
    print('=-=-=-=-=-=-=-=')
    print(dir(request))
    print('--------------')
    print(dir(response))
    print('=-=-=-=-=-=-=-=')
    return response


def anotherRouteHandler(request):
    response = HttpResponse("<marquee>We can make as many routes as we want</marquee>")
    response.status_code = 418

    # django automatically puts query string variables into a dictionary
    print(request.GET.get('format'))

    return response 

def withParams(request, format='h1'):
    print(format)
    return HttpResponse(f"<{format}>Hello Django</{format}")

def withParams(request, format='h1'):
    print(format)
    return HttpResponse(f"<{format}>Hello Django</{format}")


def forRectangleArea(request, height=2, width=4):
    print(height, width)
    area = height * width
    return HttpResponse(f"<h1>{area}</h1>")

def forRectanglePerimeter(request, height, width):
    print(height, width)
    perimeter = (height * 2) + (width * 2)
    return HttpResponse(f"<h1>{perimeter}</h1>")

def forCircleArea(request, radius):
    area = round((math.pi * radius ** 2), 2)
    return HttpResponse(f"<h1>{area}</h1>")

def forCirclePerimeter(request, radius):
    perimeter = round((2 * math.pi * radius), 2)
    return HttpResponse(f"<h1>{perimeter}</h1>") 


urlpatterns = [
    path('admin/', admin.site.urls), # default admin routes, provided for free by django
    path('', rootRouteHandler),
    path('another-route/', anotherRouteHandler),
    path('another-route/<str:format>', withParams),
    path('rectangle/area/<int:height>/<int:width>', forRectangleArea),
    path('rectangle/perimeter/<int:height>/<int:width>', forRectanglePerimeter),
    path('circle/area/<int:radius>', forCircleArea),
    path('circle/perimeter/<int:radius>', forCirclePerimeter)
]

