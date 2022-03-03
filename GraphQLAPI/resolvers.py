from ariadne import QueryType

query = QueryType()

@query.field("hello")
async def resolve_hello(_, info):
    return "Hello!"

@query.field("helloThere")
async def resolve_helloThere(_, info):
    return "Hello There!"

resolvers = [query]