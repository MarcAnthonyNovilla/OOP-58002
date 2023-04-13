import tkinter as tk


def fullname():
    fullname = f"{firstname.get()}{middlename.get()}{lastname.get()}"

    output.delete(0, tk.END)
    output.insert(0, fullname)


window = tk.Tk()
window.title("Midterm Exam Problem 2")

tk.Label(window, text="My FULL Name:").grid(row=0, column=2, padx=5, pady=5)

tk.Label(window, text="Enter Given Name:").grid(row=1, column=0, padx=5, pady=5)
firstname = tk.Entry(window)
firstname.grid(row=1, column=4, padx=10, pady=10)

tk.Label(window, text="Enter Middle Name:").grid(row=2, column=0, padx=5, pady=5)
middlename = tk.Entry(window)
middlename.grid(row=2, column=4, padx=10, pady=10)

tk.Label(window, text="Enter Last Name:").grid(row=3, column=0, padx=5, pady=5)
lastname = tk.Entry(window)
lastname.grid(row=3, column=4, padx=10, pady=10)

tk.Label(window, text="My FULL Name:").grid(row=4, column=0, padx=5, pady=5)
output = tk.Entry(window)
output.grid(row=4, column=4, padx=10, pady=10)

tk.Button(window, text="Show Full Name", command=fullname).grid(row=5, column=2, padx=10, pady=10)

window.mainloop()
