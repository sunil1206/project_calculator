
def bmi_cal(w,h):
    bmi = w/h** 2
    return bmi

w = int(input("Weight"))
h = int(input("height"))
BMI=bmi_cal(w,h)
print(BMI)