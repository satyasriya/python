'''create a class ticket which will be the abstract class inside that create a function book_ticket which will be the abstract method
and has nothing in it create a class make my trip which will use the bookticket function from ticket class to take the details such as name , ph no,
email id,journey date,and displays a msg saying "thankyou for booking from make my trip".
create a class irctc which uses the book ticket of ticket class and takes the same details as make my trip but in the end it will give an
option to user to select whether it is one way or round trip if the user option is round trip it again asks the user to enter
the return date as well and then prints a msg "thankyou for choosing irctc" else print the msg "thankyou for choosing irctc".
create a class indigo which takes all the details as irctc and just asks which mode of transport u want to go in train, flight, or bus
and displays "thankyou for choosing indigo"  '''


from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class make_my_trip(ticket):
    def book_ticket(self):
        name=input("enter name:")
        ph_no=input("enter phone no:")
        email_id=input("enter email id:")
        journey_date=input("enter journey date:")
        print("thankyou for booking from make my trip!!")
class irctc(ticket):
    def book_ticket(self):
        name=input("enter name:")
        ph_no=input("enter phone no:")
        email_id=input("enter email id:")
        journey_date=input("enter journey date:")
        trip=input("round trip or one way trip: ")
        if trip=="round trip":
            return_date=input("enter return date:")
            print("thankyou for choosing irctc!")
        else:
            print("thankyou for choosing irctc!")
class indigo(ticket):
    def book_ticket(self):
        name=input("enter name:")
        ph_no=input("enter phone no:")
        email_id=input("enter email id:")
        journey_date=input("enter journey date:")
        trip=input("round trip or one way trip: ")
        if trip=="round trip":
            return_date=input("enter return date:")
        mode=input("enter which mode of transport u want to go in train, flight, or bus: ")
        print("thankyou for choosing indigo!")
x=make_my_trip()
y=irctc()
z=indigo()
x.book_ticket()
y.book_ticket()
z.book_ticket()
        
