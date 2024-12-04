# program to calculate BMI
# BMI = weight in kg / height in meter square

weight_in_kg=int(input("enter the value in kg => "))

height_in_cm=int(input("enter the value in cm => "))

height_in_meter=height_in_cm/100

Bmi=weight_in_kg/(height_in_meter**2)

BMI=round(Bmi,2)

print(BMI)