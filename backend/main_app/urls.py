from django.urls import path
from .views.user_view import UserLoginView, UserRegistrationView
from .views.nomenclature_view import NomenclatureListView, NomenclatureDetailsView, NomenclatureCreateView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('nomenclature/list/', NomenclatureListView.as_view()),
    path('nomenclature/<int:pk>/', NomenclatureDetailsView.as_view()),
    path('nomenclature/create/', NomenclatureCreateView.as_view(),)
]
