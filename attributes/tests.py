from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.

from attributes.schema import schema
from attributes.models import Attribute

ATTRIBUTES_QUERY = '''
 {
   attributes {
     id
     name
     country
     birth
     age
     club
     position
     nickname
     height
     weight
     jersey
   }
 }
'''
class AttributeTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.attribute1 = mixer.blend(Attribute)
        self.attribute2= mixer.blend(Attribute)
        
    def test_attributes_query(self):
        response = self.query(
            ATTRIBUTES_QUERY
            )
        
        content = json.loads(response.content)
        #print (content)
        self.assertResponseNoErrors(response)
        print ("query attributes results")
        print (content)
        assert len(content['data']['attributes']) == 2

