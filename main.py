import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.config(padx=100, pady=100)

sum_btn = tk.Button(text="+")
sum_btn.grid(column=3, row=0)

sub_btn = tk.Button(text="-")
sub_btn.grid(column=3, row=1)

multiply_btn = tk.Button(text="*")
multiply_btn.grid(column=3, row=2)

div_btn = tk.Button(text="/")
div_btn.grid(column=3, row=3)

equal_btn = tk.Button(text="=")
equal_btn.grid(column=3, row=4)

decimal_btn = tk.Button(text=".")
decimal_btn.grid(column=2, row=4)

invert_signal_btn = tk.Button(text="+/-")
invert_signal_btn.grid(column=0, row=4)

clear_btn = tk.Button(text="C")
clear_btn.grid(column=0, row=0)

clear_all_btn = tk.Button(text="CA")
clear_all_btn.grid(column=1, row=0)

zero_btn = tk.Button(text="0")
zero_btn.grid(column=1, row=4)

one_btn = tk.Button(text="1")
one_btn.grid(column=0, row=1)

two_btn = tk.Button(text="2")
two_btn.grid(column=1, row=1)

three_btn = tk.Button(text="3")
three_btn.grid(column=2, row=1)

four_btn = tk.Button(text="4")
four_btn.grid(column=0, row=2)

five_btn = tk.Button(text="5")
five_btn.grid(column=1, row=2)

six_btn = tk.Button(text="6")
six_btn.grid(column=2, row=2)

seven_btn = tk.Button(text="7")
seven_btn.grid(column=0, row=3)

eigth_btn = tk.Button(text="8")
eigth_btn.grid(column=1, row=3)

nine_btn = tk.Button(text="9")
nine_btn.grid(column=2, row=3)

window.mainloop()
