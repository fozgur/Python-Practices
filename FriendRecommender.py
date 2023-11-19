def GetFriends(id):
  return refined_data.get(id, list())

def GetFriendsofFriends(id):
  foflist = []
  for friend in GetFriends(id):
    temp = GetFriends(friend)
    for item in temp:
      foflist.append(item)
  foflist = [f for f in foflist if f != id] 
  return foflist

def recommender(id):
  count = {}
  recommend = []
  temp = GetFriendsofFriends(id)
  for friend in temp:
    if friend not in GetFriends(id):
      count[friend] = temp.count(friend)
  if not count:
    pass
  else:
    max_val = max(count.values())
  for k,v in count.items():
    if v == max_val:
      recommend.append(int(k))
  recommend.sort()
  return recommend

##Main##
refined_data={}

path = ("friendship.txt")

with open(path) as friends:
  data = friends.readlines()

for line in data:
  key, value = map(int, line.strip().split('\t'))
  try:
    refined_data[key].append(value)
  except:
    refined_data[key] = [value]
  try:
    refined_data[value].append(key)
  except:
    refined_data[value] = [key]    


id = int(input("Enter a user id to suggest some friends: "))

if id in refined_data.keys():
  friendrec = recommender(id)
  strlist = []
  if friendrec:
    formatted = ', '.join(map(str, friendrec))
    print(formatted)
  else:
    print ("There is no friend to suggest")
else:
  print("There is no such user")
