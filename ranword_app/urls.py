from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.random_word),
    path('reset', views.reset),
    # path('admin/', admin.site.urls),
]