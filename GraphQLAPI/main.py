from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from resolvers import resolvers

schema = make_executable_schema(
    load_schema_from_path('./Schemas/'), 
    resolvers)
    
app = GraphQL(schema, debug=True)
