from dagster import Definitions, load_assets_from_modules

from .assets import mongodb
from dagster_embedded_elt.dlt import DagsterDltResource

monogdb_assets = load_assets_from_modules([mongodb])

defs = Definitions(
    assets=[*monogdb_assets],
    resources={"dlt": DagsterDltResource()},
)
