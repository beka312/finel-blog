from rest_framework.routers import DefaultRouter
# from main.views import ArticleViewSet
from article.views import PostViewSet

router = DefaultRouter()
router.register(r'articles', PostViewSet, basename='user')

urlpatterns = router.urls






# from django.urls import path
# from .views import ArticleView
#
# app_name = "articles"
#
# urlpatterns = [
#
#     path('articles/', ArticleView.as_view({'get': 'list'})),
#     path('articles/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
# ]