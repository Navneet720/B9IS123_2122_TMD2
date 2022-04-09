# importing unitest framework for testing the methods given for CA.
import unittest


# creating the class Employee.
class Employee:

    # Creating the python constructor to initialise instance  variable/data members of class.
    # Using self keyword for accessing the instance defined within Employee class.
    # Passing the parameters to constructor to initialise them
    def __init__(self, StaffID, FirstName, LastName, RegHours, HourlyRate, OTMultiple, TaxCreadit, StandardBand):

        # initialising the data members of class
        self.StaffID = StaffID
        self.FirstName = FirstName
        self.LastName = LastName
        self.RegHours = RegHours
        self.HourlyRate = HourlyRate
        self.OTMultiple = OTMultiple
        self.TaxCreadit = TaxCreadit
        self.StandardBand = StandardBand

    # creating a method computePayment and passing parameters (HoursWorked and date)
    def computePayment(self, HourseWokred, date):

        # creating and assigning  multiple values to variables
        # over time rate=24 (already given)
        # standard tax rate is 20%: 20/100=0.2 (standardRatePay = 0.2)
        # higher tax rate is 40%: 40/100=0.4 (higerTaxRate = 0.4)
        # higher tax rate is 4%: 4/100=0.04 (PRSIrate = 0.04)
        overTimeHours, regularPay, overtimepay, overTimeHourlyRate, grossPay, standardRatePay, standardTax, netPay = 0, 0, 0, 24, 0, 0, 0, 0
        standardTaxRate, higherRatePay, higerTax, higerTaxRate, totalTax, netTax, PRSIrate, netDeduction = 0.2, 0, 0, 0.4, 0, 0, 0.04, 0

        # creating an empty dictionary
        empDetails = {}

        if HourseWokred > self.RegHours:
            overTimeHours = HourseWokred - self.RegHours
        else:
            self.RegHours = HourseWokred

        regularPay = self.RegHours * self.HourlyRate
        overtimepay = overTimeHours * overTimeHourlyRate
        grossPay = regularPay + overtimepay

        if (grossPay > self.StandardBand):
            higherRatePay = grossPay - self.StandardBand
            standardTax = standardTaxRate * self.StandardBand
        else:
            standardTax=grossPay * standardTaxRate

        # standardTax = standardTaxRate * self.StandardBand
        print(standardTax)
        print(self.StandardBand)
        higerTax = higerTaxRate * higherRatePay
        totalTax = higerTax + standardTax

        if (totalTax > self.TaxCreadit):
            netTax = totalTax - self.TaxCreadit  # TO CHHECK
            print("HI",totalTax)
            print("self.TaxCreadit")
        else:
            netTax = totalTax
        print("gp",grossPay)
        PRSI = PRSIrate * grossPay
        netDeduction = netTax + PRSI
        print(netTax)
        print(PRSIrate)
        print(grossPay)
        print(PRSI)
        print(netDeduction)
        print(netPay)
        netPay = grossPay - netDeduction
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
        # print(empDetails)
        return empDetails


class Testpayment(unittest.TestCase):

    def testnet_pay_cannot_exceed_gross_pay(self):
        net_pay = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = net_pay.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    def testOvertimePay_cannotbenegative(self):
        overPay = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = overPay.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Overtime Pay'], -1)
        # self.assertGreater(pi['Overtime Hours Worked'],-1)

    def testovertimeHourse_cannotbenegative(self):
        overTimeHourse = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = overTimeHourse.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Overtime Hours Worked'], -1)

    def testregular_hours_cannot_morethan_hoursworked(self):
        reg_hours = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = reg_hours.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], pi["Regular Hours Worked"] + pi["Overtime Hours Worked"])

    def test_Higher_Tax_cannot_be_negative(self):
        high_tax = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = high_tax.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Higher Tax'], -1)

    def test_netpay_cannot_be_negative(self):
        net_pay = Employee(10501018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = net_pay.computePayment(25, '31/10/2021')
        self.assertGreater(pi['Net Pay'], -1)
