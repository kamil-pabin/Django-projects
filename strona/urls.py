from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password-reset/',
            auth_views.PasswordResetView.as_view(
                template_name='registration/password_reset.html'
            ),
            name='password_reset'),
    path('password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='registration/password_reset_done.html'
            ),
            name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='registration/password_reset_confirm.html'
            ),
            name='password_reset_confirm'),
    path('password-reset-complete/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='registration/password_reset_complete.html'
            ),
            name='password_reset_complete'),

]