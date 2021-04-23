
class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.cartItem = {}

    def addItems(self, itemName, quantity, price):
        self.total += quantity * price
        if itemName not in self.cartItem:
            self.cartItem.update({itemName:{'quantity': quantity, 'price':price}})
        else:
            self.cartItem[itemName]['quantity'] += quantity

    def removeItems(self, itemName, quantity, price):
        if itemName in self.cartItem:
            if quantity < self.cartItem[itemName]['quantity'] and quantity > 0:
                self.total -= quantity*price
                self.cartItem[itemName]['quantity'] -= quantity

            elif quantity >= self.cartItem[itemName]['quantity']:
                self.total -= price * self.cartItem[itemName]['quantity']
                del self.cartItem[itemName]

    def checkout(self, paidcash):
        if cashpaid > paidcash:
            paid = self.total - cashpaid
            if paid >=0:
                return True
        else:
            return "insufficient amount" 

    def  displaySummary(self):
        print("total itmes -> ", self.cartItem)
        print("total price -> ", self.total)


person1 = ShoppingCart()
person1.addItems('Orange', 2, 40)
person1.addItems('Banana', 3, 50)
person1.addItems('Apple', 4, 70)
person1.addItems('Green', 5, 80)
person1.displaySummary()
person1.removeItems('Orange', 2, 40)
person1.removeItems('Apple', 2, 70)
person1.displaySummary()
person1.addItems('Apple', 4, 90)
person1.displaySummary()







