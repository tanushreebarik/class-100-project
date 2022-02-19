class Atm(object):

    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def cashwithdrawal(self):
        print("cashwithdrawal")

    def bankenquiry(self):
        print("bankenquiry")

icic = Atm("1234567890", "0000")
print(icic.pinnumber)
print(icic.cashwithdrawal())