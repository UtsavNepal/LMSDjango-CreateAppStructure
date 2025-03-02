# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    
    path('api/', include('author.urls')),
    path('api/', include('book.urls')),
    path('api/', include('student.urls')),
    path('api/', include('transactions.urls')),
    path('api/', include('dashboard.urls')),
]
