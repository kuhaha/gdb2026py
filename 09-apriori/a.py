import pandas as pd
df = pd.read_csv("retail-france.csv")
df = df[df['商品番号']!='POST'] # 送料関連の項目を除いた内容に限定する
df_ts = df.groupby('発注番号', as_index=False).agg({'商品番号': list})
ts = df_ts['商品番号'].values
ts = [','.join(s) for s in ts]
ds = pd.Series(ts)
ds.to_csv("retail-transactions.csv", header=False, index=False)