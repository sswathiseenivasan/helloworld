import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Set the title of the window
root.title("Hello World Label")

# Create a label widget with text "Hello, World!"
label = tk.Label(root, text="Hello, World!")

# Pack the label widget into the window
label.pack()

# Start the tkinter event loop
root.mainloop()
