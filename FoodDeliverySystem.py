class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):
        details = ""
        for item, price in self.menu.items():
            details += f"{item} | {price}\n"
            return details

        
    def place_order(self, customer_name, order_items):
        if customer_name in self.orders_log:
            order_id = len(self.orders_log) + 1
        else:
            order_id = 1 

        for item in order_items.items():
            if item not in self.menu:
                return "Order placement failed . Invalid item in order"
        
        self.orders_log[order_id] = {"custumer_name" : customer_name, "order_item" : order_items, "status" : "Placed"}
        return self.orders_log

        
    def pickup_order(self, order_id):
        if order_id in self.orders_log:
            self.orders_log[order_id]["Status"] = "Picked Up"
            return self.orders_log[order_id]
        else:
            return "Order not found"
        
    def deliver_order(self, order_id):
        if order_id in self.orders_log:
            self.orders_log[order_id]["Status"] = "Delivered"
            return "Order delivered"
        else:
            return "Order fond found"
 
        
    def modify_order(self, order_id, new_items):
        if order_id in self.orders_log and self.orders_log[order_id]["Status"] != "Picked Up":
            for item in new_items:
                if item not in self.menu:
                    return "Order modification failed. Invalid item in the new order."
                self.orders_log[order_id]["order_items"].update(item)
            return self.orders_log[order_id] 
        else:
            return "Order modification failed. Order cannot be modified."
    
    def generate_bill(self, order_id):
        amount = len(self.orders_log[order_id])
        if amount > 1000:
            amount_total = sum(amount + 0.1 * amount)
        else:
            amount_total = sum(amount + 0.05 * amount)
        return amount_total
            
    def cancel_order(self, order_id):

        if order_id in self.orders_log and self.orders_log[order_id]["Status"] != "Picked Up":
            del self.orders_log[order_id]
            return self.orders_log
        else:
            return "Order not found or with status Picked Up"



