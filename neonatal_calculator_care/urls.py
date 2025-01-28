from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from calculators import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bilirubin-calculator/', views.bilirubin_calculator, name='bilirubin_calculator'),
    path('medications-calculator/', views.medications_calculator, name='medications_calculator'),
    path('fluid-balance-calculator/', views.fluid_balance_calculator, name='fluid_balance_calculator'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
