
import polars as pl
import numpy as np

ROWS = 1_000_000

a = np.random.randint(0, 2**32, ROWS)
b = np.random.randint(0, 2**32, ROWS)
c = np.random.randint(0, 2**32, ROWS)
d = np.random.randint(0, 2**32, ROWS)
e = np.random.randint(0, 2**32, ROWS)
f = np.random.randint(0, 2**32, ROWS)
g = np.random.randint(0, 2**32, ROWS)

df = pl.DataFrame({'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g})
df.write_csv("outputs.txt", separator="\t", has_header=False)
