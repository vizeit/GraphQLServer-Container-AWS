from graphql import graphql
from ariadne import make_executable_schema, load_schema_from_path
import sys
sys.path.append('.')
from GraphQLAPI.resolvers import resolvers
import pytest

schema = make_executable_schema(
        load_schema_from_path('./GraphQLAPI/Schemas/'), 
        resolvers)

@pytest.mark.asyncio
async def test_hello():
    result = await graphql(schema, "{hello}")
    assert result.data['hello'] == "Hello!"

@pytest.mark.asyncio
async def test_helloThere():
    result = await graphql(schema, "{helloThere}")
    assert result.data['helloThere'] == "Hello There!"

    
    