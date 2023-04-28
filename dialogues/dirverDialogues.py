print(""" Booking request...
          Source Location to Destination
          Rent:
          Distance:
          Customer name:
          Customer number: 
""")
print(""" 
          1-Accept
          2-Decline
          3-Wait
""")
query = input("> ")
for x in query:
    if (x == "1"):
        print("Enter the OTP")
        query = input("> ")
        print("Ride started!")
        query = input("> ")
        print("Ride ended!")
        print("""
                 Please tell us the feedback of customer:
                 Rate out of five.
        """)
        query = input("> ")
        print("Thanks for giving us the valuable feedback!")
    elif (x == "2"):
        print("You've declined the request!")
    elif (x == "3"):
        print("You've asked to wait. Will contact you soon!")
