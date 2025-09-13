class Mobile:
    def __init__(self, **kwargs):
       print("Mobile is created...",kwargs)
       self.dial_list=kwargs

    def __str__(self):
        return ("String method called...")  

    def dial_numb(self, phone_number):
        # dst = {'siva': 12345, 'kumar': 67890}
        for name, number in self.dial_list.items():
            if phone_number == number:
                print(f"Dialing {name} at {number}")
                break
        else:
            print("Dialing number...",self)

    def send_msg(self, phone_number):
        for name, number in self.dial_list.items():
            if phone_number == number:
                print(f"Sending message to {name} at {number}")
                break

siva=Mobile(kumar=12345, ram=1235678945)
# print(id(siva))
print(siva)
siva.dial_numb(12345)
siva.send_msg(1235678945)    
print((1).__add__(2))   