from django.urls import path
from journal import views
from . import views

urlpatterns = [
    path('', views.write, name="write"),
    path('note_list/', views.note_list, name="note_list"),

    # path('new/', views.contact_create, name="contact_new"),
    path('note/<int:id>/edit', views.note_update, name="note_update"),
    # path('<int:id>/', views.show, name="contact_show"),
    # path('delete/<int:id>', views.contact_delete, name='contact_delete'),
    # path('gifts', views.contact_gift_list, name="contact_gift_list"),
    # path('<int:id>/gift/new/', views.contact_gift_create, name="contact_gift_new"),
    # path('upload-csv/', views.contact_upload, name="contact_upload"),

]