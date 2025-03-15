from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.api.serializers import PostSerializerGet, PostSerializerPost
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from post.api.premissions import IsAdminOrReadOnly

# class PostApiView(APIView):
#     def get(self, request):
        
#         serializer = PostSerializerGet(Post.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PostSerializerPost(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializerGet(Post.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def create(self, request):
#         serializer = PostSerializerPost(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def retrieve(self, request, pk=None):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializerGet(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class PostModelViewSet(ModelViewSet):
    permission_classes =[IsAdminOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializerGet


    
    