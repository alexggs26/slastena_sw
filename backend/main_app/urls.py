from django.urls import path
from .views.user_view import UserLoginView, UserRegistrationView
from .views.provider_view import *



urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('providers/', ProviderView.as_view()),
    path('providers/<int:pk>', ProviderView.as_view()),
    path('providers/contacts/provider_<int:pk>/', ContactsView.as_view()),
    path('providers/requisits/provider_<int:pk>', RequisitsView.as_view()),
    path('get_all_users/', UserRegistrationView.as_view())
]

