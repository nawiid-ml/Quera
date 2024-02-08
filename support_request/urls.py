from django.urls import path 
from .views import AskTheGBTCreateView , AskTheTeacherCreateView

urlpatterns = [
    path('',AskTheTeacherCreateView.as_view(),name='Teacher'),
    path('gpt',AskTheGBTCreateView.as_view(),name='GBT'),

]
