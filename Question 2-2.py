from math import atan2, cos, sin, sqrt, pi
import pandas as pd
from sys import maxsize
from itertools import permutations
import gmplot
#---------------------------------------------------------------------------------------------------------------------------------------

#calculate distance from one store to another store (first store, second store)
def distance(first,second):

    r = 6371
    dlat = degToRad(second[1] - first[1])
    dlong = degToRad(second[0] - first[0]) #second[1] - first[1]
    x = sin (dlat/2) * sin (dlat/2)
    y = cos (degToRad(first[1]) * cos(degToRad(second[1]))) #degToRad(first[0]) * cos(degToRad(second[0]))
    z = sin(dlong/2) * sin(dlong/2)
    a = x+y*z
    c = 2 * atan2(sqrt(a),sqrt(1-a))
    d = r*c
    return d

    

# convert degree to radian
def degToRad(deg):
   return deg * (pi/180)

#-------------------------------------------------------------------------------------------------------------------------------

v = 6
center = 0
def computeShortestPath(listdistance,center):
   vertex = []
   for i in range(v):
       if i!=center:
           vertex.append(i)

   mindistance = maxsize

   vertexPermute = permutations(vertex)


   for i in vertexPermute:
       currentdistance = 0
       k=center
       for j in i:
           currentdistance += listdistance[k][j]
           k = j
       currentdistance += listdistance[k][center] #add distance from last node to the initial node

       if(currentdistance<=mindistance):
           mindistance = min(mindistance, currentdistance)
           path = i

   return {'mindistance':mindistance, 'path':path, 'center':center}

#------------------------------------------------------------------------------------------------------------------------

# to plot on google map
def plot(path,stores):
   location = [[0 for i in range(len(stores))] for j in range (len(stores))]
   location[0] = stores[0]
   j=1
   for i in path: #to sort the stores location (long,lat) according to the sorted path
       location[j]=stores[i]
       j=j+1

   #transfer long and lat from 2d array to 1d array
   lat=[]
   long=[]
   for i in range(len(location)):
       long.append(location[i][1]) #location[i][0]
       lat.append(location[i][0]) #location[i][1]

   # print(lat)
   # print(long)

   mapping = gmplot.GoogleMapPlotter(lat[0],long[0],zoom=15,apikey="")
   mapping.plot(lat,long,'blue',edge_width = 2.5) # to connect the location from 1 store to another store

   # to connect the last store to deliver to the starting store
   lastPath = zip(*[
       (lat[len(lat)-1],long[len(long)-1]),
       (lat[0],long[0])
   ])
   mapping.plot(*lastPath,'blue',edge_width = 2.5)

   # to mark the stores according to their original number
   j=0
   # print("path",path)
   for i in range(len(location)):
       if (i==0):
           mapping.marker(lat[i],long[i], label=0, color="green")
       else:
           mapping.marker(lat[i],long[i], label=path[j], color="green")
           j=j+1
  
   mapping.draw("map.html")

#------------------------------------------------------------------------------------------------------------------------

#read location(long,lat) from text file
def readFile(file):
   with open(file) as textFile:
       line_array = textFile.read().splitlines()
       location = [line.split(",") for line in line_array]

   floatLocation = [[0 for i in range (len(location[0]))] for j in range (len(location))]
   for i in range(len(location)):
       for j in range (len(location[0])):
           floatLocation[i][j] = float(location[i][j])
  
   return floatLocation


#------------------------------------------------------------------------------------------------------------------------

#driver code
if __name__ == "__main__":

   prompt = "\nSelect country: \n1- Malaysia\n2- Japan\n3- Canada\n4- Singapore\n5- Qatar\n\nEnter number: "
   num = input(prompt)
   if num == "1":
       country = "Text Files - Country Stores\malaysia_stores.txt"
   elif num == "2":
       country = "Text Files - Country Stores\japan_stores.txt"
   elif num == "3":
       country = "Text Files - Country Stores\canada_stores.txt"
   elif num == "4" :
       country = "Text Files - Country Stores\singapore_stores.txt"
   else :
       country = "Text Files - Country Stores\qatar_stores.txt"

   print("")
   stores = readFile(country)
   print("Store\tLatitude\tLongitude")
   for i in range(len(stores)):
       print(i,"\t",stores[i][0],"\t",stores[i][1])
   print()

   #calculate distance from one store to another store
   listdistance = [[0 for i in range(len(stores))] for j in range (len(stores))] #matrix representation graph
   center = stores[0]
   for i in range (len(stores)):
       for j in range (len(stores)):
           listdistance[i][j] = float(distance(stores[i],stores[j]))

   #print all dinstance
   print("Matrix representation distance (km): \n")
   print("Eg:")
   print("[ 0 3 ] means distance from Store 0 to Store 3\n")
   for i in range(len(stores)):
       for j in range(len(stores)):
           print("[ ",i,j," ]", end=" ")
       print()

   print()
   for i in range (len(stores)):
       print(listdistance[i])
   print("\n")

   # compute shortest path for delivery
   # center=0
   print("********** Computing Shortest Path For Delivery **********")
   ret = computeShortestPath(listdistance, center=0)
   print("\nLocal Distribution Center (starting and ending): ",ret['center'],center)
   print("Shortest Path: ", ret['path'])
   print("Total Distance: ", ret['mindistance'],"km\n")
   plot(ret['path'], stores)