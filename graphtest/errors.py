from graphene_django.views import GraphQLError

def db_connection_error():
    raise GraphQLError('DB Server not connected!')
