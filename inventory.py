 class Item():
     def __init__(self, name, price):
         self.name = name
         self.price = price

     def __str__(self):
         if print(Item):
             return self.name + "$" + self.price

     def change_price(self, price):
         new_price = input(int("enter a new price:"))
         self.price = new_price


 class Keyboard(Item):
     def __init__(self, brand, price):
         self.brand = brand
         if brand == "BrandA":
             self.price(float(19.99))
         elif brand == "BrandB":
             self.price(float(99.00))
         else:
             self.price(float(39.99))

 print('soap, shampoo, beer, candies, doritos')
 want_item = input(str('What item would you like to purchase?'))

 item1 = Item('soap','1.99')
 print('Price: $', Item.price(item1))
 item2 = Item('shampoo','2.99')
 print('Price: $', Item.price(item1))
 item3 = Item('beer','3.99')
 print('Price: $', Item.price(item1))
 item3 = Item('doritos','1.49')
 print('Price: $', Item.price(item1))
