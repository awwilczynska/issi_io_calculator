"""
Test suite for Calculator class and main interactive function.

This module contains comprehensive tests for:
- Calculator class arithmetic operations
- Interactive main function with various user inputs
- Error handling and edge cases
"""

from calculator import Calculator, main
import pytest

# =============================================================================
# CALCULATOR CLASS UNIT TESTS
# =============================================================================
# Tests for individual Calculator class methods with various input combinations

class TestCalculatorArithmetic:
    """Test suite for Calculator class arithmetic operations."""
    
    def test_sum_positive_numbers(self):
        """Test addition with positive numbers."""
        assert Calculator(2.0, 3.111119).sum() == pytest.approx(5.111119)

    def test_sum_with_negative(self):
        """Test addition with mixed positive and negative numbers."""
        assert Calculator(2.71, -3.92).sum() == pytest.approx(-1.21)

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        assert Calculator(5.0, 3).subtract() == pytest.approx(2.0)

    def test_subtract_with_negative(self):
        """Test subtraction involving negative numbers."""
        assert Calculator(5.0, -3.0).subtract() == pytest.approx(8.0)

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        assert Calculator(2, 3.0).multiply() == pytest.approx(6.0)

    def test_multiply_with_zero(self):
        """Test multiplication with zero (edge case)."""
        assert Calculator(-2, 0.0).multiply() == pytest.approx(0.0)

    def test_divide_normal_operation(self):
        """Test normal division operation."""
        assert Calculator(6.0, 3.0).divide() == pytest.approx(2.0)

    def test_divide_by_zero_exception(self):
        """Test that division by zero raises appropriate exception."""
        with pytest.raises(ZeroDivisionError):
            Calculator(6, 0.0).divide()


# =============================================================================
# INTERACTIVE MAIN FUNCTION TESTS - VALID CHOICES
# =============================================================================
# Tests for main() function with valid operation choices (1-4)

class TestMainFunctionValidChoices:
    """Test suite for main() function with valid user choices."""
    
    def test_choice_1_addition(self, monkeypatch, capsys):
        """Test main function with choice '1' (addition operation)."""
        inputs = iter(['1', '10', '5'])  # Choice 1, then numbers 10 and 5
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: 10.0 + 5.0 =  15.0" in captured.out

    def test_choice_2_subtraction(self, monkeypatch, capsys):
        """Test main function with choice '2' (subtraction operation)."""
        inputs = iter(['2', '10', '3'])  # Choice 2, then numbers 10 and 3
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: 10.0 - 3.0 =  7.0" in captured.out

    def test_choice_3_multiplication(self, monkeypatch, capsys):
        """Test main function with choice '3' (multiplication operation)."""
        inputs = iter(['3', '4', '6'])  # Choice 3, then numbers 4 and 6
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: 4.0 * 6.0 =  24.0" in captured.out

    def test_choice_4_division(self, monkeypatch, capsys):
        """Test main function with choice '4' (division operation)."""
        inputs = iter(['4', '15', '3'])  # Choice 4, then numbers 15 and 3
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: 15.0 / 3.0 =  5.0" in captured.out


# =============================================================================
# INTERACTIVE MAIN FUNCTION TESTS - ERROR HANDLING
# =============================================================================
# Tests for error conditions and exception handling in main() function

class TestMainFunctionErrorHandling:
    """Test suite for main() function error handling scenarios."""
    
    def test_division_by_zero_handling(self, monkeypatch, capsys):
        """Test main function handles division by zero appropriately."""
        inputs = iter(['4', '10', '0'])  # Choice 4, then numbers 10 and 0
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Error: Division by zero" in captured.out

    def test_invalid_number_input(self, monkeypatch, capsys):
        """Test main function handles invalid number input gracefully."""
        inputs = iter(['1', 'abc', '5'])  # Choice 1, then invalid input 'abc'
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Invalid input. Please enter only numbers." in captured.out

# =============================================================================
# INTERACTIVE MAIN FUNCTION TESTS - EDGE CASES
# =============================================================================
# Tests for edge cases and special input scenarios

class TestMainFunctionEdgeCases:
    """Test suite for main() function edge cases and special scenarios."""
    
    def test_negative_numbers(self, monkeypatch, capsys):
        """Test main function with negative number inputs."""
        inputs = iter(['1', '-5', '3'])  # Choice 1, then numbers -5 and 3
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: -5.0 + 3.0 =  -2.0" in captured.out

    def test_decimal_numbers(self, monkeypatch, capsys):
        """Test main function with decimal number inputs."""
        inputs = iter(['2', '7.5', '2.5'])  # Choice 2, then numbers 7.5 and 2.5
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        
        captured = capsys.readouterr()
        assert "Simple Calculator" in captured.out
        assert "Result: 7.5 - 2.5 =  5.0" in captured.out


# =============================================================================
# INTERACTIVE MAIN FUNCTION TESTS - INVALID CHOICES
# =============================================================================
# Tests for invalid operation choices and input validation

class TestMainFunctionInvalidChoices:
    """Test suite for main() function invalid choice handling."""
    
    def test_invalid_choice_letter(self, monkeypatch, capsys):
        """Test that entering a letter choice shows appropriate error message."""
        monkeypatch.setattr('builtins.input', lambda _: 'a')
        
        main()
        
        captured = capsys.readouterr()
        assert "Invalid choice." in captured.out
        assert "Simple Calculator" in captured.out

    def test_invalid_choice_number_5(self, monkeypatch, capsys):
        """Test that entering choice '5' shows appropriate error message."""
        monkeypatch.setattr('builtins.input', lambda _: '5')
        
        main()
        
        captured = capsys.readouterr()
        assert "Invalid choice." in captured.out
        assert "Simple Calculator" in captured.out
        assert "Select operation:" in captured.out