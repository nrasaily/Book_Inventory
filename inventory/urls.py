from django.urls import path

from . import views
urlpatterns = [
  #path('inventory/', inventory_view, name='inventory'),
  path('inventory/', views.InventoryListView.as_view(), name='inventory_page'),
  path('add_book/', views.AddBookView.as_view(), name='add_book'),
  path('edit_book/<int:pk>/', views.UpdateBookView.as_view(), name='edit_book'),
  path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name="delete_book"),
  path('search/', views.search_book_view, name='search_book'),
]