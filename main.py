import tkinter as tk

window = tk.Tk()
window.minsize(width=350, height=300)
window.title('Miles To KM converter')
window.config(padx=100, pady=100)
# Label
empty_label = tk.Label(text='', font=('Arial', 10, 'bold'))
empty_label.grid(row=0, column=0)
label = tk.Label(text='Is Equal To:', font=('Arial', 15, 'bold'))
label.grid(row=2, column=1)

km_label = tk.Label(text='Km', font=('Arial', 15, 'bold'))
km_label.grid(row=2, column=3)

miles_label = tk.Label(text='Miles', font=('Arial', 15, 'bold'))
miles_label.grid(row=1, column=3)

km_value_label = tk.Label(text=0)
km_value_label.grid(row=2, column=2)

# Entry
miles_entry = tk.Entry(width=15, insertbackground='red')
miles_entry.grid(row=1, column=2)


# Button
def convert_to_km():
    try:
        km_value_label['text'] = 1.609 * int(miles_entry.get())
    except:
        print('Invalid value')


calculate_click = tk.Button(text='Calculate', command=convert_to_km, font=('Arial', 15, 'bold'))
calculate_click.grid(row=3, column=2)

window.mainloop()
