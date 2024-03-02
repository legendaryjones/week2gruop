class ParkingGarage:
    def __init__(self, total_spaces, total_tickets, ):
        self.spaces = spaces = list(range(1, total_spaces +1))
        self.tickets = tickets = list(range(1, total_tickets +1))
        self.currentTickets = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self,currentTickets[ticket] = {'paid': False, 'parking_space': print(
                f"Ticket {ticket} issued. Park in space {parking_space}")}
    
    def pay_for_parking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_ticket and not self.current_ticket[ticket]['paid']:
            amount = input("Enter the payment amount: ")
            print(f"Ticket {ticket} paid. You have 15 minutes to leave.") if amount else print("Give me your money.")
    
    def leavegarage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]['paid']:
                print("Thank you, have a nice day!!!!!!!") if self.current_ticket[Ticket]['paid'] else self.pay_for_parking()
                self.parkingSpace.append(self.currentTicket[tickets]['parking_space'])
                self.ticket.append(ticket)
            else:
                print('Invalid ticket number. Please check and try again.')
    
    def run(self):
        while True:
            menu = input("Would you like to take a ticket, pay for parking, or leave the garage? ")
            if menu == 'take a ticket':
                self.takeTicket
            elif menu == 'pay for parking':
                 self.pay_for_parking
            elif menu == "leave the garage":
                 self.leavegarage
                 break
            else:
                print("Not a valid input, please try again. ")

parking_garage = ParkingGarage(10, 10)

parking_garage.run()