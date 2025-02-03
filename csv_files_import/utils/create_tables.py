from sqlalchemy import create_engine
from csv_files_import.db.schema import Base


def create_tables(database_uri) -> None:
    """
    Function that create db tables (schema) if they do not exist.
    :return: None
    """
    db_engine = create_engine(database_uri)
    Base.metadata.create_all(db_engine)
