from django.urls import path, include 
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('notes/delete/<int:pk>/', views.delete_note, name="delete_note"),
    path('notes_detail/<int:pk>/',views.NotesDetailView.as_view(),name="notes-detail"),  

    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name="update-homework"),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('homework/<int:homework_id>/', views.homework_detail, name='homework-detail'),


    path('youtube',views.youtube,name="youtube"),

    path('history/', views.history, name='history'),


    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),

    path('todo_details/<int:pk>/', views.todo_details, name='todo-details'),


    path('books',views.books,name="books"),


    path('dictionary',views.dictionary,name="dictionary"),  


    path('wiki',views.wiki,name="wiki"),


    path('conversion',views.conversion,name="conversion"),
    
]