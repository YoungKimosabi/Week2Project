
class ParkingGarage():
    currentticket={
        1: 'paid',
        2: 'paid',
        3: 'paid',
        4: 'paid',
        5: 'paid',
        6: 'paid',
        7: 'paid',
        8: 'paid',
        9: 'paid',
        10: 'paid'

    }
    unavailable_parking_spaces=[]
    unavailable_tickets=[]
    available_parking_spaces= ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'fox', 'golf', 'hotel', 'india', 'juliet']
    available_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def __init__(self):
        self.available_tickets = ParkingGarage.available_tickets
        self.unavailable_tickets = ParkingGarage.unavailable_tickets
        self.available_parking_spaces = ParkingGarage.available_parking_spaces
        self.unavailable_parking_spaces = ParkingGarage.unavailable_parking_spaces
    def take_ticket(self):
        first = self.unavailable_tickets.append(self.available_tickets.pop()) 
        second = self.unavailable_parking_spaces.append(self.available_parking_spaces.pop())
        used = self.unavailable_tickets[-1]
        self.currentticket[used]= 'unpaid' 
        print(f'Processing... \n Please proceed to parking space: {self.unavailable_parking_spaces[-1]}') 
        print(self.available_parking_spaces)
        print(self.unavailable_parking_spaces) 
        print(self.available_tickets)     
        print(self.unavailable_tickets)  
        print(self.currentticket)
        
        
        
    def pay_for_parking(self):
        payment = int(input('Please enter the amount owed'))
        paid = 15
        while True:
            if payment != 15:
                print('Yeah right get back, enter the correct amount because I only take exact amount')
                pass
            elif payment == paid:
                used = self.unavailable_tickets[-1]
                self.currentticket[used] = 'paid'
                first = self.available_tickets.append(self.unavailable_tickets.pop()) 
                second = self.available_parking_spaces.append(self.unavailable_parking_spaces.pop())
                print('Thank you for your payment, please exit the garage')
                break
                
            
                

            
            

        print(self.available_parking_spaces)
        print(self.unavailable_parking_spaces) 
        print(self.available_tickets)     
        print(self.unavailable_tickets)  
        print(self.currentticket)
                
class UI():
    def __init__(self):
        self.parkinggarage = ParkingGarage()
    
    def run_program(self):
        while True:
            response = input('Hello, Welcome to the Parking Garage! \n Are you Checking In or Checking out? ')
            if response.lower() == 'checking in':
                question = input('Would you like a ticket? Please respond with "Yes" or "No" ')
                if question.lower() == 'yes':
                    self.parkinggarage.take_ticket()
                if question.lower() == 'no':
                    print('Then why are you here? Go away Aye Aye Sir!')
            elif response.lower() == 'checking out':
                self.parkinggarage.pay_for_parking()
            else:
                print('Invalid response try again later')
                break
                
        
        
def execute():
    ui = UI()
    ui.run_program()




execute()  