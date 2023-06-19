from django.urls import path
from .views.user_view import UserLoginView, UserRegistrationView
from .views.provider_view import *
from .views.nomenclature_view import NomenclatureView
from .views.orders_view import OrdersView



urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('get_all_users/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('providers/', ProviderView.as_view()),
    path('providers/<int:pk>', ProviderView.as_view()),
    path('providers/contacts/create/', ContactsView.as_view()),
    path('providers/contacts/provider_<int:pk>', ContactsView.as_view()),
    path('providers/contacts/<int:pk>', ContactsView.as_view()),
    path('providers/contacts/create_link/', ContactLinkView.as_view()),
    path('providers/contacts/delete_link/', ContactLinkView.as_view()),
    path('providers/requisits/create/', RequisitsView.as_view()),
    path('providers/requisits/provider_<int:pk>', RequisitsView.as_view()),
    path('nomenclature/', NomenclatureView.as_view()),
    path('nomenclature/<int:pk>', NomenclatureView.as_view()),
    path('orders/', OrdersView.as_view()),
    path('orders/<int:pk>', OrdersView.as_view()),
]

