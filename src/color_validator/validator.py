import re

_COLOR_RE = re.compile(
    r"(?P<hex>#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?:[0-9a-fA-F]{2})?\b)|"
    r"rgba?\(\s*(?P<r>\d{1,3})\s*,\s*(?P<g>\d{1,3})\s*,\s*(?P<b>\d{1,3})\s*(?:,\s*(?P<a>\d*\.?\d+)\s*)?\)",
    re.IGNORECASE
)

def is_valid_color(color: str) -> bool:
    match = _COLOR_RE.fullmatch(color.strip())
    if not match:
        return False

    if match.group("r"):
        r, g, b = int(match.group("r")), int(match.group("g")), int(match.group("b"))
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False
        if match.group("a"):
            a = float(match.group("a"))
            if not (0.0 <= a <= 1.0):
                return False
    return True

def find_colors(text: str) -> list[str]:
    results = []
    for match in _COLOR_RE.finditer(text):
        color_str = match.group(0)
        if is_valid_color(color_str):
            results.append(color_str)
    return results


def _interactive() -> None:
    print("Поиск цветов CSS")
    print("1 - Проверить один цвет")
    print("2 - Найти цвета в файле")
    print("3 - Найти цвета на сайте")

    choice = input("Выберите режим: ").strip()

    try:
        if choice == "1":
            color = input("Введите цвет: ").strip()
            if is_valid_color(color):
                print("Результат: Цвет корректен.")
            else:
                print("Результат: Цвет некорректен.")

        elif choice == "2":
            path = input("Введите путь к файлу: ").strip()
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            colors = find_colors(text)
            print(f"Найдено цветов: {len(colors)}")
            for c in colors:
                print(" -", c)

        elif choice == "3":
            import requests
            url = input("Введите URL (http://...): ").strip()
            response = requests.get(url, timeout=10)
            colors = find_colors(response.text)
            print(f"Найдено цветов: {len(colors)}")
            for c in colors[:5]:
                print(" -", c)
        else:
            print("Неверный выбор.")

    except Exception as exc:
        print(f"Ошибка: {exc}")

if __name__ == "__main__":
    _interactive()