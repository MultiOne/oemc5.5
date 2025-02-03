import os
import logging
from csv_files_import.utils.data_laoder import execute_sql_command
from obis_table_sql.sql_statements import SQL_STATEMENTS

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    DATABASE_URI = (
        f"postgresql://postgres:{os.environ.get('POSTGRES_BIODIVERSITY_PASSWORD', 'postgres')}@localhost:9998/postgres"
    )

    for command in SQL_STATEMENTS:
        logger.info("\n")
        logger.info(command)
        execute_sql_command(DATABASE_URI, command)

