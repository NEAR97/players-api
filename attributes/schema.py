import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from attributes.models import Attribute, Vote

from .models import Attribute


class AttributeType(DjangoObjectType):
    class Meta:
        model = Attribute

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    attributes = graphene.List(AttributeType)
    votes = graphene.List(VoteType)

    def resolve_attributes(self, info, **kwargs):
        return Attribute.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


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
    posted_by = graphene.Field(UserType)

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
        user = info.context.user or None
        attribute = Attribute(name=name, country=country, birth=birth, age=age, club=club, position=position, nickname=nickname, height=height, weight=weight, jersey=jersey, posted_by=user,)
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
            jersey=attribute.jersey,
            posted_by=attribute.posted_by,
        )
        
class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    attribute = graphene.Field(AttributeType)

    class Arguments:
        attribute_id = graphene.Int()

    def mutate(self, info, attribute_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        attribute = Attribute.objects.filter(id=attribute_id).first()
        if not attribute:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            attribute=attribute,
        )

        return CreateVote(user=user, attribute=attribute)

class Mutation(graphene.ObjectType):
    create_link = CreateAttribute.Field()
    create_vote = CreateVote.Field()


#4
class Mutation(graphene.ObjectType):
    create_attribute = CreateAttribute.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

