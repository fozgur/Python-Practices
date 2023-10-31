names = ["Ali", "Veli", "Aylin","Nilgun"]
surnames = ["Arin", "Cirisci", "Candan", "Kurtkapan"]
birth_days = [15, 22, 8, 17]
birth_months = [3, 6, 12, 12]
birth_years = [1984, 1994, 2001, 1997]

name= input ("Please enter your name: ").capitalize()

if name in names:
  name_idx = names.index(name)

  if birth_months[name_idx]<10:
    month_fix = "0"+ str(birth_months[name_idx])
  elif birth_days[name_idx] < 10:
    day_fix= "0"+ str(birth_days[name_idx])

    birth_months[name_idx] = month_fix
    birth_days[name_idx] = day_fix

  surname = input("Please enter your surname: ").capitalize()

  if surname in surnames and surname == surnames[name_idx].capitalize():

    bday= input ("please enter your birthday as a DD/MM/YYYY: ")

    if len(bday)==10 and bday[2] == "/" and bday [5] == "/":
      temp=bday.split("/")
      day= int(temp[0])
      month = int(temp[1])
      year = int(temp[2])
      if day == birth_days[name_idx] and month == birth_months[name_idx] and year == birth_years[name_idx]:
        print ("you are a customer")
      else:
        print ("not a customer")
    else:
      print("wrong format")
  else:
    print ("not a customer!")
else:
  print ("not a customer!")
