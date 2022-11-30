class BMI():
    """
    Get BMI value. bmi = weight in Kgs / height in metres squared
    """
    def calculate_bmi(self, weight, height):
        if weight > 0 and height > 0:
            bmi = weight / (height * height)
            return bmi
        else:
            return 0

    """
    * Based on BMI value, return the BMI category
    * BMI value of less than 18.5 = underWeight   
    * BMI value of 18.5 to less than 25 = normal 
    * BMI value of 25 to less than 30 = overWeight 
    * BMI value of 30 or more = obese 
    """
    def calculate_bmi_category(self, bmi):
        underWeightUpperLimit = 18.5
        normalWeightUpperLimit = 25
        overWeightUpperLimit = 30 # Obese from 30 +

        if bmi <= underWeightUpperLimit:
            category = "Underweight"
        elif bmi <= normalWeightUpperLimit:
            category = "Normal"
        elif bmi <= overWeightUpperLimit:
            category = "Overweight"
        else:
            category = "Obese"

        return category

if __name__ == '__main__':
    print("******                *******    ")
    print("****** BMI Calculator *******    ")
    weight = float(input("Please enter weight in KG: "))
    height = float(input("Please enter height in Metres:  "))

    bmi = BMI()

    bmi_value = bmi.calculate_bmi(weight, height)
    print("Your BMI value is: ", str(bmi_value))
    print("Your BMI category is: ", bmi.calculate_bmi_category(bmi_value))
    
    main__init__.py
    main()
    











    
    













    

    

    








