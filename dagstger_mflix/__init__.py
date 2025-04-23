from dagster import Definitions, load_assets_from_modules
from .resources import dlt_resource, snowflake_resource
from .assets import mongodb, movies

monogdb_assets = load_assets_from_modules([mongodb], group_name="mongodb")
movies_assets = load_assets_from_modules([movies], group_name="movies")

defs = Definitions(
    assets=[*monogdb_assets, *movies_assets],
    resources={
        "dlt": dlt_resource,
        "snowflake": snowflake_resource
    },
)
