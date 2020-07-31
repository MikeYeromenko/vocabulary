from django.urls import path

from vocabulary import views

app_name = 'vocabulary'

urlpatterns = [
    path('', views.WordListView.as_view(), name='show_all'),
    path('add/', views.add_word, name='add_word'),
    path('study/', views.study, name='study'),
    # path('test/', views.test, name='test'),
    path('test/<int:pk>', views.test, name='test'),
]
