from django.urls import path

from tube.views import VideoView, watch, SignUpView, logout_view
from tube.views import uploaded_stream_detail, main
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', main, name='main'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('upload/', VideoView.as_view(), name='upload_video'),
    path('watch/<int:video_id>/', watch, name='video_stream_detail'),
    path('<str:name>/', uploaded_stream_detail, name='video_stream'),
]
