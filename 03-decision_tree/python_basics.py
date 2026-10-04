print("---変数、文字列---")
pi = 3.141592
r = 5
print(r * r * pi)  # 78.5398

greet = "こんにちは！"
greet += "お元気ですか？"
print(greet)
#'こんにちは！お元気ですか？'

greet = """
こんにちは！
お元気ですか？
"""
print(greet)
# こんにちは！
# お元気ですか？

name = "渡部"
print(f"{name}さん、こんにちは！")
# 渡部さん、こんにちは！

############################################

print("---リスト：定義、操作---")
data = [78, 84, 92, 55]
# 添え字は0から
print(data[0])  # 78
# 添え字に-1を指定すると最後の要素
print(data[-1])  # 55

# リストの連結
data2 = [72, 91]
all = data + data2
print(all)
# [78, 84, 92, 55 , 72, 91]

# 要素の置換，削除
all[3] = 75
print(all)
# [78, 84, 92, 75 , 72, 91]

del all[3]
print(all)
# [78, 84, 92, 72, 91]

print(all)
# [78, 84, 92, 72, 91]
print(all[2:4])
# [92, 72]

# コロン(:)の左右は省略可
print(all[2:])
# [92, 72, 91]

# リストの合計，最大値，最小値
print(sum(all))  # 417

# リストの長さ（サイズ）を求める
print(len(all))  # 5

# リストを並べ替える
all_sorted = sorted(all)
print(all)  # allは変わらない
# [78, 84, 92, 72, 91]
print(all_sorted)
# [72, 78, 84, 91, 92]

all.sort()  # allの順序が変わる
print(all)
# [72, 78, 84, 91, 92]

############################################

print("---タブル：定義、操作---")

record = (172, 69)
# record = 172, 69 でも可（括弧省略）
print(record)  # (172, 69)

print(f"身長{record[0]}cm, 体重{record[1]}kg")
# 身長172cm, 体重69kg

############################################

print("---辞書: 定義、操作---")

d = {"Tom": 23, "Bob": 19}
print(f"Bob is {d['Bob']} years old.")
# Bob is 19 years old.
d["Alice"] = 18
print(d)
# {'Tom': 23, 'Bob': 19, 'Alice': 18}

print("---集合：定義、操作---")

grades = ["S", "B", "A", "A", "C"]  # 重複要素をもつリスト
print(grades)
# ['S', 'B', 'A', 'A', 'C']
unique_grades = set(grades)
print(unique_grades)  # list(unique_grades)でリストに変換できる
# {'B', 'S', 'C', 'A'}


print("---リストの内包表記---")

odds = [2 * n + 1 for n in range(9)]
print(odds)
# [1, 3, 5, 7, 9, 11, 13, 15, 17]
odds = [n for n in range(1, 18) if n % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9, 11, 13, 15, 17]
