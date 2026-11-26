
#!/bin/bash
# SPDX-FileCopyrightText: 2026 Yudai Tsutsumida
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目のテスト失敗" >&2
    res=1
}

res=0

# 卵とご飯 → チャーハン
out=$(echo "卵 ご飯" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: チャーハン\n推定カロリー: 550 kcal')" ] || ng "$LINENO"

# 卵とパン → フレンチトースト
out=$(echo "卵 パン" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: フレンチトースト\n推定カロリー: 400 kcal')" ] || ng "$LINENO"

# パスタとベーコン → カルボナーラ
out=$(echo "パスタ ベーコン" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: カルボナーラ\n推定カロリー: 700 kcal')" ] || ng "$LINENO"

# じゃがいもと玉ねぎ → ポテトスープ
out=$(echo "じゃがいも 玉ねぎ" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: ポテトスープ\n推定カロリー: 250 kcal')" ] || ng "$LINENO"

# 鶏肉と玉ねぎ → 親子丼
out=$(echo "鶏肉 玉ねぎ" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: 親子丼\n推定カロリー: 600 kcal')" ] || ng "$LINENO"

# 該当する料理がない場合
out=$(echo "卵 牛乳" | python3 ../system01/system01.py) || ng "$LINENO"
[ "$out" = "$(printf 'おすすめ料理: 料理なし\n推定カロリー: 0 kcal')" ] || ng "$LINENO"

# 空入力の場合はエラー終了することを確認
python3 ../system01/system01.py </dev/null >/dev/null 2>/dev/null
[ "$?" -ne 0 ] || ng "$LINENO"

[ "$res" -eq 0 ] && echo "OK"

exit "$res"
