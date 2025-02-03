SQL_STATEMETS = [
    # Create the new table with the same schema
    "CREATE TABLE public.bio_time_query_clean AS TABLE public.bio_time_query_24_06_2021;",
    # day column
    "UPDATE public.bio_time_query_clean SET day = NULL WHERE day = 'NA';",
    "ALTER TABLE public.bio_time_query_clean ALTER COLUMN day TYPE INT USING (day::INT);",
    # month column
    "UPDATE public.bio_time_query_clean SET month = NULL WHERE month = 'NA';",
    "ALTER TABLE public.bio_time_query_clean ALTER COLUMN month TYPE INT USING (month::INT);",
    # year column
    "ALTER TABLE public.bio_time_query_clean ALTER COLUMN year TYPE INT USING (year::INT);"
    # geom column from lat and long columns
    "ALTER TABLE public.bio_time_query_clean ADD COLUMN geom geometry;",
    "UPDATE public.bio_time_query_clean SET geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);",
    "CREATE INDEX bio_time_geom_gist ON public.bio_time_query_clean USING GIST (geom);",
    # abundance column
    "UPDATE public.bio_time_query_clean SET abundance = NULL WHERE abundance = 'NA';",
    "ALTER TABLE public.bio_time_query_clean ALTER COLUMN abundance TYPE DOUBLE PRECISION USING abundance::DOUBLE PRECISION;",
    # biomass
    "UPDATE public.bio_time_query_clean SET biomass = NULL WHERE biomass = 'NA';",
    "ALTER TABLE public.bio_time_query_clean ALTER COLUMN biomass TYPE DOUBLE PRECISION USING biomass::DOUBLE PRECISION;",

    # clean columns from white space before moving into new table
    """
     UPDATE public.bio_time_query_clean
     SET genus = REGEXP_REPLACE(TRIM(genus), '\s+', ' ', 'g'),
        species = REGEXP_REPLACE(TRIM(species), '\s+', ' ', 'g'),
        genus_species = REGEXP_REPLACE(TRIM(genus_species), '\s+', ' ', 'g');
    """,

    """
    UPDATE public.bio_time_query_clean
    SET genus_species = TRIM(genus || ' ' || COALESCE(species, ''))
    WHERE TRIM(genus || ' ' || COALESCE(species, '')) <> genus_species;

    """,

    # create new table species
    """
    CREATE TABLE species (
    id SERIAL PRIMARY KEY,
    genus TEXT NOT NULL,
    species TEXT NULL,
    genus_species TEXT NOT NULL,
    CONSTRAINT unique_species_combination UNIQUE (genus, species, genus_species)
    );""",

    # move data to new table
    """
    INSERT INTO species (genus, species, genus_species)
    SELECT DISTINCT genus, COALESCE(species, NULL), genus_species
    FROM bio_time_query_clean;
    """,

    # add species table id column to bio_time_query_clean table
    "ALTER TABLE bio_time_query_clean ADD COLUMN species_id INTEGER;",

    # # connect rows from species table back to bio_time_query_clean
    """
    UPDATE bio_time_query_clean AS btc
    SET species_id = s.id
    FROM species AS s
    WHERE btc.species = s.species
      AND btc.genus = s.genus
      AND btc.genus_species = s.genus_species;
    """,

    # drop columns that are copied to species table
    """
    ALTER TABLE bio_time_query_clean
    DROP COLUMN species,
    DROP COLUMN genus,
    DROP COLUMN genus_species;
    """,
]

SQL_RESET = [
    "DROP TABLE IF EXISTS bio_time_query_clean;",
    "DROP TABLE IF EXISTS species;",
]
