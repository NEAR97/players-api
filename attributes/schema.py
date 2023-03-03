import graphene
from graphene_django import DjangoObjectType

from .models import Attribute


class AttributeType(DjangoObjectType):
    class Meta:
        model = Attribute


class Query(graphene.ObjectType):
    attributes = graphene.List(AttributeType)

    def resolve_attributes(self, info, **kwargs):
        return Attribute.objects.all()