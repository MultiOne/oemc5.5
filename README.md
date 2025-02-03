### Project setup

---

- install `uv` tool:
  - https://docs.astral.sh/uv/getting-started/installation/
#### from project root

```uv init```

```uv sync```

---

### Run script  import_csv_files.py

```uv run import_scv_files.py path/to/file.csv db_table_name```

### map to table mapping:

- BioTIMEQuery_24_06_2021.csv -> bio_time_query_24_06_2021
- obis_20230208.csv -> obis_20230208

Use it like this:

```python
python3 import_scv_files.py path/to/file/BioTIMEQuery_24_06_2021.csv bio_time_query_24_06_2021
```

```python
python3 import_scv_files.py path/to/file/obis_20230208.csv obis_20230208
```

### Schema correction

- use SCHEMA_CORRECTIONS_COMMANDS in /src/db/schema_corrections/ to add commands to list that will be executed one by one after data is loaded

### edge cases:

- cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)                                  │(1 row)
  psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type double precision: "Distance 20.4│
  4 x width of the blade 1.35"                                                                             │postgres=#
  CONTEXT:  COPY obis_20230208, line 7528, column samplesizevalue: "Distance 20.44 x width of the blade 1.3│
  5"
- cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)
  psycopg2.errors.InvalidDatetimeFormat: invalid input syntax for type timestamp: "2012-08-19T01:47:10/2012-08-20T19:39:03"
  CONTEXT:  COPY obis_20230208, line 244, column eventdate: "2012-08-19T01:47:10/2012-08-20T19:39:03"
- psycopg2.errors.DatetimeFieldOverflow: date/time field value out of range: "28/04/2003 0:00:00"          │     0
  HINT:  Perhaps you need a different "datestyle" setting.                                                 │(1 row)
  CONTEXT:  COPY obis_20230208, line 8423, column modified: "28/04/2003 0:00:00"
- cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)                                  │ count
  psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type double precision: "na"          │-------
  CONTEXT:  COPY obis_20230208, line 34902, column coordinateprecision: "na"
- psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "NA"                   │     0
  CONTEXT:  COPY obis_20230208, line 39689, column year: "NA"
- cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)                                  │
  psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "NA"                   │postgres=# drop table obis_20230208 ;
  CONTEXT:  COPY obis_20230208, line 39689, column month: "NA"
- psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type double precision: "reef crest"  │     0
  CONTEXT:  COPY obis_20230208, line 2202464, column minimumelevationinmeters: "reef crest"
- psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type double precision: "reef crest"  │     0
  CONTEXT:  COPY obis_20230208, line 2202464, column minimumdistanceabovesurfaceinmeters: "reef crest"
- cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)                                  │d, 13 removed, 25 recycled; write=2.868 s, sync=1.114 s, total=4.031 s; sync files=15, longest=0.285 s, a
  psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "#VALUE!"              │verage=0.075 s; distance=625166 kB, estimate=649769 kB; lsn=83/C766F200, redo lsn=83/A1AD2C50
  CONTEXT:  COPY obis_20230208, line 100199571, column startdayofyear: "#VALUE!"

---

### NPP data preparation

- coast_distance.py
  - Calculating minimum distance to coast on grid of 0.5° x 0.5°.
- test_coast_dist_calc.py
  - Testing of minimum distance calculation
- biotime_subset_npp.py
  - Downloading of npp data
  - Calculating statistics per year
  - Calculating timeseries
  - Joining with bathymetry data
  - Joining with distance to coast
