
# Book_My_Spot 



## Brief Introduction

*Book_My_Spot* is a convenient nearby restaurant match and book platform. After users inputting their location, preferred cuisine type, and check in time, *Book_My_Spot* will list all matched restaurants nearby with details of the recommended restaurants including map link and review, and will help the customer to book the table and time slot they want to go.

## Packages and Fuctions

- Package : **Book_My_Spot**; helps to suggest list of restaurants with reviews for users according to their personal preference and book their spot for a particular slot.It also records the feedback from the user for the selected restaurant.
    - Sub Package 1 :**Data** ; helps to record user's preference and suggest restaurants accordingly. 
        - Module 1 : **CustomerInteraction** : Interacts with user and record their response
          - Function 1: **initialize()**: it creates all the objects for the modules in sub-package-2.Each object contains the information of the restaurant and the tables it has.
          - Function 2: **greeting()**:  greets the user as he/she proceed for looking for restaurants.
          - Function 3: **location()**:  records the preferred restaurant location from the user
          - Function 4: **cuisine()**:  records the preferred crusine that the user want to have
          - Function 5: **record()**: creates the object for user preferrance with location and cuisine type.
          - Function 6: **askbooking()**: records the name of the restaurant that user wants to book from the list of suggested restaurants.
          - Function 7: **checkin()**: records the  expected time of arrival of the user once he/she proceeds to reserve a table in the selected restaurant.
          
        - Module 2 : **Database**
          - Function 1: **restInfo()**: calls the table class which inherits from Restaurant class to provide the list of suggestions on restaurants based on location and cuisine type.
          - Function 2: **chosenTable()**: matches the name of the user created object with the name of list of objects of the database of restaurants.
          - Function 3: **askFeedback()**: asks user to provide the rating for the selected if and only if he/she agrees to provide that information.
          
     - Sub Package 2: **Structure**;  This package has the inheritance in which class Restaurant is the parent and class Table is the child. It helps in perform several operations on the instances created and also for fetching required details regarding the objects.
        - Module 1 : **Restaurant** : Parent class which provides the details of the suggested restaurants as per user requirements.
          - Function 1: **__init__()**: initializes information of the restaurant such as name, location, cuisine, maplink (which is link to the restaurant), rating and the number of customer that reviewd the particular restaurant.
          - Function 2: **getRest()**: displays all the information of the restaurants such as name, maplink, rating with the total number of customers that reviewed it based on the inputs given by the user for the choice of location and cuisine type. 
          - Function 3: **updateRating()**: updates the rating of the restaurant selected by the user based on the given rating by the user.
          - Function 4: **updateCustomer()**: update the count of total number of people if the user has given his/her rating for the selected restaurant.
          
        - Module 2 : **Table** : Child class of class Restaurant.This module contains the information of the tables in each restaurant.
          - Function 1: **__init__()**: initializes information such as number of tables with its total occupancy.
          - Function 2: **setTable()**: each restaurant has the seat map dataframe which is basically the total number of tables in each restaurant v/s the timeslot with all the enteries as 0 which means the particular table is not booked for that particular timeslot.This dataframe also contains the total occupancy limit for each table.
          - Function 3: **emptyTable()**: it displays the table numbers with its occupancy based on the selected timeslot of dine-in for the selected restaurant.
          - Function 4: **bookTable()**: it changes the status of the selected table number for selected timeslot of selected restaurant from 0 to 1 which indicates that the table is booked for that timeslot. 
          
