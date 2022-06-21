import pandas as pd
import sys
from math import radians
from geopy.distance import geodesic
 
 
file = pd.read_csv(r'dataset-starbucks_2018_11_06.csv', delimiter =',', index_col="state", encoding = "utf-8")
localDistributorName_list = []
totalDistance_list = []
coordinateLocalDistributor_list = []
 
def localDistributor(stateName):    
    min = sys.maxsize
    data = file.loc[stateName].head(7)
    print(data)
 
   
    for i in range(len(data)): # tukar origin
        sum = 0
        origin = data.iloc[[i]]
        for j in range(len(data)): 
            x1 = origin.latitude
            y1 = data.iloc[[j]].latitude
            x2 = origin.longitude
            y2 = data.iloc[[j]].longitude
            sum1 = distance(x1,y1,x2,y2)
           
            sum += sum1
            print(sum1,"km") # print sum of distance from origin store to other store
        print("Total distance from ",origin[['name']]," is : ", sum,"km")
        if(sum < min):
            min = sum
            min_store = origin
       
    totalDistance_list.append(min)
 
    print()
    print()
    print("LOCAL DISTRIBUTOR FOR ",stateName," is : ",)    
    print()  
    localDistributorName_list.append(min_store[['name']])
    print(str(min_store[['name','street_address']]))
    print()
    #print(type(min_store[['street_address']]))
    coordinate = (radians(min_store.latitude),radians(min_store.longitude))
    print("Coordinate: ",coordinate)
    coordinateLocalDistributor_list.append(coordinate)
    print("Total distance: ",min,"km")
    print()
    return min_store
 
 
 
def distance(x1,y1,x2,y2):
    x1 = radians(x1)
    y1 = radians(y1)
    x2 = radians(x2)
    y2 = radians(y2)
 
    coords_1 = (x1,x2)
    coords_2 = (y1,y2)
 
    return geodesic(coords_1, coords_2).km
 
 
 
 
def main():
    ca = localDistributor("CA")
    jp = localDistributor("JP")
    my = localDistributor("MY")
    qa = localDistributor("QA")
    sg = localDistributor("SG")
    i=0
    print()
    print()
    print(*localDistributorName_list,sep="\n")
    print()
    print(*coordinateLocalDistributor_list,sep="\n")
    print()
    print(*totalDistance_list,sep="\n")
 
if __name__ == "__main__":
    main()