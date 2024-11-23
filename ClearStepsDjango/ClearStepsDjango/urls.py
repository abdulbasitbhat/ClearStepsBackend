from django.contrib import admin
from django.urls import path,include
import ClearSteps

urlpatterns = [
    path('api/',include("ClearSteps.urls")),
    path('admin/', admin.site.urls),
]
