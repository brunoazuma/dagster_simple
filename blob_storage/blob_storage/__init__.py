from dagster import (
    AssetSelection,
    Definitions,
    EnvVar,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)
from dagster_aws.s3 import ConfigurablePickledObjectS3IOManager, S3Resource

from . import assets
from .resources import IBGE_api
from .io import postgres_pandas_io_manager

all_assets = load_assets_from_modules([assets])

municipios_job = define_asset_job("municipios_job", selection=AssetSelection.all())

municipios_schedule = ScheduleDefinition(
    job=municipios_job, cron_schedule="*/10 * * * *"  # every 10 minutes
)

ibge_api = IBGE_api()

db_io_manager = postgres_pandas_io_manager.configured(
    {
        'server': {'env': 'SILVER_DB_HOST'},
        'db': {'env': 'SILVER_DB_NAME'},
        'uid': {'env': 'SILVER_DB_USER'},
        'pwd': {'env': 'SILVER_DB_PASSWORD'},
        'port': {'env': 'SILVER_DB_PORT'},
    }
)

defs = Definitions(
    assets=all_assets,
    schedules=[municipios_schedule],
    resources={
        "s3_io_manager": ConfigurablePickledObjectS3IOManager(
            s3_resource=S3Resource(
                endpoint_url=EnvVar('MINIO_ENDPOINT_URL'),
                aws_access_key_id=EnvVar('MINIO_ROOT_USER'),
                aws_secret_access_key=EnvVar('MINIO_ROOT_PASSWORD'),
                ), s3_bucket=EnvVar('MINIO_BUCKET_NAME')
        ),
        'ibge_api': ibge_api,
        'db_io_manager': db_io_manager
    },
)
