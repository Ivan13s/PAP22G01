from collections import deque


class Shop:

    shelves = deque([], 4)
    waiting_list = []

    def add_product(self, product):
        if len(self.shelves) == self.shelves.maxlen:
            self.waiting_list.append(self.shelves.pop())
        self.shelves.appendleft(product)

    def sell_product(self, product):
        self.shelves.remove(product)
        self.shelves.append(self.waiting_list.pop())

    def return_product(self, product):
        self.add_product(product)

shop = Shop()
shop.add_product('paine')
shop.add_product('portocale')
shop.add_product('oua')
shop.add_product('lapte')
shop.add_product('banane')
shop.add_product('rosii')
shop.sell_product('banane')
shop.return_product('banane')
print(shop.shelves)
print(shop.waiting_list)
