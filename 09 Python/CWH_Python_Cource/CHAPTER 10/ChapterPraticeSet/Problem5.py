#Q.Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 

from random import randint
class Train:
    
    def __init__(self, train_no):
        self.train_no = train_no
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.train_no} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.train_no} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {randint(222, 5555)}")

t = Train(5454)
t.book("Pune", "Mumbai")
t.getStatus()
t.getFare("Pune", "Mumbai")
