from dagster import AssetCheckExecutionContext
from ..mongodb import mongodb 
import dlt
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets


mflix = mongodb(
    database='sample_mflix'
).with_resources(
    'comments',
    'embeded_movies'
)

