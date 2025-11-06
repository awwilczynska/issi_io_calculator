"""
Simple calculator module.

This module provides a Calculator class for performing basic arithmetic operations
(addition, subtraction, multiplication, and division) and a main function for
interactive calculator usage.
"""

class Calculator:
    """
    A simple calculator class for basic arithmetic operations.
    """
    def __init__(self, op1: float, op2: float):
        """
        Initialize the Calculator with two operands.
        
        Args:
            op1 (float): The first operand.
            op2 (float): The second operand.
        """
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """
        Calculate the sum of the two operands.
        
        Returns:
            float: The sum of op1 and op2.
        """
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """
        Calculate the difference of the two operands.
        
        Returns:
            float: The result of op1 - op2.
        """
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """
        Calculate the product of the two operands.
        
        Returns:
            float: The product of op1 and op2.
        """
        return self.__op1 * self.__op2

    def divide(self) -> float:
        """
        Calculate the division of the two operands.
        
        Returns:
            float: The result of op1 / op2.
            
        Raises:
            ZeroDivisionError: If op2 is zero.
        """
        if self.__op2 == 0:
            raise ZeroDivisionError("Error: Division by zero")
        return self.__op1 / self.__op2

def main():
    """
    Main function that provides an interactive calculator interface.
    
    Prompts the user to select an operation and enter two numbers,
    then performs the calculation and displays the result.
    """
    print("Simple Calculator")
    print("Select operation:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            op1 = float(input("Enter first number: "))
            op2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter only numbers.")
            return
        if choice == '1':
            print(f"Result: {op1} + {op2} = ",  Calculator(op1, op2).sum())
        elif choice == '2':
            print(f"Result: {op1} - {op2} = ",  Calculator(op1, op2).subtract())
        elif choice == '3':
            print(f"Result: {op1} * {op2} = ",  Calculator(op1, op2).multiply())
        elif choice == '4':
            try:
                print(f"Result: {op1} / {op2} = ",  Calculator(op1, op2).divide())
            except ZeroDivisionError as e:
                print(e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
