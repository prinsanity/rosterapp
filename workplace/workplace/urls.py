from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('table.urls')),  # Include the URLs from the 'table' app
]