# Module 4 Table


resdata = [['Golden island' ,'Around Campus','Chinese','https://goo.gl/maps/3zQXDAaT3ySVWqpA6',4.2,115],
['Tossing Pizza','Around Campus','Italian','https://goo.gl/maps/4TpQmM7WWmmZHyLCA',3.8,109],
['CRAFT','Downtown','Canadian','https://goo.gl/maps/NWo2ELGLaTQYtLJ17',4.3,1683],
['Cactus Club','Downtown','Canadian','https://goo.gl/maps/RmsGijZ2kTZ6BSxS6',4.4,1870],
['Pho Soc Trang','Downtown','Vietnamaese','https://goo.gl/maps/siWnih6ufA2f4EkH8',4.4,436],
['O Machi' ,'Glenmore' ,'Taiwanese','https://goo.gl/maps/oMrAAAv2PzHG1Dy38',4.8,178],
['Ozeki','Glemnore','Japanese','https://goo.gl/maps/hbptDNAZKDSYi4sg8',4.5,916],
['New Punjab','Rutland','Indian','https://goo.gl/maps/j8EtHEfTRwFC4brH7',4,520],
['eMDees Indian Bistro','Rutland','Indian','https://goo.gl/maps/DJqqFb5eF3QwPQML9',3.5,95]]

import pandas as pd
import numpy as np
from .Restaurant import Restaurant

class Table(Restaurant):
    def __init__(self,name ='NA',
                 location='NA',
                 cuisine='NA',
                 maplink='NA',
                 cust_rating='NA',
                 cust_num='NA',tables='NA',seats=[],data = 0,seat_map = 0):
        Restaurant.__init__(self,name,location,cuisine,maplink,cust_rating,cust_num)
        self.tables = tables
        self.data = data
        self.seats = seats
        self.seat_map = seat_map

    def setTable(self):
        data = np.zeros((self.tables,5))
        self.seat_map = pd.DataFrame(data, index = range(1,self.tables+1), columns=["10am:12pm","12pm:02pm","02pm:04pm","04pm:06pm","06pm:08pm"])
        self.seat_map.insert(0, "Seater", self.seats)
        self.seat_map.index.name = "Table number"

    def emptyTable(self,time_slot):
        if time_slot == 1:
            time = "10am:12pm"
        elif time_slot == 2:
            time = "12pm:02pm"
        elif time_slot == 3:
            time = "02pm:04pm"
        elif time_slot == 4:
            time = "04pm:06pm"
        else:
            time = "06pm:08pm"
        empty =self.seat_map.loc[self.seat_map[time] == 0]
        print("\n",empty[["Seater"]])
        return time

    def bookTable(self,t_num,time_slot):
        if time_slot == 1:
            time = "10am:12pm"
        elif time_slot == 2:
            time = "12pm:02pm"
        elif time_slot == 3:
            time = "02pm:04pm"
        elif time_slot == 4:
            time = "04pm:06pm"
        else:
            time = "06pm:08pm"

        if self.seat_map.at[t_num,time] == 0:
            self.seat_map.at[t_num,time] =1
            print("Hurray🎉!! Table is booked")
        else:
            print("Sorry, table is already booked")



# initi Table Instance

tabledata = [[4,[5,6,7,8]],
             [3,[2,3,4]],
             [4,[4,4,4,6]],
             [4,[8,8,8,8]],
             [5,[4,4,4,8,8]],
             [4,[2,2,4,4]],
             [6,[2,2,2,4,4,4]],
             [3,[8,8,8]],
             [5,[3,4,5,6,7]]]

tableList = [Table(name = resdata[i][0],
                      location = resdata[i][1],
                      cuisine = resdata[i][2],
                      maplink = resdata[i][3],
                      cust_rating = resdata[i][4],
                      cust_num = resdata[i][5],
                   tables = tabledata[i][0],
                     seats = tabledata[i][1]) for i in range(len(resdata))]


setTableList = [table.setTable() for table in tableList]


#[print(table.emptyTable(3)) for table in tableList]
#[print(table.seat_map) for table in tableList]
#[table.bookTable(2,3) for table in tableList]
