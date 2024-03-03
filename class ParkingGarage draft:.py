class ParkingGarage:
    def __init__(self, total_spaces, total_tickets):
        self.spaces = list(range(1, total_spaces + 1))
        self.tickets = list(range(1, total_tickets + 1))
        self.current_tickets = {}

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            parking_space = self.spaces.pop(0)
            self.current_tickets[ticket] = {'paid': False, 'parking_space': parking_space, 'amount_owed': 25}
            print(f"Ticket {ticket} issued. Park in space {parking_space}. Amount owed: $25.")

    def pay_for_parking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_tickets and not self.current_tickets[ticket]['paid']:
            amount = input("Enter the payment amount: ")
            if amount == '25':
                self.current_tickets[ticket]['paid'] = True
                print(f"Ticket {ticket} paid. You have 15 minutes to leave.")
                self.tickets.append(ticket) #Add the ticket back to the tickets list
                self.spaces.append(ticket) #Add the ticekt back to the tickets list
            else:
                print("Incorrect amount. Please pay $25.")
        else:
            print("Ticket already paid for Thank you, have a nice day! .")

    def leave_garage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_tickets:
            if self.current_tickets[ticket]['paid']:
                print("Thank you, have a nice day!")
            else:
                print("Please pay for parking before leaving.")
                self.pay_for_parking()
            self.spaces.append(self.current_tickets[ticket]['parking_space'])
            self.tickets.append(ticket)
            del self.current_tickets[ticket]
        else:
            print('Invalid ticket number. Please check and try again.')

    def print_status(self):
        print("\nCurrent Garage Status:")
        print(f"Available Spaces: {self.spaces}")
        print(f"Available Tickets: {self.tickets}")
        print(f"Current Tickets: {self.current_tickets}")

    def run(self):
        while True:
            self.print_status()
            menu = input("Would you like to take a ticket, pay for parking, leave the garage, or exit? ")
            if menu.lower() == 'ticket':
                self.take_ticket()
            elif menu.lower() == 'pay':
                self.pay_for_parking()
            elif menu.lower() == "leave":
                self.leave_garage()
            else:
                print("Not a valid input, please try again.")

parking_garage = ParkingGarage(10, 10)
parking_garage.run() 