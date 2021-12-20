class Shop:
    name = None
    choice = None
    qty = None

    def __init__(self, products_list):
        self.products = products_list

    def printMenu(self):
        for i, (k,v) in enumerate(self.products.items(), start=1):
            print(f"{i}. {k} - {v}")
        return self

    def getChoice(self):
        while bool(self.choice) == False or not inProducts:
            self.choice = input("What you want to choose?\nExample: item1:\n") 
            inProducts = self.products.get(self.choice, False)
        return self

    def getQty(self):
        while bool(self.qty) == False or not self.qty.isnumeric()  :
            self.qty = input("How many? ")  
        return self

    def greetings(self, name=None):
        while bool(self.name) == False:
            self.name = input("Hello! How can I call you? ")       
        else:
            print(f"Hello {self.name}")
        return self
    
    def summurize(self):
        return float(self.products.get(self.choice)) * float(self.qty)

    def showPrice(self):
        print("You have to pay ${}.".format(self.summurize()))

    def out(self, string=None):
        if string:
            print(string.format(self.name))
        else:
            print("Have a nice day {}.".format(self.name))





products_list = {
    "item1": 12.1,
    "item2": 14.3,
    "item3": 2.9,
    "item4": 36.2,
}

shop = Shop(products_list)
shop.greetings()
shop.printMenu()
shop.getChoice()
shop.getQty()
shop.showPrice()
shop.out()
