from django.urls import path
from .views import SignUpView, HomePageView, ProfileEditView, ProfilePageView



urlpatterns = [
    path('create/',SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('edit_profile/<int:pk>/', ProfileEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
]