from django.contrib import admin
from django.urls import path, include, re_path

# swagger import
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.views.static import serve

# end swagger import

# swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Azamov Samandar",
        default_version='v1',
        description="Sadullaxon",
        terms_of_service="https://blog.iprogrammer.uz",
        contact=openapi.Contact(email="azamov.samandar.programmer@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
# end swagger settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls")),
    path('accounts/', include("djoser.urls")),
    path('accounts/', include("djoser.urls.authtoken")),
    path('payme/', include("paymeapp.urls")),
    path('services/', include("servicesapp.urls")),
    path('order/', include("orderapp.urls")),
    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_URL}),
]

# swagger urls
swagger_urls = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns.extend(swagger_urls)
# end swagger urls
