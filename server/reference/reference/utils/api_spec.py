"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Reference API",
    version="1.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Define schema
class OutputSchema(Schema):
    result = fields.Dict(description="A json object, containing key-value pairs of a symbol and its price", required=True)

# register schemas with spec
spec.components.schema("Output", schema=OutputSchema)
