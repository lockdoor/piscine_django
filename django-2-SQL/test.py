import psycopg2 as psycopg

with psycopg.connect("dbname=djangotraining user=djangouser password=pnamnil42 host=localhost port=5432") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print (db_version)

