import tkinter as tk
from tkinter import ttk

# Data dictionary mapping printing services to their details
printing_data = {
    "Screen printing": {
        "description": "Screen printing: plastic, metal, 1 color.",
        "options": [
            "Plastic Pens Screen Printing (Serigrafía)",
            "Metal Pens and USB Drives Screen Printing (Serigrafía or Tampografía)",
            "Plastic Items Screen Printing (Serigrafía)"
        ],
        "notes": "1. Prices are per unit and per color unless specified otherwise.\n"
                 "2. 'Matrix' refers to setup costs per color for screen printing.\n"
                 "3. 'Film' costs are for preparing the screens for printing."
    },
    "Pad printing": {"description": "Pad printing: curved plastic, eco-friendly.", "options": [
        "Pad Printing on Plastic and Curved Surfaces (including Ecological Items)",
        "Pad Printing on Stress Balls (1 Color, One Side)"
        ], 
        "notes": "Prices are per unit and per color unless specified otherwise."
                "\"Matrix\" refers to setup costs per color for pad printing."
                "Additional colors cost the same as the first color."
    },
    "Serigraphy": {"description": "Serigraphy: mugs, bottles, frisbees, beach balls, 1 color.", "options": [], "notes": ""},
    "Laser engraving": {"description": "Laser engraving: metal, wood, glass, customization.", "options": [], "notes": ""},
    "Textile printing": {"description": "Textile printing: bags, umbrellas, t-shirts, 1 color.", "options": [], "notes": ""},
    "Digital printing": {"description": "Digital printing: plastic bottles, sublimation bags, vinyl, logo size.", "options": [], "notes": ""}
}

plastic_pens_pricing = """
Quantity Range              | Price per Unit (1 Color)
----------------------------------------------------
1 - 100 units               | $30,000 pesos
101 - 500 units             | $25,000 pesos
501 - 1,000 units           | $25,000 pesos
1,001 - 5,000 units         | $25 pesos
5,001 - 10,000 units        | $20 pesos

* Matrix: $5,000 pesos per color.
* Additional colors cost the same as the first color.
"""

metal_pens_usb_pricing = """
Quantity Range              | Price per Unit (1 Color)
----------------------------------------------------
1 - 100 units               | $30,000 pesos
101 - 200 units             | $200 pesos
201 - 300 units             | $180 pesos
301 - 400 units             | $160 pesos
401 - 500 units             | $140 pesos
501 - 1,000 units           | $120 pesos

* Matrix: $5,000 pesos per color.
* Additional colors cost the same as the first color.
"""

plastic_items_pricing = """
Quantity Range              | Price per Unit (1 Color)
----------------------------------------------------
1 - 100 units               | $30,000 pesos
101 - 200 units             | $250 pesos
201 - 300 units             | $230 pesos
301 - 400 units             | $200 pesos
401 - 500 units             | $150 pesos
501 - 1,000 units           | $130 pesos
Over 1,000 units            | $100 pesos

* Film: $4,000 pesos per color.
* Additional colors cost the same as the first color.
"""

def show_details(event=None):
    selected_service = combo.get()
    if selected_service in printing_data:
        details = printing_data[selected_service]
        details_text.config(text=details["description"])
        
        # Update the second combo box with relevant options if available
        if details["options"]:
            sub_combo.config(values=details["options"])
            sub_combo.set(details["options"][0])  # Set the first option as default
            sub_combo.grid(row=2, column=1, padx=10, pady=10)
            notes_text.config(text=details["notes"])
            notes_text.grid(row=3, column=1, padx=10, pady=10)
        else:
            sub_combo.grid_forget()  # Hide the sub combo if no options are available
            notes_text.grid_forget()  # Hide the notes if no notes are available
    else:
        details_text.config(text="Details not found.")
        sub_combo.grid_forget()
        notes_text.grid_forget()
    show_pricing()  # Clear pricing table

def show_pricing(event=None):
    selected_option = sub_combo.get()
    if selected_option == "Plastic Pens Screen Printing (Serigrafía)":
        pricing_text.config(state=tk.NORMAL)
        pricing_text.delete("1.0", tk.END)
        pricing_text.insert(tk.END, plastic_pens_pricing)
        pricing_text.config(state=tk.DISABLED)
        pricing_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    elif selected_option == "Metal Pens and USB Drives Screen Printing (Serigrafía or Tampografía)":
        pricing_text.config(state=tk.NORMAL)
        pricing_text.delete("1.0", tk.END)
        pricing_text.insert(tk.END, metal_pens_usb_pricing)
        pricing_text.config(state=tk.DISABLED)
        pricing_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    elif selected_option == "Plastic Items Screen Printing (Serigrafía)":
        pricing_text.config(state=tk.NORMAL)
        pricing_text.delete("1.0", tk.END)
        pricing_text.insert(tk.END, plastic_items_pricing)
        pricing_text.config(state=tk.DISABLED)
        pricing_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    else:
        pricing_text.grid_forget()
        
def calculate_price():
    try:
        quantity = int(entry_quantity.get())  # Get the quantity from the entry widget
        # Example calculation based on quantity (modify as per your actual calculation needs)
        calculated_result = quantity * 100  # Example calculation, replace with your logic
        result_label.config(text=f"Calculated Result: ${calculated_result} pesos", foreground="blue", font=("Arial", 14, "bold"))
    except ValueError:
        result_label.config(text="Please enter a valid quantity!", foreground="red", font=("Arial", 14, "bold"))

# Create the main window
root = tk.Tk()
root.title("Printing Services Details")

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Create the dropdown (Combobox) for printing services
ttk.Label(frame, text="Select Printing Service:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10)
combo = ttk.Combobox(frame, values=list(printing_data.keys()), width=400//8)
combo.grid(row=0, column=1, padx=10, pady=10)
combo.current(0)  # Set default selection

# Bind the combobox selection event to show_details function
combo.bind("<<ComboboxSelected>>", show_details)

# Create a label to display the selected service details
ttk.Label(frame, text="Details:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10)

details_text = ttk.Label(frame, text="", wraplength=300, justify="left")
details_text.grid(row=1, column=1, padx=10, pady=10)

# Create the second dropdown (Combobox) for additional options
ttk.Label(frame, text="Select Detailed Service:", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10)
sub_combo = ttk.Combobox(frame, width=400//8)
sub_combo.grid(row=2, column=1, padx=10, pady=10)
sub_combo.grid_forget()  # Hide initially
sub_combo.bind("<<ComboboxSelected>>", show_pricing)

# Create a label to display additional notes
ttk.Label(frame, text="Details:", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10)
notes_text = ttk.Label(frame, text="", wraplength=400, justify="left")
notes_text.grid(row=3, column=1, padx=10, pady=10)
notes_text.grid_forget()  # Hide initially

# Create a text widget to display pricing information
pricing_text = tk.Text(frame, wrap="word", state=tk.DISABLED, height=10, width=80)
pricing_text.grid_forget()  # Hide initially

# Create an entry widget for input
ttk.Label(frame, text="Enter Quantity:", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=10)
entry_quantity = ttk.Entry(frame, width=20)
entry_quantity.grid(row=5, column=1, padx=10, pady=10)

# Create a button to calculate the price
calculate_button = ttk.Button(frame, text="Calculate Price", command=calculate_price)
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the calculated result
result_label = ttk.Label(frame, text="", font=("Arial", 16, "bold"))
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Adjust row and column weights so widgets expand correctly
frame.grid_rowconfigure(8, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Show initial details
show_details()

# Start the main loop
root.mainloop()
