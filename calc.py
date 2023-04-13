import tkinter as tk
import ipdb
# Define the calculator button colors and font
BG_COLOR = "#F5F5F5"
BUTTON_COLOR = "#E0E0E0"
FONT = ("Roboto", 28)

# Define the calculator layout and button labels
CALCULATOR_LAYOUT = [
    ["AC", "C", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="],
]


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg=BG_COLOR)
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.operation = None
        self.operand = None

        # Create the calculator display
        self.display = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=FONT,
            bg=BG_COLOR,
            fg="black",
            anchor="e",
            padx=20,
            pady=10,
            bd=0,
            highlightthickness=0,
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="news")

        # Create the calculator buttons
        for row, row_values in enumerate(CALCULATOR_LAYOUT, start=1):
            for col, button_label in enumerate(row_values):
                button = tk.Button(
                    self.root,
                    text=button_label,
                    font=FONT,
                    bg=BUTTON_COLOR,
                    fg="black",
                    bd=0,
                    highlightthickness=0,
                    command=lambda x=button_label: self.button_click(x),
                )
                button.grid(row=row, column=col, sticky="news")

        # Configure the rows and columns to expand when the window is resized
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    def button_click(self, button_label):
        """
        Handle button clicks and perform calculator operations.
        """
        ipdb.set_trace()
        if button_label.isdigit() or button_label == ".":
            if self.operation is None:
                if button_label == "." and "." in self.result_var.get():
                    # Don't allow multiple decimal points
                    return
                if self.result_var.get() == "0":
                    self.result_var.set(button_label)
                else:
                    self.result_var.set(self.result_var.get() + button_label)
            else:
                if button_label == "." and "." in self.operand:
                    # Don't allow multiple decimal points
                    return
                self.operand += " "+self.operation+" "+button_label
                self.result_var.set(self.operand)
        elif button_label == "C":
            self.result_var.set("0")
            self.operand = None
        elif button_label == "AC":
            self.result_var.set("0")
            self.operation = None
            self.operand = None
        elif button_label == "±":
            self.result_var.set(str(float(self.result_var.get()) * -1))
        elif button_label == "%":
            self.result_var.set(str(float(self.result_var.get()) / 100))
        elif button_label in ("+", "-", "x", "÷"):
            if self.operand is not None:
                self.button_click("=")
            self.operation = button_label
            self.operand = self.result_var.get()
            self.result_var.set(self.result_var.get()+" "+button_label)
        elif button_label == "=":
            if self.operation is None or self.operand is None:
                return
            self.operand = self.operand.split(self.operation)
            if self.operation == "+":
                result = float(self.operand) + float(self.result_var.get())
            elif self.operation == "-":
                result = float(self.operand) - float(self.result_var.get())
            elif self.operation == "x":
                result = float(self.operand[0]) * float(self.operand[-1])
            elif self.operation == "÷":
                result = float(self.operand) / float(self.result_var.get())
            # Don't allow division by zero
            if result == float('inf'):
                self.result_var.set("Error")
                self.operation = None
                self.operand = None
                return
            self.result_var.set(str(result))
            self.operation = None
            self.operand = None

    def run(self):
        """
        Run the calculator application.
        """
        self.root.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
