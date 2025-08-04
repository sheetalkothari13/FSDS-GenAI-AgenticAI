import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Calculator state
        self.current_number = ""
        self.first_number = 0
        self.operation = ""
        self.should_reset = False
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_frame = ttk.Frame(main_frame)
        display_frame.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.display = ttk.Entry(display_frame, textvariable=self.display_var, 
                                font=('Arial', 20), justify='right', state='readonly')
        self.display.grid(row=0, column=0, sticky=(tk.W, tk.E), ipady=10)
        
        # History display
        self.history_var = tk.StringVar()
        self.history_var.set("")
        
        history_label = ttk.Label(display_frame, textvariable=self.history_var, 
                                 font=('Arial', 10), foreground='gray')
        history_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Buttons configuration
        buttons = [
            # Row 1 - Scientific functions
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3),
            # Row 2 - More scientific functions
            ('log', 2, 0), ('ln', 2, 1), ('x²', 2, 2), ('x³', 2, 3),
            # Row 3 - Numbers and operations
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('÷', 3, 3),
            # Row 4
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('×', 4, 3),
            # Row 5
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
            # Row 6
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('+', 6, 3),
            # Row 7 - Clear and special functions
            ('C', 7, 0), ('CE', 7, 1), ('±', 7, 2), ('%', 7, 3),
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            button = self.create_button(main_frame, text, row, col)
            if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                button.configure(command=lambda t=text: self.add_number(t))
            elif text in ['+', '-', '×', '÷']:
                button.configure(command=lambda t=text: self.set_operation(t))
            elif text == '=':
                button.configure(command=self.calculate)
            elif text == 'C':
                button.configure(command=self.clear_all)
            elif text == 'CE':
                button.configure(command=self.clear_entry)
            elif text == '±':
                button.configure(command=self.negate)
            elif text == '%':
                button.configure(command=self.percentage)
            elif text in ['sin', 'cos', 'tan', 'log', 'ln', '√', 'x²', 'x³']:
                button.configure(command=lambda t=text: self.scientific_function(t))
        
        # Configure grid weights
        for i in range(8):
            main_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)
            display_frame.grid_columnconfigure(i, weight=1)
    
    def create_button(self, parent, text, row, col):
        """Create a styled button"""
        button = ttk.Button(parent, text=text, style='Calculator.TButton')
        button.grid(row=row, column=col, padx=2, pady=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure button style based on type
        if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            button.configure(style='Number.TButton')
        elif text in ['+', '-', '×', '÷', '=']:
            button.configure(style='Operator.TButton')
        elif text in ['C', 'CE']:
            button.configure(style='Clear.TButton')
        elif text in ['sin', 'cos', 'tan', 'log', 'ln', '√', 'x²', 'x³']:
            button.configure(style='Scientific.TButton')
        
        return button
    
    def add_number(self, number):
        """Add a number to the current display"""
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if number == '.' and '.' in self.current_number:
            return
        
        self.current_number += number
        self.display_var.set(self.current_number)
    
    def set_operation(self, op):
        """Set the operation to perform"""
        if self.current_number:
            if self.operation and not self.should_reset:
                self.calculate()
            
            self.first_number = float(self.current_number)
            self.operation = op
            self.history_var.set(f"{self.first_number} {op}")
            self.should_reset = True
    
    def calculate(self):
        """Perform the calculation"""
        if not self.current_number or not self.operation:
            return
        
        second_number = float(self.current_number)
        result = 0
        
        try:
            if self.operation == '+':
                result = self.first_number + second_number
            elif self.operation == '-':
                result = self.first_number - second_number
            elif self.operation == '×':
                result = self.first_number * second_number
            elif self.operation == '÷':
                if second_number == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = self.first_number / second_number
            
            # Update history
            self.history_var.set(f"{self.first_number} {self.operation} {second_number} = {result}")
            
            # Display result
            self.display_var.set(str(result))
            self.current_number = str(result)
            self.operation = ""
            self.should_reset = True
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def scientific_function(self, func):
        """Perform scientific calculations"""
        if not self.current_number:
            return
        
        number = float(self.current_number)
        result = 0
        
        try:
            if func == 'sin':
                result = math.sin(math.radians(number))
            elif func == 'cos':
                result = math.cos(math.radians(number))
            elif func == 'tan':
                result = math.tan(math.radians(number))
            elif func == 'log':
                if number <= 0:
                    messagebox.showerror("Error", "Cannot calculate log of non-positive number!")
                    return
                result = math.log10(number)
            elif func == 'ln':
                if number <= 0:
                    messagebox.showerror("Error", "Cannot calculate ln of non-positive number!")
                    return
                result = math.log(number)
            elif func == '√':
                if number < 0:
                    messagebox.showerror("Error", "Cannot calculate square root of negative number!")
                    return
                result = math.sqrt(number)
            elif func == 'x²':
                result = number ** 2
            elif func == 'x³':
                result = number ** 3
            
            # Update history
            self.history_var.set(f"{func}({number}) = {result}")
            
            # Display result
            self.display_var.set(str(result))
            self.current_number = str(result)
            self.should_reset = True
            
        except Exception as e:
            messagebox.showerror("Error", f"Scientific calculation error: {str(e)}")
    
    def clear_all(self):
        """Clear everything"""
        self.current_number = ""
        self.first_number = 0
        self.operation = ""
        self.should_reset = False
        self.display_var.set("0")
        self.history_var.set("")
    
    def clear_entry(self):
        """Clear current entry"""
        self.current_number = ""
        self.display_var.set("0")
    
    def negate(self):
        """Negate the current number"""
        if self.current_number:
            if self.current_number.startswith('-'):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
            self.display_var.set(self.current_number)
    
    def percentage(self):
        """Calculate percentage"""
        if self.current_number:
            number = float(self.current_number)
            result = number / 100
            self.history_var.set(f"{number}% = {result}")
            self.display_var.set(str(result))
            self.current_number = str(result)
            self.should_reset = True

def main():
    root = tk.Tk()
    
    # Configure styles
    style = ttk.Style()
    
    # Number button style
    style.configure('Number.TButton', 
                   font=('Arial', 12, 'bold'),
                   background='#f0f0f0',
                   foreground='#333333')
    
    # Operator button style
    style.configure('Operator.TButton',
                   font=('Arial', 12, 'bold'),
                   background='#ff9500',
                   foreground='white')
    
    # Clear button style
    style.configure('Clear.TButton',
                   font=('Arial', 12, 'bold'),
                   background='#ff3b30',
                   foreground='white')
    
    # Scientific button style
    style.configure('Scientific.TButton',
                   font=('Arial', 10, 'bold'),
                   background='#007aff',
                   foreground='white')
    
    # Default button style
    style.configure('Calculator.TButton',
                   font=('Arial', 12),
                   background='#e0e0e0',
                   foreground='#333333')
    
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 