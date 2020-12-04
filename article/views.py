from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Category, Comment
from .permissions import PostPermission, IsPostAuthor, IsCommentAuthor
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, PostDetailsSerializer
from rest_framework import viewsets, generics


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['category', 'title', ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [PostPermission, IsPostAuthor]
        return [permissions() for permission in permissions]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [PostPermission, ]
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []

        else:
            permissions = [IsCommentAuthor, ]
        return [permission() for permission in permissions]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

















































# from rest_framework.generics import get_object_or_404
# from rest_framework.mixins import ListModelMixin
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from .models import Article
# from .serializers import ArticleSerializer
#
# class ArticleView(ListModelMixin, GenericAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
#     def post(self, request):
#         article = request.data.get("article")
#         # Create an article from the above data
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({
#             "success": "Article '{}' updated successfully".format(article_saved.title)
#         })



