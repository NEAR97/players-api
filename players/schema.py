import graphene

import attributes.schema


class Query(attributes.schema.Query, graphene.ObjectType):
    pass

class Mutation(attributes.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

