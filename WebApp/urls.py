from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexPage,name='index'),
    path('works',WorksPage,name='works'),
    path('uses',UsesPage,name='uses'),
    path('personal-projects',ProjectsPage,name='projects'),
    path('wallpapers',WallpapersPage,name='wallpapers'),
    
    path("media/<path:path>",media_path),
    path("static/<path:path>",static_path),

]
