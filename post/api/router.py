from rest_framework.routers import DefaultRouter
from post.api.views import PostModelViewSet

routes = DefaultRouter()

routes.register(prefix='posts', viewset=PostModelViewSet, basename='post')


