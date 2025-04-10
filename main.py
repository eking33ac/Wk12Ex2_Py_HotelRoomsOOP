# Create a Hotel room class
class HotelRoom:
    # constructor
    def __init__(self,RoomNumber,RoomType,IsBooked):
        # set the object's room number to the room number typed
        self.RoomNumber = RoomNumber
        # set the object's Room Type to the Room Type typed
        self.RoomType = RoomType
        # set the object's booked status to the book status typed
        self.IsBooked = IsBooked
    
    #methods
    # method to book a hotel room
    def BookRoom(self):
        # set the room to being booked
        self.IsBooked = True
        
    # method to cancel a hotel room booking
    def CancelBooking(self):
        # set the room to not being booked
        self.IsBooked = False
        
    # method to streamling displaying the availability
    def DisplayAvailability(self):
        if self.IsBooked == True:
            print(f"The {self.RoomType} room {self.RoomNumber} is booked.\n")
        else:
            print(f"The {self.RoomType} room {self.RoomNumber} is available to book.\n")
        
        
# create the first hotel room object
room1 = HotelRoom("101","Single",False)
# create the second hotel room object
room2 = HotelRoom("102","Double",True)

# display initial availability of room1
room1.DisplayAvailability()
# display initial availability of room2
room2.DisplayAvailability()

# book room 1
room1.BookRoom()
# unbook room 2
room2.CancelBooking()

# display new availability of room1
room1.DisplayAvailability()
# display new availability of room2
room2.DisplayAvailability()