##Diego Medina

import unittest


from classes import test

class classescalculate(unittest, testcase):
    #create class test that can be used by all unit 

    testBMIcalculate_bmi = test()

    # initialise the  test the classs

    def setUp(self):
        self.testBMIcalculate_bmi = test()

    # test  test method runs


    def tearDonw(self):
        del self.testBMIcalculate_bmi

    """this test is for calculate the weight in kgs and height in meter
        Get BMI value. bmi = weight in Kgs / height in metres squared
    """
    def test_calculate_the_weightinkgs(self):
    #Assing
        weight = 1000
        height = "kgs"
        exp_result = (weight / (height * height))

    #Act
        actual_calculate = self.testBMIcalculate_bmi.weight_in_kgs(weight, height)

    #Assert
        self.assertEqual(exp_result, actual_calculate)


    """this test is for calculate the weight in kgs and height in meter
        this calculate is for weight in metres
    """
    
    def test_calculate_the_heightinmeter(self):
        #Assing

        bmi = 1000
        weight = "kgs"
        height =  "meter"
        exp_result = weight / (height * height)

        #Act 
        actual_calculate = self.testBMIcalculate_bmi.weight_in_kgs(bmi, weight, height)

        self.assertEqual(exp_result, actual_calculate)

    """this test is for calculate the weight in kgs and height in meter
    BMI value of less than 18.5 = underWeight 
    """

    def test_calculate_the_less18heightinmeter(self):
        #Assing 
        bmi = 18 
        exp_result = "underWeight"

        #Act

        actual_calculate = self.testBMIcalculate_bmi.weight_in_kgs(bmi)

        #Assert

        self.assertEqual(exp_result, actual_calculate)

    """this test is for calculate the weight in kgs and height in meter
    test the value between  BMI value of 18.5 to less than 25
    """

    #Assing 
    def test_calculate_the_between18to24heightinmeter(self):

        bim18 = 18.5
        bim24 = 24
        exp_result = "Normal"

    #Act 
        actual_calculate18 = self.testBMIcalculate_bmi.weightcategory(bim18)
        actual_calculate24 = self.estBMIcalculate_bmi.weightcategory(bim24)

    #Assert

        self.assertEqual(exp_result, actual_calculate18)
        self.assertEqual(exp_result, actual_calculate24)

    
    """ this test is for calculate the weight in kgs and height in meter
        test the value between  BMI value BMI value of 25 to less than 30
    """
    def test_calculate_the_between25to29heightinmeter(self):
     #Assing 

        bim25 = 25
        bim29 = 29
        exp_result = "Overweight"

    #Act 
        actual_calculate25 = self.testBMIcalculate_bmi.weightcategory(bim25)
        actual_calculate29 = self.estBMIcalculate_bmi.weightcategory(bim29)

    #Assert

        self.assertEqual(exp_result, actual_calculate25)
        self.assertEqual(exp_result, actual_calculate29)



    """this test is for calculate the weight in kgs and height in meter
    test the value between  BMI value BMI value of 30 or more
    """
    def test_calculate_the_height30over(self):
     #Assing 


        bim30 = 30
        exp_result = "Obese"

    #Act 
        actual_calculate30 = self.estBMIcalculate_bmi.weightcategory(bim30)

    #Assert
        self.assertEqual(exp_result, actual_calculate30)