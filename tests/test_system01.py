from system01.system01 import suggest_dish


def test_fried_rice():
    assert suggest_dish(["卵", "ご飯"]) == ("チャーハン", 550)


def test_french_toast():
    assert suggest_dish(["卵", "パン"]) == ("フレンチトースト", 400)


def test_unknown():
    assert suggest_dish(["りんご"]) == ("料理なし", 0)