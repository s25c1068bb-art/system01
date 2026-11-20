# system01.py
# 冷蔵庫の材料から料理を提案するコマンド

ingredients = input("材料を入力してください: ")

ingredients = ingredients.replace("、", " ")
items = ingredients.split()

if "卵" in items and "ご飯" in items:
    print("おすすめ料理: チャーハン")

elif "卵" in items and "パン" in items:
    print("おすすめ料理: フレンチトースト")

elif "パスタ" in items and "ベーコン" in items:
    print("おすすめ料理: カルボナーラ")

elif "じゃがいも" in items and "玉ねぎ" in items:
    print("おすすめ料理: ポテトスープ")

elif "鶏肉" in items and "玉ねぎ" in items:
    print("おすすめ料理: 親子丼")

else:
    print("おすすめ料理が見つかりませんでした")