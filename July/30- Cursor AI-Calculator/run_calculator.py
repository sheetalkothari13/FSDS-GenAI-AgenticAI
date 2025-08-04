#!/usr/bin/env python3
"""
Calculator Launcher
A simple script to launch either the GUI or command-line calculator.
"""

import subprocess
import sys
import os

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        return True
    except ImportError:
        return False

def main():
    print("🧮 Python Calculator Launcher")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('calculator.py') or not os.path.exists('simple_calculator.py'):
        print("❌ Error: Calculator files not found!")
        print("Please run this script from the calculator directory.")
        return
    
    print("Choose your calculator:")
    print("1. 🖥️  GUI Calculator (Graphical Interface)")
    print("2. 💻 Command-Line Calculator (Terminal Interface)")
    print("3. ❌ Exit")
    print("-" * 40)
    
    while True:
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                if check_tkinter():
                    print("🚀 Starting GUI Calculator...")
                    subprocess.run([sys.executable, 'calculator.py'])
                else:
                    print("❌ Error: tkinter is not available!")
                    print("Please install tkinter or use the command-line calculator.")
                    print("\nTo install tkinter:")
                    print("  Ubuntu/Debian: sudo apt-get install python3-tk")
                    print("  macOS: brew install python-tk")
                    print("  Windows: Usually comes with Python")
                break
                
            elif choice == '2':
                print("🚀 Starting Command-Line Calculator...")
                subprocess.run([sys.executable, 'simple_calculator.py'])
                break
                
            elif choice == '3':
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            break

if __name__ == "__main__":
    main() 