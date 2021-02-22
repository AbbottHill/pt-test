
import pandas as pd
import numpy as np
pd.set_option('expand_frame_repr', False)  # 当列太多时显示所有列
# pd.set_option('max_rows', 5)
# pd.set_option('max_rows', 5)

df = pd.DataFrame(np.random.randn(5, 5))

print(df)
print(df[[0, 1]].mean())
print(df[[0, 1]].mean(axis= 1).mean())