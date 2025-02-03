import argparse
import time
import logging
from csv_files_import.utils.create_tables import create_tables
from csv_files_import.utils.data_laoder import load_data

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Load CSV file into PostGIS DB")
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument(
        "table_name", help="Name of the database table to load data into"
    )
    args = parser.parse_args()

    DATABASE_URI = "postgresql://postgres:postgres@localhost:9998/postgres"

    logger.info("Starting to create db tables...")
    create_tables(DATABASE_URI)
    logger.info("Tables created...")
    logger.info("Loading data...")
    load_data(args.file_path, args.table_name, DATABASE_URI)
    logger.info("Data loaded!")

    end_time = time.time()
    duration = end_time - start_time
    logger.info(f"Script executed in {duration:.2f} seconds")
