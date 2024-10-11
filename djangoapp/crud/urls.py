from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from crud.views import index
app_name = 'crud'

urlpatterns = [
    #blog:index
    path("", index, name='index'),
]

