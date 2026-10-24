from django.urls import path

from apps.account.views.front import AuthView

app_name = "account_front"

urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
]
