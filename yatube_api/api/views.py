from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post
from .serializers import CommentSerializer, FollowSerializer
from .serializers import GroupSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка сообществ и получение информации о сообществе по id."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Получение списка постов; создание, обновление, удаление постов.

    Пагинация возможна при указании параметров limit и offset.
    Обновить или удалить существующий пост может только автор поста.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            msg = 'У вас недостаточно прав для выполнения данного действия.'
            raise PermissionDenied(msg)
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            msg = 'У вас недостаточно прав для выполнения данного действия.'
            raise PermissionDenied(msg)
        instance.delete()


class CommentViewSet(PostViewSet):
    """Получение списка комментариев; CRUD операции для комментариев.

    Наследует PostViewSet с переопределением get_queryset & perform_update.
    Обновить / удалить существующий комментарий может только автор комментария.
    """

    serializer_class = CommentSerializer
    pagination_class = None

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post

    def get_queryset(self):
        post = self.get_post()
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowListCreate(generics.ListCreateAPIView):
    """Получение текущих подписок пользователя; создание новых подписок."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
