
#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Yudai Tsutsumida
# SPDX-License-Identifier: BSD-3-Clause

import sys


def suggest_dish(ingredients):
    """材料から料理とカロリーを返す"""

    if "卵" in ingredients and "ご飯" in ingredients:
        return "チャーハン", 550

    elif "卵" in ingredients and "パン" in ingredients:
        return "フレンチトースト", 400

    elif "パスタ" in ingredients and "ベーコン" in ingredients:
        return "カルボナーラ", 700

    elif "じゃがいも" in ingredients and "玉ねぎ" in ingredients:
        return "ポテトスープ", 250

    elif "鶏肉" in ingredients and "玉ねぎ" in ingredients:
        return "親子丼", 600

    else:
        return "料理なし", 0


def main():
    ingredients = sys.stdin.read().split()

    if len(ingredients) == 0:
        print("材料を入力してください", file=sys.stderr)
        sys.exit(1)

    dish, calorie = suggest_dish(ingredients)

    print(f"おすすめ料理: {dish}")
    print(f"推定カロリー: {calorie} kcal")


if __name__ == "__main__":
    main()
