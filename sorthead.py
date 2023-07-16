import polars as pl

ROWS = 100

df = pl.read_csv("outputs.txt", separator="\t", has_header=False)
# print(df.columns)
df = df.sort(pl.col("column_7")).head(ROWS)
print(df.write_csv(separator="\t", has_header=False))
