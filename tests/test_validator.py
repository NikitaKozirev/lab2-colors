from src.color_validator.validator import is_valid_color, find_colors

def test_all_valid_fixture_colors(valid_colors):
    for color in valid_colors:
        assert is_valid_color(color) is True, f"должен быть валидным: {color!r}"

def test_all_invalid_fixture_colors(invalid_colors):
    for color in invalid_colors:
        assert is_valid_color(color) is False, f"должен быть невалидным: {color!r}"

def test_find_colors_in_text():
    text = "Фон: #FFF, текст: rgb(255, 0, 0), рамка: #123456."
    expected = ["#FFF", "rgb(255, 0, 0)", "#123456"]
    assert find_colors(text) == expected

def test_find_ignores_invalid_rgb():
    text = "Ошибка: rgb(300, 0, 0) не должен найтись."
    assert find_colors(text) == []