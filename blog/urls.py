from re import template
from unicodedata import name
from django.urls import path
from .views import PostDetailView#,PostListView
from django.conf import settings
from . import views

urlpatterns = [
    #path('', PostListView.as_view(template_name = "home.html"), name = 'home'),
    path('', views.home, name='home'),
    path('article/<int:pk>', PostDetailView.as_view(template_name = "article.html"), name = 'article'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
    path('search', views.search, name='search'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)