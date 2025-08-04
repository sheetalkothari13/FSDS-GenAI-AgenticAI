# 🧮 Python Calculator

A comprehensive calculator application built with Python, featuring both a graphical user interface (GUI) and a command-line interface (CLI).

## 📋 Features

### GUI Calculator (`calculator.py`)
- **Modern Interface**: Clean, professional GUI built with tkinter
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: sin, cos, tan, log, ln, square root, square, cube
- **Special Functions**: Percentage, negation, clear all, clear entry
- **History Display**: Shows previous calculations
- **Error Handling**: Comprehensive error messages for invalid operations
- **Responsive Design**: Well-styled buttons with different colors for different functions

### Command-Line Calculator (`simple_calculator.py`)
- **Text-Based Interface**: Clean terminal interface
- **Expression Evaluation**: Supports complex mathematical expressions
- **Scientific Functions**: sqrt, sin, cos, tan (with degree input)
- **History Tracking**: Keeps track of last 20 calculations
- **Interactive Commands**: clear, history, help, quit
- **Error Handling**: Graceful error handling with informative messages

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python installation)

### Setup
1. **Clone or download the project files**
2. **No additional installation required** - all dependencies are built-in!

## 🎯 Usage

### GUI Calculator
```bash
python calculator.py
```

**Features:**
- Click buttons to input numbers and operations
- Use scientific functions for advanced calculations
- View calculation history in real-time
- Clear functions: 'C' (clear all) and 'CE' (clear entry)
- Percentage and negation operations

### Command-Line Calculator
```bash
python simple_calculator.py
```

**Features:**
- Type mathematical expressions directly
- Use scientific functions like `sqrt(16)`, `sin(30)`, `cos(45)`
- View calculation history with `history` command
- Get help with `help` command
- Clear screen with `clear` command

## 📖 Examples

### GUI Calculator Operations
1. **Basic Arithmetic**: Click numbers and operators
   - `5 + 3 = 8`
   - `10 × 4 = 40`
   - `15 ÷ 3 = 5`

2. **Scientific Functions**:
   - `sin(30)` → 0.5
   - `√(16)` → 4
   - `5²` → 25
   - `log(100)` → 2

### Command-Line Calculator Examples
```bash
Enter calculation: 2 + 3 * 4
✅ Result: 14

Enter calculation: sqrt(16)
✅ Result: 4

Enter calculation: sin(30)
✅ Result: 0.5

Enter calculation: 5 ** 2
✅ Result: 25

Enter calculation: 10 / 3
✅ Result: 3.333333
```

## 🎨 GUI Calculator Interface

The GUI calculator features a modern design with:

- **Display Area**: Large, readable display for current number and history
- **Number Buttons**: Gray buttons for digits 0-9 and decimal point
- **Operator Buttons**: Orange buttons for +, -, ×, ÷, =
- **Scientific Buttons**: Blue buttons for scientific functions
- **Clear Buttons**: Red buttons for C (clear all) and CE (clear entry)
- **Special Buttons**: Percentage and negation functions

## 🔧 Technical Details

### GUI Calculator (`calculator.py`)
- **Framework**: tkinter with ttk widgets
- **Architecture**: Object-oriented design with Calculator class
- **Styling**: Custom button styles with different colors
- **State Management**: Tracks current number, operation, and calculation state
- **Error Handling**: Try-catch blocks with user-friendly error messages

### Command-Line Calculator (`simple_calculator.py`)
- **Interface**: Pure Python with os module for screen clearing
- **Expression Parsing**: Uses Python's eval() with safety checks
- **History Management**: Maintains list of recent calculations
- **Input Validation**: Handles various input formats and errors
- **Command System**: Built-in commands for calculator control

## 🛠️ Customization

### Adding New Functions
To add new scientific functions to the GUI calculator:

1. Add button to the buttons list in `create_widgets()`
2. Add function logic in `scientific_function()` method
3. Update button styling if needed

### Modifying Styles
The GUI calculator uses ttk styles that can be customized:
- Number buttons: Gray background
- Operator buttons: Orange background
- Scientific buttons: Blue background
- Clear buttons: Red background

## 🐛 Troubleshooting

### Common Issues

1. **tkinter not found**
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install python3-tk
   
   # On macOS with Homebrew
   brew install python-tk
   
   # On Windows - usually comes with Python
   ```

2. **GUI not displaying properly**
   - Ensure your system supports tkinter
   - Try running with different Python version
   - Check display settings

3. **Command-line calculator issues**
   - Ensure you're using Python 3.6+
   - Check terminal encoding settings
   - Try running with `python3` instead of `python`

## 📁 Project Structure

```
calculator/
├── calculator.py           # GUI Calculator
├── simple_calculator.py    # Command-Line Calculator
├── requirements.txt        # Dependencies (optional)
└── README.md              # This file
```

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new mathematical functions
- Improving the user interface
- Adding unit tests
- Enhancing error handling
- Adding new features like memory functions
- Improving documentation

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Enjoy Calculating!

Both calculators are designed to be user-friendly and powerful. The GUI calculator is perfect for everyday use with its intuitive interface, while the command-line calculator is great for quick calculations and scripting.

---

**Happy Calculating! 🧮✨** 