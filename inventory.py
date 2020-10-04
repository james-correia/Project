#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:33:05 2020

@author: Christiaan Smith
         James Correia
"""
import csv

'''
Test comment
'''

class Inventory:

    def __init__(self):
        self.items = self.create_inventory()        
        
        
    def create_inventory(self):
        storage = []
        #csv_titles = ['book.csv','cd_vinyl.csv','collectible.csv','electronics.csv','fashion.csv','home_garden.csv']
        
        #Adds all books into inventory
        book_list = []
        csvfile = open('book.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            book_list.append(Book(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4],info_list[i][5],info_list[i][6],))
        
        
        #Adds all cd_vinyl in inventory
        cd_list = []
        csvfile = open('cd_vinyl.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            cd_list.append(CDVinyl(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4],info_list[i][5],info_list[i][6],))
       
        
        #Adds all collectibles to inventory
        collectibles_list = []
        csvfile = open('collectible.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            collectibles_list.append(Collectible(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4]))
       
        
        #Adds all electronics to inventory
        electronics_list = []
        csvfile = open('electronics.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            electronics_list.append(Ebay(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4]))
        
        
        #Adds all fashion to inventory
        fashion_list = []
        csvfile = open('fashion.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            fashion_list.append(Ebay(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4]))
        
        
        #Adds all home garden to inventory
        garden_list = []
        csvfile = open('home_garden.csv', 'r')
        reader = csv.reader(csvfile)
        info_list = list(reader)
        for i in range(len(info_list)):
            garden_list.append(Ebay(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3],info_list[i][4]))
        
        
        #Adding all individual objects into one master list
        storage.append(book_list)
        storage.append(cd_list)
        storage.append(collectibles_list)
        storage.append(electronics_list)
        storage.append(fashion_list)
        storage.append(garden_list)
        
        #Designates specific ID values for each item in storage
        #for i in range(len(storage)):
            #storage[i].id = i + 1
        
        return storage
    
    
    #Method to print specific parts of the inventory or the Inventory as a whole 
    def print_inventory(self, begin = 0, end = -1):
        if end == -1 and begin ==0:
            for x in self.items:
                print (x)
        else:
            for x in (begin,end):
                print (self.items[x-1])
    
    #Checks the type of an indicated Item in an Inventory
    def check_type(self, item):
        return str(isinstance(self.items[item]))
      
    #This method computes the total price of every item in the Inventory
    def compute_inventory(self):
        total=0
        for x in self.items:
            total+=(x.unit_price)*(x.quantity)
        return total
            
    #Method that will return all objects from an Inventory of the specified type
    def print_category(self, cat_name):
        for x in self.items:
            if cat_name == str(isinstance(x)):
                print(x)
    
    #Method that will return a list of all objects in a Inventory with a specified name/title
    def search_item(self, item_name):
        temp_list=[]
        for x in self.items:
            if item_name in x.name:
                temp_list.append(x)
        return temp_list


#Basic Item class which stores all the basic information every item has   
class Item():
    def __init__(self, title, price, quantity, date):
        self.id = -1
        self.name = title
        self.price = price
        self.quantity = quantity
        self.date = date

    def __str__(self):
        return "------------\nID: " + str(self.id) + "\nName: " + str(self.name) + "\nPrice: " + str(self.price) + "\nQuantity: " + str(self.quantity)
    
    def __repr__(self):
        self.__str__()
    
           
#Book class which inherits Items
#stores extra information pertaining to books   
class Book(Item):
    def __init__(self, title, date, publisher, author, price, ISBN, quantity):
        super().__init__(title, price, quantity, date)
        self.publisher = publisher
        self.author = author
        self.ISBN = ISBN
     
    def __str__(self):
        return super().__str__() + ("\nAuthor: " + str(self.author) + "\nPublish: " + str(self.publisher) + "\nISBN:" + str(self.ISBN))


#CD/Vinyl class which inherits Items
#stores extra information pertaining to CD/Vinyls  
class CDVinyl(Item):
    def __init__(self, title, artist, label, ASIN, date, price, quantity):
        super().__init__(title, price, quantity, date)
        self.artist = artist
        self.label = label
        self.ASIN = ASIN
        
    def __str__(self):
        return super().__str__() + ("\nArtist: " + str(self.artist) + "\nLabel: " + str(self.label) + "\nASIN: " + str(self.ASIN))

        
        
        
#Collectible class which inherits Items
#stores extra information pertaining to collectibles
class Collectible(Item):
    def __init__(self, title, price, date, owner, quantity):
        super().__init__(title, price, quantity, date)
        self.owner = owner

    def __str__(self):
        return super().__str__() + ("\nOwner: " + str(self.owner))


#Ebay item class which inherits Items
#stores extra information pertaining to Ebay Items
class Ebay(Item):
    def __init__(self, title, price, date, manufacturer, quantity):
        super().__init__(title, price, quantity, date)
        self.manufacturer = manufacturer
        
    def __str__(self):
        return super().__str__() + ("\nManufacturer: " + str(self.manufacturer))


    
    
    
    
    
    
    
