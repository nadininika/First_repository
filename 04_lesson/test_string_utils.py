import pytest
from StringUtils import StringUtils


# Создаём экземпляр класса
string_utils = StringUtils()


# Тесты для capitilize
def test_capitilize_positive():
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"


def test_capitilize_negative():
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize("123abc") == "123abc"


# Тесты для trim
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   ") == ""


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


# Тесты для contains
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "y") is True


def test_contains_negative():
    assert string_utils.contains("SkyPro", "X") is False
    assert string_utils.contains("", "X") is False


# Тесты для delete_symbol
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"


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


# Тесты для end_with
def test_end_with_positive():
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "Pro") is True


def test_end_with_negative():
    assert string_utils.end_with("SkyPro", "y") is False
    assert string_utils.end_with("", "o") is False


# Тесты для is_empty
def test_is_empty_positive():
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty("   ") is True


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
