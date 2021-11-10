from django.urls import path, include
from layout import views

urlpatterns = [
    path('computers-layout/', views.LayoutView.as_view()),
]