from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', view.home),
    path('counts/', view.count, name='count'),
]
