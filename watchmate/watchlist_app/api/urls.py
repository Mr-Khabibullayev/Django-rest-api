from django.urls import path,include
from watchlist_app.api.views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

 
urlpatterns = [
    path('list/',WatchlistAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-detail'),
    
    path('',include(router.urls)),
    
    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='stream-detail'),
    
    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create/'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    
] 
