import tkinter as tk
from tkinter import messagebox
from Python_Scripts.Daily_Reports_Scripts import dailyreports
from Python_Scripts.SOQ_full import soqreport
from Python_Scripts.SOQ_half import soqreporthalf

def daily_reports_cmd():
    dailyreports()
    messagebox.showinfo("Daily Reports", "Done!")
    
def soqreports_cmd():
    soqreport()
    messagebox.showinfo("SOQ Reports", "Done!")
    
def soqreportshalf_cmd():
    soqreporthalf()
    messagebox.showinfo("SOQ Reports-Half", "Done!")    


# Main App
root = tk.Tk()

# Dimensions of App
size = root.geometry("500x270")
title = root.title("All Reports")
root.configure(background='#006666')

# Label for Title
label = tk.Label(root, text="HOME DEPOT REPORTS PROGRAM",
                  font=("Gotham", 18, 'bold'),
                  fg='white', background='#006666', pady=10)
label.pack()

# Label Frame for Daily Report button organization
daily_label_frame = tk.LabelFrame(root, text="Daily Reports",
                                   padx=10, pady=20, font="Gotham",
                                   fg='white', background='#006666')
daily_label_frame.pack(side='right', padx=15, pady=5)

# Label Frame for SOQ button organization
soq_label_frame = tk.LabelFrame(root, text="SOQ Reports", 
                                padx=10, pady=10, font="Gotham", 
                                fg='white', background='#006666')
soq_label_frame.pack(side='left', padx=15, pady=5)

# Daily Reports Button
daily_reports_btn = tk.Button(daily_label_frame,text="Daily Reports", 
                              command=daily_reports_cmd, bg='#E76824', 
                              fg='white', padx=20, pady=10, 
                              font = ("Helvetica", 12, 'bold'))
daily_reports_btn.pack(padx=15, pady=25)

# SOQ Reports Button
soq_reports_btn = tk.Button(soq_label_frame,text="SOQ Reports", 
                            command=soqreports_cmd, bg='#E76824', 
                            fg='white', padx=30, pady=10, 
                            font = ("Helvetica", 12, 'bold'))
soq_reports_btn.pack(side='top',padx=10, pady=5,)

# Half Truck SOQ Reports Button
soq_reportshalf_btn = tk.Button(soq_label_frame,text="SOQ Reports-Half", 
                                command=soqreportshalf_cmd, bg='#E76824', 
                                fg='white', padx=30, pady=10, 
                                font = ("Helvetica", 12, 'bold'))
soq_reportshalf_btn.pack(side='bottom',padx=10, pady=5)

root.mainloop()

