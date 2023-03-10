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

#1
class CreateAttribute(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    country = graphene.String()
    birth = graphene.String()
    age = graphene.String()
    club = graphene.String()
    position = graphene.String()
    nickname = graphene.String()
    height = graphene.String()
    weight = graphene.String()
    jersey = graphene.String()

    #2
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        country = graphene.String()
        birth = graphene.String()
        age = graphene.String()
        club = graphene.String()
        position = graphene.String()
        nickname = graphene.String()
        height = graphene.String()
        weight = graphene.String()
        jersey = graphene.String()

    #3
    def mutate(self, info, name, country, birth, age, club, position, nickname, height, weight, jersey):
        attribute = Attribute(name=name, country=country, birth=birth, age=age, club=club, position=position, nickname=nickname, height=height, weight=weight, jersey=jersey)
        attribute.save()

        return CreateAttribute(
            id=attribute.id,
            name=attribute.name,
            country=attribute.country,
            birth=attribute.birth,
            age=attribute.age,
            club=attribute.club,
            position=attribute.position,
            nickname=attribute.nickname,
            height=attribute.height,
            weight=attribute.weight,
            jersey=attribute.jersey
        )


#4
class Mutation(graphene.ObjectType):
    create_attribute = CreateAttribute.Field()