from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product_detail/<int:id>/',views.ProductDetail.as_view(), name='product_detail'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('registration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    # path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('logout/',views.logouthandle, name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name ='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url ='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name = 'app/passwordchangedone.html'), name ='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/passwordreset.html' , form_class = MyPasswordResetForm ),name='password_reset'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



