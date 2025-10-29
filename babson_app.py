import tkinter as tk
from tkinter import ttk, messagebox
from babsondijkstra import graph, dijkstra

# Average human walking speed: 186 feet/minute
FEET_PER_MINUTE = 186

def find_path():
    start = start_var.get()
    end = end_var.get()

    if start == end:
        messagebox.showinfo("Result", "You selected the same start and end point.")
        return

    distances, previous = dijkstra(graph, start)
    if distances[end] == float("inf"):
        messagebox.showerror("Error", "No path found between these buildings.")
        return
        
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    total_feet = distances[end]
    total_minutes = round(total_feet / FEET_PER_MINUTE, 2)

    result = f"Path: {' → '.join(path)}\nTotal Distance: {total_feet} ft\nEstimated Time: {total_minutes} min"
    output_label.config(text=result)

# --- GUI setup ---
root = tk.Tk()
root.title("Babson Path Finder")
root.geometry("450x300")

title = tk.Label(root, text="Babson Path Finder", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

frame = ttk.Frame(root)
frame.pack(pady=10)

buildings = sorted(graph.keys())

tk.Label(frame, text="Start:").grid(row=0, column=0, padx=5, pady=5)
start_var = tk.StringVar()
start_menu = ttk.Combobox(frame, textvariable=start_var, values=buildings, width=30)
start_menu.grid(row=0, column=1)

tk.Label(frame, text="End:").grid(row=1, column=0, padx=5, pady=5)
end_var = tk.StringVar()
end_menu = ttk.Combobox(frame, textvariable=end_var, values=buildings, width=30)
end_menu.grid(row=1, column=1)

find_button = ttk.Button(root, text="Find Shortest Path", command=find_path)
find_button.pack(pady=10)

output_label = tk.Label(root, text="", wraplength=400, justify="left", font=("Helvetica", 11))
output_label.pack(pady=10)

root.mainloop()
