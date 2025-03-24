from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('certificates/', views.certificate_list, name='certificates'),
    path('certificates/delete/<int:certificate_id>/', views.delete_certificate, name='delete_certificate'),
    path('contact/', views.contact_view, name='contact'),

]


# 🔥 Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
