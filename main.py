temp=int(input("Enter temperature: "))
humi=int(input("Enter humidity: "))


if temp>50 and humi <15 :
    print("OMG risk level highhh!!!")
elif temp>50 or humi <15:
    print("Risk level medium")
else:
    print("Chill out ")