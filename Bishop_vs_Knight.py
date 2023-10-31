#!/usr/bin/env python
# coding: utf-8

# In[1]:


h = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
v = [1,2,3,4,5,6,7,8]

knight_h = input ("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ").lower().strip()

if knight_h.isalpha() == True and len(knight_h) == 1:
  if knight_h in h:
    knight_v = input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ").strip()
    if knight_v.isdigit() == True and int(knight_v) > 0:
      if int(knight_v) in v:
        bi_h = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ").lower().strip()
        if bi_h.isalpha() == True and len(bi_h) == 1:
          if bi_h in h:
            bi_v = input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ").strip()
            if bi_v.isdigit() == True and int(bi_v) >= 1:
              if int(bi_v) in v:
                delta_h = abs(ord(knight_h) - ord(bi_h))
                delta_v = abs(int(knight_v) - int(bi_v))
                if knight_h != bi_h or knight_v != bi_v:
                  if delta_h == delta_v:
                    print ("Bishop can attack knight")
                  elif (delta_h == 2 and delta_v == 1) or (delta_h == 1 and delta_v == 2):
                    print ("Knight can attack bishop")
                  else:
                    print ("Neither of them can attack each other")
                else:
                   print ("They can't be in the same square")
              else:
                print ("Vertical input for bishop is not a proper number")
            else:
              print ("Vertical input for bishop is not a number")
          else:
            print ("Horizontal input for bishop is not a proper letter")
        else:
          print ("Horizontal input for bishop is not a letter")
      else:
         print ("Vertical input for knight is not a proper number")
    else:
      print ("Vertical input for knight is not a number")
  else:
    print ("Horizontal input for knight is not a proper letter")
else:
  print ("Horizontal input for knight is not a letter")


# In[ ]:




