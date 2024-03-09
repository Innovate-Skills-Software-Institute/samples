import pandas as pd
import adbc_driver_postgresql.dbapi as dbapi

df = pd.DataFrame(
    [
        [1,2,3],
        [4,5,6],
    ],
    columns=['a','b','c']
)

uri = "postgresql://postgres:postgres@localhost/postgres"

with dbapi.connect(uri) as conn:
    # df.to_sql("pandas_table", conn, index=False)
    df2 = pd.read_sql("pandas_table", conn)
    print(df2)

