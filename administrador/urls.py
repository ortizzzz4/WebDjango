from django.urls import path

from .import views

from .views import RegistroDetalle

app_name='administrador'

urlpatterns = [
    
   
    path('crear/', views.crear, name='crear'),
    #path('detalles/<int:id>', views.detalles, name='detalles'),
    path('detalles/<int:pk>', RegistroDetalle.as_view(template_name = "detalles.html"), name='detalles'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>' , views.eliminar, name='eliminar') ,
]
