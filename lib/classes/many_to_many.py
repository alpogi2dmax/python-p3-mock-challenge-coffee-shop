class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            None
        elif isinstance (name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError('Name must be a string and between 1 and 15 characters')
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_customers = []
        for order in Order.all:
            if order.customer not in unique_customers and order.coffee == self:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        price_list = [order.price for order in Order.all if order.coffee == self]
        return sum(price_list) / len(price_list) if len(price_list) != 0 else 0


class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise ValueError('Name must be a string and more than 2 characters')
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_coffees = []
        for order in Order.all:
            if order.coffee not in unique_coffees and order.customer == self:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and hasattr(self,'_price') == False:
            self._price = price
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise TypeError('customer must be an instance of Customer')
        
    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else: raise TypeError('coffe must be an instance of Coffee')