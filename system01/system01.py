#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Yuudai
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
    ingredients = sys.argv[1:]

    if len(ingredients) == 0:
        print(
            "使い方: system01.py 材料1 材料2 ...",
            file=sys.stderr
        )
        sys.exit(1)

    dish, calorie = suggest_dish(ingredients)

    if calorie > 0:
        print(f"おすすめ料理: {dish}")
        print(f"推定カロリー: {calorie} kcal")
    else:
        print(dish)


if __name__ == "__main__":
    main()