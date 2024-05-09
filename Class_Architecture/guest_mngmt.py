class Guest:
    def __init__(self, first, last, rank, age):
        self.first_name = first
        self.last_name = last
        self.rank = int(rank)
        self.age = int(age)

    def guest_info(self, all_guests):
        for guest in all_guests:
            print(f"{guest.first_name} {guest.last_name} Age: {guest.age}")

    def loyalty_program(self, all_guests):
        # create a list for any guest who has more than 10 points
        # add last name to every guest in the list
        # this condition must be met to be added to the list
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]

        if gold_members:
            print("Gold Members:")
            for member in gold_members:
                print(f"    Guest: {member}")

    def guest_avg(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        avg_age = total_age / len(all_guests)
        print("Average customer age:", avg_age)


all_guests = list()
num_guests = int(input("Enter a number of guests: "))

for _ in range(num_guests):
    data = input("First Name/Last Name/Rank/Age: ").split("/")
    # data = ["John", "Doe", "8", "45"]
    guest = Guest(data[0], data[1], int(data[2]), int(data[3]))
    all_guests.append(guest)

guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)
