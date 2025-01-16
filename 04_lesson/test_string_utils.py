import pytest
from StringUtils import StringUtils

# Создаем экземпляр класса
string_utils = StringUtils()

# Тесты для capitilize
def test_capitilize_positive():
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"

def test_capitilize_negative():
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize("123abc") == "123abc"

def test_capitilize_non_string():
    with pytest.raises(AttributeError):  # Проверка на вызов с None
        string_utils.capitilize(None)
    with pytest.raises(AttributeError):  # Передача числового значения
        string_utils.capitilize(123)

# Тесты для trim
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   ") == ""
    assert string_utils.trim("\t skypro") == "skypro"  # С табуляцией
    assert string_utils.trim("\n skypro") == "skypro"  # С новой строкой

def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim("   ") == ""

# Тесты для to_list
def test_to_list_positive():
    assert string_utils.to_list("a,b,c") == ["a", "b", "c"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []

def test_to_list_negative():
    assert string_utils.to_list("abc", ",") == ["abc"]
    assert string_utils.to_list("123", ":") == ["123"]

def test_to_list_empty_delimiter():
    with pytest.raises(ValueError):  # Ожидаем исключение при пустом разделителе
        string_utils.to_list("abc", "")

# Тесты для contains
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "y") is True

def test_contains_negative():
    assert string_utils.contains("SkyPro", "X") is False
    assert string_utils.contains("", "X") is False

def test_contains_with_none():
    with pytest.raises(AttributeError):  # Проверка на None в строке
        string_utils.contains(None, "X")

# Тесты для delete_symbol
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "o") == "SkyPr"  # Удаление одного символа

def test_delete_symbol_multiple_occurrences():
    assert string_utils.delete_symbol("SkySkyProPro", "Pro") == "SkySky"
    assert string_utils.delete_symbol("aaa", "a") == ""

def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"
    assert string_utils.delete_symbol("", "X") == ""

# Тесты для starts_with
def test_starts_with_positive():
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "Sk") is True

def test_starts_with_negative():
    assert string_utils.starts_with("SkyPro", "P") is False
    assert string_utils.starts_with("", "S") is False

def test_starts_with_empty_symbol():
    assert string_utils.starts_with("SkyPro", "") is True  # Пустая строка как символ

# Тесты для end_with
def test_end_with_positive():
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "Pro") is True

def test_end_with_negative():
    assert string_utils.end_with("SkyPro", "y") is False
    assert string_utils.end_with("", "o") is False

def test_end_with_empty_symbol():
    assert string_utils.end_with("SkyPro", "") is True  # Пустая строка как символ

# Тесты для is_empty
def test_is_empty_positive():
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty("   ") is True
    assert string_utils.is_empty("\t") is True  # Строка с табуляцией

def test_is_empty_negative():
    assert string_utils.is_empty("SkyPro") is False
    assert string_utils.is_empty(" a ") is False

# Тесты для list_to_string
def test_list_to_string_positive():
    assert string_utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_negative():
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([1]) == "1"

def test_list_to_string_mixed_elements():
    assert string_utils.list_to_string([None, 1, "Test"]) == "None, 1, Test"
