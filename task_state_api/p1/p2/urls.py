
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', add, name='add'),
    path('list/', listall, name='list'),
    path('change_state/', change_state),
    path('delete/<int:id>', delete, name='delete')
]