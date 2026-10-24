from django.urls import path

from apps.documents.views.front import IndexView

app_name = 'documents_front'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
