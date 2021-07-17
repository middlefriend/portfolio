from django.contrib import admin
from django.urls import include, path,re_path
from rest_framework import routers,permissions
from cosmetic_analyze import views
#drf_yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings



#drf_view
schema_view = get_schema_view( 
    openapi.Info( 
        title="Comento DRF Swagger API", 
        default_version="v1", 
        description="4weeks API 문서", 
        terms_of_service="https://www.comento.kr", 
        contact=openapi.Contact(name="test", email="test@test.com"), 
        license=openapi.License(name="Test License"), 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'cosmetics', views.CosmeticViewSet)
router.register(r'categorys', views.CategoryViewSet)
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
