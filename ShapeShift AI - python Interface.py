import tkinter as tk
from tkinter import messagebox
import math

class AreaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("ShapeShift AI")
    
        # Shape selection
        self.label = tk.Label(master, text="Select a shape:")
        self.label.pack()

        self.shape_var = tk.StringVar(value="Circle")
        self.shape_menu = tk.OptionMenu(master, self.shape_var, "Circle", "Rectangle", "Triangle", command=self.update_ui)
        self.shape_menu.pack()

        # Input fields
        self.input_frame = tk.Frame(master)
        self.input_frame.pack()

        self.radius_label = tk.Label(self.input_frame, text="Radius:")
        self.radius_label.grid(row=0, column=0)
        
        self.radius_entry = tk.Entry(self.input_frame)
        self.radius_entry.grid(row=0, column=1)

        self.length_label = tk.Label(self.input_frame, text="Length:")
        self.length_label.grid(row=1, column=0)
        
        self.length_entry = tk.Entry(self.input_frame)
        self.length_entry.grid(row=1, column=1)

        self.width_label = tk.Label(self.input_frame, text="Width:")
        self.width_label.grid(row=2, column=0)
        
        self.width_entry = tk.Entry(self.input_frame)
        self.width_entry.grid(row=2, column=1)

        self.base_label = tk.Label(self.input_frame, text="Base:")
        self.base_label.grid(row=3, column=0)
        
        self.base_entry = tk.Entry(self.input_frame)
        self.base_entry.grid(row=3, column=1)

        self.height_label = tk.Label(self.input_frame, text="Height:")
        self.height_label.grid(row=4, column=0)
        
        self.height_entry = tk.Entry(self.input_frame)
        self.height_entry.grid(row=4, column=1)

        # Calculate button
        self.calculate_button = tk.Button(master, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack()

    def update_ui(self, shape):
        """Update the UI based on the selected shape."""
        
        # Hide all input fields initially
        for widget in self.input_frame.winfo_children():
            widget.grid_remove()

        if shape == "Circle":
            # Show only radius input
            self.radius_label.grid(row=0, column=0)
            self.radius_entry.grid(row=0, column=1)

            # Clear other entries
            for entry in [self.length_entry, self.width_entry, self.base_entry, self.height_entry]:
                entry.delete(0, 'end')

            for label in [self.length_label, self.width_label, self.base_label, self.height_label]:
                label.grid_remove()

        elif shape == "Rectangle":
            # Show length and width inputs
            self.length_label.grid(row=0, column=0)
            self.length_entry.grid(row=0, column=1)

            self.width_label.grid(row=1, column=0)
            self.width_entry.grid(row=1, column=1)

            # Clear other entries
            for entry in [self.radius_entry, self.base_entry, self.height_entry]:
                entry.delete(0, 'end')

            for label in [self.radius_label, self.base_label, self.height_label]:
                label.grid_remove()

        elif shape == "Triangle":
            # Show base and height inputs
            self.base_label.grid(row=0, column=0)
            self.base_entry.grid(row=0, column=1)

            self.height_label.grid(row=1, column=0)
            self.height_entry.grid(row=1, column=1)

            # Clear other entries
            for entry in [self.radius_entry, self.length_entry, self.width_entry]:
                entry.delete(0, 'end')

            for label in [self.radius_label, self.length_label, self.width_label]:
                label.grid_remove()

    def calculate_area(self):
        """Calculate the area based on the selected shape."""
        
        shape = self.shape_var.get()
        
        try:
            if shape == "Circle":
                radius = float(self.radius_entry.get())
                area = math.pi * (radius ** 2)
                messagebox.showinfo("Area", f"The area of the circle is: {area:.2f}")

            elif shape == "Rectangle":
                length = float(self.length_entry.get())
                width = float(self.width_entry.get())
                area = length * width
                messagebox.showinfo("Area", f"The area of the rectangle is: {area:.2f}")

            elif shape == "Triangle":
                base = float(self.base_entry.get())
                height = float(self.height_entry.get())
                area = 0.5 * base * height
                messagebox.showinfo("Area", f"The area of the triangle is: {area:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculator(root)
    root.mainloop()
