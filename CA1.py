import unittest


class Employee():

    HourseWokred = None

    def __init__(self, StaffID, FirstName, LastName, RegHours, HourlyRate, OTMultiple, TaxCreadit, StandardBand):
        self.StaffID = StaffID
        self.FirstName = FirstName
        self.LastName = LastName
        self.RegHours = RegHours
        self.HourlyRate = HourlyRate
        self.OTMultiple = OTMultiple
        self.TaxCreadit = TaxCreadit
        self.StandardBand = StandardBand

    def computePayment(self, HourseWokred, date):
        empDetails = {}
        overTimeHours = 0
        regularPay = 0
        overtimepay = 0
        overTimeHourlyRate = 24
        grossPay = 0
        standardRatePay = 0
        standardTax = 0
        standardTaxRate = 0.2
        higherRatePay = 0
        higerTax = 0
        higerTaxRate = 0.4
        totalTaxm = 0
        netTax = 0
        PRSIrate = 0.04
        netDeduction = 0
        netPay = 0
        print("HourseWokred = ", HourseWokred)
        if HourseWokred > self.RegHours:
            overTimeHours = HourseWokred - self.RegHours
            print("overtime Hourse", overTimeHours)
            print("regular Hourse", self.RegHours)
        else:
            self.RegHours = HourseWokred
            print("overtime Hourse", overTimeHours)
            print("regular Hourse", self.RegHours)

        regularPay = self.RegHours * self.HourlyRate
        overtimepay = overTimeHours * overTimeHourlyRate
        grossPay = regularPay + overtimepay

        if (grossPay > self.StandardBand):
            higherRatePay = grossPay - self.StandardBand

        standardTax = standardTaxRate * grossPay
        higerTax = higerTaxRate * higherRatePay
        totalTax = higerTax + standardTax

        if (totalTax > self.TaxCreadit):
            netTax = totalTax - self.TaxCreadit  # TO CHHECK
        else:
            netTax = totalTax

        PRSI = PRSIrate * grossPay
        netDeduction = netTax + PRSI
        netPay = grossPay - netDeduction
        #
        # print("regularPay",regularPay)
        # print("overtimepay = ", overtimepay)
        # print("grossPay",grossPay)
        # print("standardTax",standardTax)
        # print("higherRatePay",higherRatePay)
        # print("higerTax = ",higerTax)
        # print("totalTax",totalTax)
        # print("netTax",netTax)
        # print("PRSI",PRSI)
        # print("netDeduction",netDeduction)
        # print("netPay",netPay)
        empDetails["name"] = self.FirstName + " " + self.LastName
        empDetails["Date"] = date
        empDetails['Regular Hours Worked'] = self.RegHours
        empDetails["Overtime Hours Worked"] = overTimeHours
        empDetails["Regular Rate"] = self.HourlyRate
        empDetails["Overtime Rate"] = overTimeHourlyRate
        empDetails["Regular Pay"] = regularPay
        empDetails["Overtime Pay"] = overtimepay
        empDetails["Gross Pay"] = grossPay
        empDetails["Standard Rate Pay"] = self.StandardBand
        empDetails["Higher Rate Pay"] = higherRatePay
        empDetails["Standard Tax"] = standardTax
        empDetails["Higher Tax"] = higerTax
        empDetails["Total Tax"] = round(totalTax, 2)
        empDetails["Tax Credit"] = self.TaxCreadit
        empDetails["Net Tax"] = round(netTax, 2)
        empDetails["PRSI"] = PRSI
        empDetails["Net Deductions"] = round(netDeduction, 2)
        empDetails["Net Pay"] = round(netPay, 2)
        print(empDetails)
        return empDetails



class Testsalary(unittest.TestCase):

    def testnet_pay_cannot_exceed_gross_pay(self):
        net_pay = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = net_pay.computePayment(0, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    def testOvertimePay_cannotbenegative(self):
        overPay = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi=overPay.computePayment(0, '31/10/2021')
        self.assertGreater(pi['Overtime Pay'],-1)

    def testovertimeHourse_cannotbenegative(self):
        overTimeHourse = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = overTimeHourse.computePayment(0, '31/10/2021')
        self.assertGreater(pi['Overtime Hours Worked'], -1)

    def testregular_hours_cannot_morethan_hoursworked(self):
        reg_hours = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = reg_hours.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], pi["Regular Hours Worked"] + pi["Overtime Hours Worked"])

    def test_Higher_Tax_cannot_be_negative(self):
        high_tax = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = high_tax.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Higher Tax'], -1)


    # def testregular_hours_cannot_morethan_hoursworked(self):




# jg= Employee(10501018,'Navneet','Pandey', 37, 16, 1.5, 72, 710)
# x=jg.computePayment(1,'31/10/2021')
# print(x)
