import pytest
import sys
import os

# Add the src directory to the Python path to import caesar_encrypt
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from caesar_encrypt import caesar_encrypt


class TestCaesarEncrypt:
    """Test suite for the caesar_encrypt function."""
    
    def test_basic_lowercase_encryption(self):
        """Test basic encryption with lowercase letters."""
        assert caesar_encrypt("hello", 3) == "khoor"
        assert caesar_encrypt("world", 3) == "zruog"
        assert caesar_encrypt("abc", 1) == "bcd"
    
    def test_basic_uppercase_encryption(self):
        """Test basic encryption with uppercase letters."""
        assert caesar_encrypt("HELLO", 3) == "KHOOR"
        assert caesar_encrypt("WORLD", 3) == "ZRUOG"
        assert caesar_encrypt("ABC", 1) == "BCD"
    
    def test_mixed_case_encryption(self):
        """Test encryption with mixed case letters."""
        assert caesar_encrypt("Hello World", 3) == "Khoor Zruog"
        assert caesar_encrypt("PyThOn", 5) == "UdYmTs"
        assert caesar_encrypt("TeSt", 1) == "UfTu"
    
    def test_wrap_around_lowercase(self):
        """Test that lowercase letters wrap around correctly."""
        assert caesar_encrypt("xyz", 3) == "abc"
        assert caesar_encrypt("z", 1) == "a"
        assert caesar_encrypt("y", 2) == "a"
    
    def test_wrap_around_uppercase(self):
        """Test that uppercase letters wrap around correctly."""
        assert caesar_encrypt("XYZ", 3) == "ABC"
        assert caesar_encrypt("Z", 1) == "A"
        assert caesar_encrypt("Y", 2) == "A"
    
    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters remain unchanged."""
        assert caesar_encrypt("hello, world!", 3) == "khoor, zruog!"
        assert caesar_encrypt("123", 5) == "123"
        assert caesar_encrypt("!@#$%", 10) == "!@#$%"
        assert caesar_encrypt("", 3) == ""
    
    def test_spaces_and_punctuation(self):
        """Test that spaces and punctuation are preserved."""
        assert caesar_encrypt("hello world", 3) == "khoor zruog"
        assert caesar_encrypt("a.b,c;d:e", 1) == "b.c,d;e:f"
        assert caesar_encrypt("test-case_example", 2) == "vguv-ecug_gzcorng"
    
    def test_zero_shift(self):
        """Test that zero shift returns the original text."""
        assert caesar_encrypt("hello", 0) == "hello"
        assert caesar_encrypt("HELLO", 0) == "HELLO"
        assert caesar_encrypt("Hello World!", 0) == "Hello World!"
    
    def test_large_positive_shift(self):
        """Test that large shifts work correctly (should wrap around)."""
        assert caesar_encrypt("abc", 26) == "abc"  # 26 shifts = full alphabet
        assert caesar_encrypt("abc", 27) == "bcd"  # 27 shifts = 1 shift
        assert caesar_encrypt("xyz", 29) == "abc"  # 29 shifts = 3 shifts
    
    def test_negative_shift(self):
        """Test that negative shifts work correctly."""
        assert caesar_encrypt("def", -3) == "abc"
        assert caesar_encrypt("abc", -1) == "zab"
        assert caesar_encrypt("ABC", -1) == "ZAB"
    
    def test_large_negative_shift(self):
        """Test that large negative shifts work correctly."""
        assert caesar_encrypt("abc", -26) == "abc"  # -26 shifts = full alphabet
        assert caesar_encrypt("abc", -27) == "zab"  # -27 shifts = -1 shift
        assert caesar_encrypt("def", -29) == "abc"  # -29 shifts = -3 shifts
    
    def test_empty_string(self):
        """Test that empty string returns empty string."""
        assert caesar_encrypt("", 1) == ""
        assert caesar_encrypt("", 0) == ""
        assert caesar_encrypt("", -5) == ""
    
    def test_single_character(self):
        """Test encryption of single characters."""
        assert caesar_encrypt("a", 1) == "b"
        assert caesar_encrypt("A", 1) == "B"
        assert caesar_encrypt("z", 1) == "a"
        assert caesar_encrypt("Z", 1) == "A"
        assert caesar_encrypt("1", 5) == "1"
    
    def test_numbers_and_symbols(self):
        """Test that numbers and symbols are preserved."""
        assert caesar_encrypt("test123!@#", 5) == "yjxy123!@#"
        assert caesar_encrypt("a1b2c3", 2) == "c1d2e3"
        assert caesar_encrypt("x+y=z", 1) == "y+z=a"
    
    def test_all_alphabet_lowercase(self):
        """Test encryption of the entire lowercase alphabet."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        expected = "defghijklmnopqrstuvwxyzabc"
        assert caesar_encrypt(alphabet, 3) == expected
    
    def test_all_alphabet_uppercase(self):
        """Test encryption of the entire uppercase alphabet."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected = "DEFGHIJKLMNOPQRSTUVWXYZABC"
        assert caesar_encrypt(alphabet, 3) == expected
    
    def test_known_example_from_main(self):
        """Test the specific example from the main function."""
        assert caesar_encrypt("hello world", 3) == "khoor zruog"


# Parametrized tests for additional coverage
class TestCaesarEncryptParametrized:
    """Parametrized tests for caesar_encrypt function."""
    
    @pytest.mark.parametrize("text,shift,expected", [
        ("a", 1, "b"),
        ("z", 1, "a"),
        ("A", 1, "B"),
        ("Z", 1, "A"),
        ("hello", 0, "hello"),
        ("test", 13, "grfg"),  # ROT13
        ("grfg", 13, "test"),  # ROT13 reverse
    ])
    def test_parametrized_cases(self, text, shift, expected):
        """Test various text and shift combinations."""
        assert caesar_encrypt(text, shift) == expected
    
    @pytest.mark.parametrize("shift", [26, 52, 78, 104])
    def test_multiple_alphabet_shifts(self, shift):
        """Test that multiples of 26 return original text."""
        text = "Hello World"
        assert caesar_encrypt(text, shift) == text
    
    @pytest.mark.parametrize("char", "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~")
    def test_special_characters_unchanged(self, char):
        """Test that special characters remain unchanged."""
        assert caesar_encrypt(char, 10) == char


if __name__ == "__main__":
    pytest.main([__file__])
