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
CREATE_ATTRIBUTE_MUTATION = '''
 mutation createAttributeMutation($name: String, $country: String, $birth: String, $age: String, $club: String, $position: String, $nickname: String, $height: String, $weight: String, $jersey: String) {
     createAttribute(name: $name, country: $country, birth: $birth, age: $age, club: $club, position: $position, nickname: $nickname, height: $height, weight: $weight, jersey: $jersey) {
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

def test_createAttribute_mutation(self):

        response = self.query(
            CREATE_ATTRIBUTE_MUTATION,
            variables={'name': 'messi', 'country': 'google', 'birth': '1978', 'age': '44', 'club': 'America','position': 'keeper', 'nickname': 'perro', 'height':'23','weight':'34', 'jersey':'120'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createAttribute" : {"name": "messi"}}, content['data'])
