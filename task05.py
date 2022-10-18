WINTER_SEASON = "winter"


def find_season(month):
    if (isinstance(month, bool)
            or not isinstance(month, int)
            or not (1 <= month <= 12)):
        return -1

    season = "spring"

    if 2 >= month >= 1 or month == 12:
        season = WINTER_SEASON
    elif 8 >= month >= 6:
        season = "summer"
    elif 11 >= month >= 9:
        season = "autumn"
    return season


if __name__ == "__main__":
    assert find_season("10") == -1
    assert find_season(7.5) == -1
    assert find_season(True) == -1
    assert find_season(None) == -1
    assert find_season([1, 2, 3]) == -1

    assert find_season(1) == WINTER_SEASON
    assert find_season(2) == WINTER_SEASON
    assert find_season(12) == WINTER_SEASON
    assert find_season(3) == "spring"
    assert find_season(4) == "spring"
    assert find_season(5) == "spring"
    assert find_season(6) == "summer"
    assert find_season(7) == "summer"
    assert find_season(7) == "summer"
    assert find_season(9) == "autumn"
    assert find_season(10) == "autumn"
    assert find_season(11) == "autumn"
