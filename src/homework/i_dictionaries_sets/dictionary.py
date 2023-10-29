widget_inv = {}

def add_inventory(widget_name, quantity):
    global widget_inv
    if widget_name in widget_inv.keys():

        widget_inv[widget_name] += quantity
        return widget_inv
    else:
        widget_inv[widget_name] = quantity
        return widget_inv
    

def remove_inventory_widget(widget_name):
    global widget_inv

    if widget_name in widget_inv.keys():
        del widget_inv[widget_name]
        print("Record deleted.")
    else:
        print("Item not found.")

    