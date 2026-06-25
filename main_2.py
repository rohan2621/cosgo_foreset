temp = int(input("Enter temperature: "))
humi = int(input("Enter humidity: "))

if  temp>50:
    if humi <15:
        print("High risk alert!!")
    else:
        print("Medium risk ")
else:
    print("Chill out ")