from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from applications.construction_object.views import ConstructionListView, ConstructionDetailView, BlockView
from applications.history.views import HistoryListView
from applications.team_member.views import PartnerView

schema_view = get_schema_view(
    openapi.Info(
        title="Emark Group Web",
        default_version='v1',
        description="Emark Group Web Development",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += i18n_patterns(
    path('blocks/', BlockView.as_view()),
    path('construction/list/', ConstructionListView.as_view()),
    path('construction/<int:pk>/', ConstructionDetailView.as_view()),
    path('construction/<int:pk>/', include('applications.construction_object.urls')),
    path('history/', HistoryListView.as_view()),
    path('blog/', include('applications.news_blog.urls')),
    path('team/', include('applications.team_member.urls')),
    path('docs/', include('applications.document.urls')),
    path('conf/', include('applications.configuration.urls')),
    path('partners/', PartnerView.as_view())
)

admin.site.site_header = 'Emark Group'
admin.site.index_title = 'Администрация'
admin.site.site_title = 'Emark Group'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



