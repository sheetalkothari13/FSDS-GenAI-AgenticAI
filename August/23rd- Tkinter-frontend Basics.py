import tkinter as tk

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("400x300")

def say_hello():
    print("Hello, World!")
    print("This is a Tkinter application.")
    print("Good Bye")

hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20)

root.mainloop()