
# git link: git@github.com:Navneet720/B9IS123_2122_TMD2.git
# student id: 10581018
# name:Navneet DineshKumar Pandey
# module name: B9IS123_2122_TMD2
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

        # creating and initialising the varibles
        # standard tax rate is 20%: 20/100=0.2 (standardRatePay = 0.2)
        # higher tax rate is 40%: 40/100=0.4 (higerTaxRate = 0.4)
        # higher tax rate is 4%: 4/100=0.04 (PRSIrate = 0.04)
        overTimeHours, regularPay, overtimepay, overTimeHourlyRate, grossPay, standardRatePay, standardTax, netPay = 0, 0, 0, 0, 0, 0, 0, 0
        standardTaxRate, higherRatePay, higerTax, higerTaxRate, totalTax, netTax, PRSIrate, netDeduction = 0.2, 0, 0, 0.4, 0, 0, 0.04, 0

        # creating an empty dictionary to store data in it.
        empDetails = {}

        # if hours worked is more than regular hours then the over time hourse will be diffrence between hours worked
        # and regular hours
        if HourseWokred > self.RegHours:
            overTimeHours = HourseWokred - self.RegHours
        else:
            # if hours worked is less than or equal to regular hours then regular hours will be same as hours worked
            self.RegHours = HourseWokred

        # over time hourly rate is  OTMultiple into  hourly rate
        overTimeHourlyRate = self.OTMultiple * self.HourlyRate

        # regular pay is regular hours into hourly rate
        regularPay = self.RegHours * self.HourlyRate

        # overtime pat will be  overtime hours into overtime hourly rate
        overtimepay = overTimeHours * overTimeHourlyRate

        # gross pay is combination of regular pay and overtime pay
        grossPay = regularPay + overtimepay

        # if gross pay is more than standardband then standardTax will be 20% of  standard band other wise standardTax  will be 20% of grosspay
        if grossPay > self.StandardBand:
            standardTax = standardTaxRate * self.StandardBand

            # higerrate  pay is grosspay minus - StandardBand
            higherRatePay = grossPay - self.StandardBand
        else:
            standardTax = grossPay * standardTaxRate

        # higher tax is higerTaxRate into higherRatePay
        higerTax = higerTaxRate * higherRatePay

        # total tax is higher tax plus standard tax
        totalTax = higerTax + standardTax

# if totaltax is greater than tax credit then net tax is total tax minus tax credit if not then net tax will be totaltax
        if (totalTax > self.TaxCreadit):
            netTax = totalTax - self.TaxCreadit
        else:
            netTax = totalTax

        # PRSI is PRSIrate into grosspay
        PRSI = PRSIrate * grossPay

        # net dedcution is netTax and PRSI combination
        netDeduction = netTax + PRSI

    # net pay is gross pay minus net amount to be deducted
        netPay = grossPay - netDeduction

        # storing all the varibles into dictionary created above in key value formate
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

        # printing the dictionary data
        print(empDetails)

        # returning the dictionary in key value formate
        return empDetails

# creating the test class for testcases
class Testpayment(unittest.TestCase):

    # test function to test  net pay can not be greater than grosspay
    def testnet_pay_cannot_exceed_gross_pay(self):
        net_pay = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = net_pay.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    # test function to test overtime  pay can not be negative
    def testOvertimePay_cannotbenegative(self):
        overPay = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = overPay.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Overtime Pay'], -1)
        # self.assertGreater(pi['Overtime Hours Worked'],-1)

    # test function to test overtime hours  pay can not be negative
    def testovertimeHourse_cannotbenegative(self):
        overTimeHourse = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = overTimeHourse.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Overtime Hours Worked'], -1)

    # test function to test regular hours  cannot be greater than hours worked
    def testregular_hours_cannot_morethan_hoursworked(self):
        reg_hours = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = reg_hours.computePayment(1, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], pi["Regular Hours Worked"] + pi["Overtime Hours Worked"])

    # test function to test higher tax cannot be negative
    def test_Higher_Tax_cannot_be_negative(self):
        high_tax = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = high_tax.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Higher Tax'], -1)

    # test function to check netpay cannot negative
    def test_netpay_cannot_be_negative(self):
        net_pay = Employee(10581018, 'Navneet', 'Pandey', 37, 16, 1.5, 72, 710)
        pi = net_pay.computePayment(1, '31/10/2021')
        self.assertGreater(pi['Net Pay'], -1)
