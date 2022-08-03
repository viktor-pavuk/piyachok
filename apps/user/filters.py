from django.contrib.auth import get_user_model

from django_filters import rest_framework as filters

UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    email = filters.CharFilter(field_name='email', lookup_expr='istartswith')
    name = filters.CharFilter(field_name='profile__name', lookup_expr='istartswith')
    surname = filters.CharFilter(field_name='profile__surname', lookup_expr='istartswith')
    phone = filters.CharFilter(field_name='profile__phone', lookup_expr='iendswith')

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'surname', 'phone')
