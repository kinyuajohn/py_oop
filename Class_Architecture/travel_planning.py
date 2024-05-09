class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0

    def trip_info(self):
        if self.month >= 10 and self.month <= 3:
            print(
                f"You are going to {self.country} in the winter. This is a {self.type} trip."
            )
        elif self.month > 3 and self.month < 10:
            print(
                f"You are going to {self.country} in the summer. This is a {self.type} trip."
            )
        else:
            print("Invalip input!")

    def calc_cost(self, cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost: "))

        return self.advice(self.price), self.list_inspect(costs)

    def advice(self, num):
        if num < 500:
            print("Low budget")
        elif num >= 500 and num < 1500:
            print("Take a flight to anywhere ...")
        else:
            print("Luxury Trip")

    def list_inspect(self, costs):
        less_than_ten = 0
        for cost in costs:
            if cost >= 10:
                less_than_ten += 1

        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price: {self.price}")


location = input("Enter a country: ").title()
trip_type = input("Leisure or Business: ").title()
month = input("Enter a month: ")

test = Travel(location, month, trip_type)
test.trip_info()

flight_cost = int(input("Enter flight cost: "))
test.calc_cost(flight_cost)
