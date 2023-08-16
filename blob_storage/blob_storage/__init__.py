from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager,  # Update the imports at the top of the file to also include this
)

from . import assets
from .resources import IBGE_api
from .io import postgres_pandas_io_manager

all_assets = load_assets_from_modules([assets])

municipios_job = define_asset_job("municipios_job", selection=AssetSelection.all())

municipios_schedule = ScheduleDefinition(
    job=municipios_job, cron_schedule="*/10 * * * *"  # every 10 minutes
)

file_io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
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
        "file_io_manager": file_io_manager,
        'ibge_api': ibge_api,
        'db_io_manager': db_io_manager
    },
)
