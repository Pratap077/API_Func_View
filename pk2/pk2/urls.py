from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>', views.detail_view, name='detail'),
    path('list/', views.list_view, name='list'),

]
