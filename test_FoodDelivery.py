from FoodDeliverySystem import FoodDeliverySystem


def test_food_delivery():
    deliverysystem = FoodDeliverySystem()
    order =  deliverysystem.place_order("Luiz", {"Buger" : 5, "pizza" : 1})
    assert order, {2 : {"custumer_name" : "Luiz" , "order_item" : {"Buger" : 5}, "status" : "Placed"}}
