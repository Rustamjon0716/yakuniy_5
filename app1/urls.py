from django.urls import path
from .views import (AllContentView,allContentView,SDetailContentView,IDetailContentView,
                    SCreateContentView,ICreateContentView,SUpdateContentView,IUpdateContentView,
                    SDeleteContentView,IDeleteContentView)

urlpatterns = [
    path('all_newsiyosiy/', AllContentView.as_view()),
    path('all_newijtimoiy/', allContentView.as_view()),
    path('Sdetail/<int:content_id>/',SDetailContentView.as_view()),
    path('Idetail/<int:content_id>/',IDetailContentView.as_view()),
    path('Screate/',SCreateContentView.as_view()),
    path('Icreate/',ICreateContentView.as_view()),
    path('Supdate/<int:content_id>/',SUpdateContentView.as_view()),
    path('Iupdate/<int:content_id>/',IUpdateContentView.as_view()),
    path('Sdelete/<int:content_id>/',SDeleteContentView.as_view()),
    path('Idelete/<int:content_id>/',IDeleteContentView.as_view())
]