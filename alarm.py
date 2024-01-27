import tkinter as tk
from tkinter import messagebox  # Import messagebox separately
from datetime import datetime, timedelta
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.label = tk.Label(root, text="Enter time (HH:MM):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.btn_set = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.btn_set.pack(pady=10)

    def set_alarm(self):
        alarm_time_str = self.entry.get()

        # Check if the input is empty
        if not alarm_time_str:
            messagebox.showerror("Error", "Please enter a time.")
            return

        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
            return

        current_time = datetime.now().time()
        current_datetime = datetime.combine(datetime.today(), current_time)
        alarm_datetime = datetime.combine(datetime.today(), alarm_time.time())

        time_difference = alarm_datetime - current_datetime

        if time_difference.total_seconds() < 0:
            messagebox.showerror("Error", "Invalid time. Please set a future time.")
            return

        self.root.after(int(time_difference.total_seconds() * 1000), self.play_alarm)

    def play_alarm(self):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        messagebox.showinfo("Alarm", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
