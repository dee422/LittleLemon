# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'booking', views.BookingViewSet)

# urlpatterns = [  
#     path('home/', views.index, name='index'),  # 避免与 router.urls 冲突
#     path('', include(router.urls)),            # 自动路由 ViewSet
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

#     # 泛型视图 URL
#     path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
#     path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
# ]

# urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, UserViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]