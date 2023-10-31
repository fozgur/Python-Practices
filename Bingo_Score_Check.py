granny = input("Enter the numbers on grandmother's card: ").split("-")
me = input("Enter the numbers on your card: ").split("-")
sack = input("Enter the numbers to be drawn from sack: ").split("-")

temp_g = granny.copy()
temp_m = me.copy()

g_score = 0
m_score = 0

for stone in sack:
  print ("Selected number is", stone)
  if stone in granny:
    g_score += 1
    temp_g.remove(stone)
  if stone in me:
    m_score +=1
    temp_m.remove(stone)
  if m_score == len(me) or g_score == len(granny):
    break

if g_score==len(granny) and g_score != m_score:
  print("Grandmother won!")
  print("Your remaining numbers are as follows:")
  for item in temp_m:
    print(item)
elif m_score==len(me) and m_score != g_score:
  print("You won!")
  print ("Grandmother's remaining numbers are as follows:")
  for i in temp_g:
    print(i)
else:
  print ("There is a tie!")

