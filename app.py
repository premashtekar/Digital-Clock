import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x250")
root.configure(bg='black')

# Create time label
time_label = tk.Label(
    root,
    font=('Arial', 50, 'bold'),
    bg='black',
    fg='cyan'
)
time_label.pack(pady=30)

# Create date label
date_label = tk.Label(
    root,
    font=('Arial', 16),
    bg='black',
    fg='white'
)
date_label.pack()

def update_time():
    # Get current time and date
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    current_date = strftime('%A, %B %d, %Y')  # Full date
    
    # Update the labels
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Schedule next update
    root.after(1000, update_time)

# Start the clock
update_time()

# Run the application
root.mainloop()