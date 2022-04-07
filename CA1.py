
class Employee(object):

    def __init__(self, StaffID, FirstName, LastName, RegHours, HourlyRate, OTMultiple, TaxCreadit ,StandardBand):
     self.StaffID = StaffID
     self.FirstName = FirstName
     self.LastName =LastName
     self.RegHours = RegHours
     self.HourlyRate =HourlyRate
     self.OTMultiple =OTMultiple
     self.TaxCreadit =TaxCreadit
     self.StandardBand =StandardBand

    def computePayment(self, HourseWokred, date):
        overTimeHours = 0
        regularPay = 0
        overtimepay = 0
        overTimeHourlyRate = 24
        grossPay=0
        standardRatePay=0
        if HourseWokred > self.RegHours:
         overTimeHours = HourseWokred - self.RegHours
         print("overtime Hourse",overTimeHours)
         print("regular Hourse",self.RegHours)

        if HourseWokred <= self.RegHours:
            self.RegHours = HourseWokred
            print("overtime Hourse", overTimeHours)
            print("regular Hourse", self.RegHours)

        regularPay = self.RegHours * self.HourlyRate
        overtimepay = overTimeHours * overTimeHourlyRate
        grossPay = regularPay + overtimepay
        standardRatePay = grossPay - self.StandardBand
        
        print(regularPay)
        print(overtimepay)
        print(grossPay)
        print(standardRatePay)



jg= Employee(10501018,'Navneet','Pandey', 37, 16, 1.5, 72, 710)
jg.computePayment(42,'31/10/2021')
