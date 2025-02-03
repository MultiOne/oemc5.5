import psycopg2


def load_data(file_path, table_name, connection_string) -> None:
    with psycopg2.connect(connection_string) as conn:
        with conn.cursor() as cur:
            with open(file_path, "r") as f:
                cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)


def execute_sql_command(uri, command):
    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cur:
            cur.execute(command)
