

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("search/",views.searchJobView,name="search"),
    # path("report/<pk>",views.jobDetailReportView,name="report"),
]