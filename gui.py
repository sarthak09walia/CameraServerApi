import subprocess 
import tkinter as tk 
from tkinter import messagebox 

def start_flask():
    try: 
        subprocess.Popen(["waitress-serve ", "--listen=*:5000","app:app"]) 
        messagebox.showinfo("Flask App", "Flask app started successfully!")

    except Exception as e: 
        messagebox.showerror("Error", f"Failed to start Flask app: {str(e)}")

def stop_flask():
    try:
        subprocess.run(["taskkill", "/f", "/im", "waitress-serve.exe"])
        messagebox.showinfo("Flask App", "Flask app stopped successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop Flask app: {str(e)}")
# Create the main window

root = tk.Tk() 
root.title("Camera Status App")
# Start Button
start_button = tk.Button(root, text="Start Flask", command=start_flask) 
start_button.pack(pady=10)
# Stop Button
stop_button = tk.Button(root, text="Stop Flask", command=stop_flask) 
stop_button.pack(pady=10)
# Run the GUI
root.mainloop()
