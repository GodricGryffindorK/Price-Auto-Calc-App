import tkinter as tk
from tkinter import ttk
from printing_data import printing_data
from pricing_info import plastic_pens_pricing, metal_pens_usb_pricing, plastic_items_pricing

def show_details(event=None, combo=None, details_text=None, sub_combo=None, notes_text=None, pricing_text=None):
    selected_service = combo.get()
    if selected_service in printing_data:
        details = printing_data[selected_service]
        details_text.config(text=details["description"])
        
        if details["options"]:
            sub_combo.config(values=details["options"])
            sub_combo.set(details["options"][0])
            sub_combo.grid(row=2, column=1, padx=10, pady=10)
            notes_text.config(text=details["notes"])
            notes_text.grid(row=3, column=1, padx=10, pady=10)
        else:
            sub_combo.grid_forget()
            notes_text.grid_forget()
    else:
        details_text.config(text="Details not found.")
        sub_combo.grid_forget()
        notes_text.grid_forget()
    show_pricing(event=None, sub_combo=sub_combo, pricing_text=pricing_text)  # Pass sub_combo and pricing_text here


def show_pricing(event=None, sub_combo=None, pricing_text=None):
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

def calculate_price(entry_quantity, result_label, combo, sub_combo):
    try:
        quantity = int(entry_quantity.get())
        
        # Get the selected service and detailed option
        selected_service = combo.get()
        selected_option = sub_combo.get()

        # Determine the price per unit based on the selected option
        if selected_service == "Screen printing":
            if selected_option == "Plastic Pens Screen Printing (Serigrafía)":
                price_per_unit = get_price_per_unit(plastic_pens_pricing, quantity)
                setup_cost = 5000
                calculated_result = quantity * price_per_unit + setup_cost
            elif selected_option == "Metal Pens and USB Drives Screen Printing (Serigrafía or Tampografía)":
                price_per_unit = 0  # Replace with actual pricing logic
                calculated_result = quantity * price_per_unit
            elif selected_option == "Plastic Items Screen Printing (Serigrafía)":
                price_per_unit = 0  # Replace with actual pricing logic
                calculated_result = quantity * price_per_unit
            else:
                calculated_result = 0  # Handle other cases if needed
        elif selected_service == "Pad printing":
            if selected_option == "Pad Printing on Plastic and Curved Surfaces (including Ecological Items)":
                price_per_unit = 0  # Replace with actual pricing logic
                calculated_result = quantity * price_per_unit
            elif selected_option == "Pad Printing on Stress Balls (1 Color, One Side)":
                price_per_unit = 0  # Replace with actual pricing logic
                calculated_result = quantity * price_per_unit
            else:
                calculated_result = 0  # Handle other cases if needed
        else:
            calculated_result = 0  # Handle other services if needed
        
        # Display the calculated result
        result_label.config(text=f"Calculated Result: ${calculated_result} pesos", foreground="blue", font=("Arial", 14, "bold"))
    
    except ValueError:
        result_label.config(text="Please enter a valid quantity!", foreground="red", font=("Arial", 14, "bold"))

def get_price_per_unit(pricing_info, quantity):
    """
    Function to parse pricing information and determine the price per unit based on quantity.
    """
    price_per_unit = 0
    
    # Split the pricing info into lines
    lines = pricing_info.strip().splitlines()
    
    # Iterate through lines to find the matching quantity range
    for line in lines[2:]:  # Skip the header lines
        parts = line.split('|')
        quantity_range = parts[0].strip()
        price_per_unit_str = parts[1].strip()
        
        # Parse the quantity range
        range_parts = quantity_range.split('-')
        range_start = int(range_parts[0].replace(',', '').strip())
        range_end = int(range_parts[1].replace(',', '').strip(' units'))
        
        # Parse the price per unit
        price_per_unit = parse_price_per_unit(price_per_unit_str)
        
        # Check if the quantity falls within the current range
        if range_start <= quantity <= range_end:
            return price_per_unit
    
    return price_per_unit


def parse_price_per_unit(price_str):
    """
    Function to parse the price per unit from the formatted string.
    """
    # Example: "$30,000 pesos"
    price_str = price_str.replace(',', '').replace('$', '').replace(' pesos', '').strip()
    return int(price_str)

def create_gui(root):
    # Frame for GUI
    frame = ttk.Frame(root, padding=20)
    frame.grid(row=0, column=0, sticky="nsew")

    # Label and Combobox for printing service selection
    ttk.Label(frame, text="Select Printing Service:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10)
    combo = ttk.Combobox(frame, values=list(printing_data.keys()), width=600//8)
    combo.grid(row=0, column=1, padx=10, pady=10)
    combo.current(0)
    combo.bind("<<ComboboxSelected>>", lambda event: show_details(event, combo, details_text, sub_combo, notes_text, pricing_text))

    # Label and Text for details
    ttk.Label(frame, text="Details:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10)
    details_text = ttk.Label(frame, text="", wraplength=300, justify="left")
    details_text.grid(row=1, column=1, padx=10, pady=10)

    # Label and Combobox for detailed service selection
    ttk.Label(frame, text="Select Detailed Service:", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10)
    sub_combo = ttk.Combobox(frame, width=600//8)
    sub_combo.grid(row=2, column=1, padx=10, pady=10)
    sub_combo.bind("<<ComboboxSelected>>", lambda event: show_pricing(event, sub_combo, pricing_text))

    # Label and Text for notes
    ttk.Label(frame, text="Details:", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10)
    notes_text = ttk.Label(frame, text="", wraplength=600, justify="left")
    notes_text.grid(row=3, column=1, padx=10, pady=10)

    # Text widget for pricing information
    pricing_text = tk.Text(frame, wrap="word", state=tk.DISABLED, height=10, width=80)
    pricing_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Label and Entry for quantity input
    ttk.Label(frame, text="Enter Quantity:", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=10)
    entry_quantity = ttk.Entry(frame, width=20)
    entry_quantity.grid(row=5, column=1, padx=10, pady=10)

    # Button to calculate price
    calculate_button = ttk.Button(frame, text="Calculate Price", command=lambda: calculate_price(entry_quantity, result_label, combo, sub_combo))

    calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Label to display calculated result
    result_label = ttk.Label(frame, text="", font=("Arial", 16, "bold"))
    result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Adjust row and column configurations
    frame.grid_rowconfigure(8, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Show initial details
    show_details(event=None, combo=combo, details_text=details_text, sub_combo=sub_combo, notes_text=notes_text, pricing_text=pricing_text)