import pandas as pd

df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B'],
                   'Values': [10, 15, 10, 20]})

df.groupby('Category').agg({'Values': ['sum', 'mean']})
