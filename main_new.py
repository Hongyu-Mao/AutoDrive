import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Mcity_11_2021"]
mycol = mydb["USA_MICHIGAN_2"]

# left
leftList = []
for col in mycol.find():
    id = col['_id']
    for xSection in col['xSection']:
        matrix = [int(id), int(xSection['_id']), float(xSection['leftEdge']['_lat']), float(xSection['leftEdge']['_long'])]
        leftList.append(matrix)

# right
rightList = []
for col in mycol.find():
    id = col['_id']
    for xSection in col['xSection']:
        matrix = [int(id), int(xSection['_id']), float(xSection['rightEdge']['_lat']), float(xSection['rightEdge']['_long'])]
        rightList.append(matrix)

def distance(mylist, lat, long):
    for list in mylist:
        dis = (list[2] - lat) ** 2 + (list[3] - long) ** 2
        list.append(dis)
    return sorted(mylist, key=(lambda x: x[4]))[0:100]

# leftEdge
left_lat = 42.30000200
left_long = -83.69867437
left = distance(leftList, left_lat, left_long)
print(left)

# rightEdge
right_lat = 42.30003093
right_long = -83.69874326
right = distance(rightList, right_lat, right_long)
print(right)