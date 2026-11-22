import pandas as pd

df = pd.read_csv("retail-france.csv")
print(df.head())

# 商品番号をキーとして、商品説明を値とする辞書を作る
goods_dict = dict(zip(df['商品番号'],df['商品説明']))
print(goods_dict['21883']) # 商品番号で商品説明を調べる

# 不要な商品番号を取り除く
df = df[df['商品番号']!='POST'] # 送料関連の項目を除いた内容に限定する

# 発注番号別の商品番号リストを作る
df_ts = df.groupby('発注番号', as_index=False).agg({'商品番号': list})

# 発注番号ごとに商品リストをcsvファイルに出力する
df_ts.to_csv("retail-transactions1.csv", index=False)


# 商品番号リストを作る
ts = df_ts['商品番号'].values
ts = [','.join(s) for s in ts]
ds = pd.Series(ts)
print(ds.head())

# 商品番号リストをcsvファイルに出力する
ds.to_csv("retail-transactions2.csv", header=False, index=False)
