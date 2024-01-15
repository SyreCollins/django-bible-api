from django.urls import path
from .views import BibleBookView

urlpatterns = [
    path('api/<str:book_name>/', BibleBookView.as_view()),
    path('api/<str:book_name>/<int:chapter_number>/', BibleBookView.as_view()),
    path('api/<str:book_name>/<int:chapter_number>/<int:verse_number>/', BibleBookView.as_view()),
]
