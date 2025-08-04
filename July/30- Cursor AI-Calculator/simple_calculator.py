#!/usr/bin/env python3
"""
Simple Command Line Calculator
A basic calculator that runs in the terminal with a clean interface.
"""

import math
import os

class SimpleCalculator:
    def __init__(self):
        self.history = []
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display calculator header"""
        print("=" * 50)
        print("           🧮 SIMPLE CALCULATOR 🧮")
        print("=" * 50)
        print("Operations: +, -, *, /, **, sqrt, sin, cos, tan")
        print("Commands: 'clear', 'history', 'quit', 'help'")
        print("=" * 50)
    
    def display_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations in history.")
            return
        
        print("\n📚 Calculation History:")
        print("-" * 30)
        for i, calc in enumerate(self.history[-10:], 1):  # Show last 10 calculations
            print(f"{i}. {calc}")
        print("-" * 30)
    
    def add_to_history(self, expression, result):
        """Add calculation to history"""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 20:  # Keep only last 20 calculations
            self.history.pop(0)
    
    def calculate(self, expression):
        """Calculate the result of an expression"""
        try:
            # Replace mathematical symbols
            expression = expression.replace('×', '*').replace('÷', '/')
            expression = expression.replace('**', '**')  # Power operation
            
            # Handle special functions
            if 'sqrt(' in expression:
                expression = expression.replace('sqrt(', 'math.sqrt(')
            if 'sin(' in expression:
                expression = expression.replace('sin(', 'math.sin(math.radians(')
                expression = expression.replace(')', '))')
            if 'cos(' in expression:
                expression = expression.replace('cos(', 'math.cos(math.radians(')
                expression = expression.replace(')', '))')
            if 'tan(' in expression:
                expression = expression.replace('tan(', 'math.tan(math.radians(')
                expression = expression.replace(')', '))')
            
            # Evaluate the expression
            result = eval(expression)
            
            # Format result
            if isinstance(result, (int, float)):
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 6)
            
            return result
            
        except ZeroDivisionError:
            return "Error: Division by zero!"
        except ValueError as e:
            return f"Error: Invalid input - {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def show_help(self):
        """Display help information"""
        print("\n📖 HELP - Available Operations:")
        print("-" * 40)
        print("Basic Operations:")
        print("  + : Addition")
        print("  - : Subtraction")
        print("  * : Multiplication")
        print("  / : Division")
        print("  ** : Exponentiation")
        print("\nScientific Functions:")
        print("  sqrt(x) : Square root")
        print("  sin(x) : Sine (degrees)")
        print("  cos(x) : Cosine (degrees)")
        print("  tan(x) : Tangent (degrees)")
        print("\nExamples:")
        print("  2 + 3 * 4")
        print("  sqrt(16)")
        print("  sin(30)")
        print("  5 ** 2")
        print("\nCommands:")
        print("  clear : Clear screen")
        print("  history : Show calculation history")
        print("  help : Show this help")
        print("  quit : Exit calculator")
        print("-" * 40)
    
    def run(self):
        """Main calculator loop"""
        self.clear_screen()
        self.display_header()
        
        while True:
            try:
                # Get user input
                user_input = input("\nEnter calculation (or command): ").strip()
                
                # Handle commands
                if user_input.lower() == 'quit':
                    print("👋 Goodbye! Thanks for using the calculator!")
                    break
                elif user_input.lower() == 'clear':
                    self.clear_screen()
                    self.display_header()
                    continue
                elif user_input.lower() == 'history':
                    self.display_history()
                    continue
                elif user_input.lower() == 'help':
                    self.show_help()
                    continue
                elif not user_input:
                    continue
                
                # Calculate result
                result = self.calculate(user_input)
                
                # Display result
                if isinstance(result, str) and result.startswith("Error"):
                    print(f"❌ {result}")
                else:
                    print(f"✅ Result: {result}")
                    self.add_to_history(user_input, result)
                
            except KeyboardInterrupt:
                print("\n\n👋 Calculator interrupted. Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break

def main():
    """Main function to start the calculator"""
    print("Starting Simple Calculator...")
    calculator = SimpleCalculator()
    calculator.run()

if __name__ == "__main__":
    main() 