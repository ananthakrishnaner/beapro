
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('student/',include('student.urls')),
    path('tutor/',include('tutor.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "BEAPRO Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to BEAPRO Admin Account"