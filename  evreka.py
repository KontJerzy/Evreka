#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:28:31 2021

@author: mustafa ahmet pesen
"""

import random
import datetime
from datetime import timedelta
import numpy as np
import pylab as plt

class generateRoute(object):
    nextIdNum = 0
    def __init__(self):
        '''
        Generates a random route data.

        n: integer, the number of the vehicles.
        
        First I designed this class to create multiple vehicles
        at a single line of code. But then I decided that might cause a
        confusion at first sight.
        '''
        
        # assert type(n) == int
        # self.VEHIC_NO = n
        
        # TIME_CONST: time constant, calculated as a vehicle with a speed of 
        # avarage 60km/sa takes to go 500m == 300sec or 5 min.
        self.TIME_CONST = 300
        # VERT_CONST: every created vertex will have same 500m, 0.5km length
        self.VERT_CONST = 0.5
        # create an id num for each route data
        self.idNum = generateRoute.nextIdNum
        generateRoute.nextIdNum += 1
        
        self.firstNum = '012345678'
        self.secondNum = '0123456789'
        self.alphabet = 'ABCDEFGHIİJKLMNOÖPRSŞTUÜVYZ'
        
        # a random route as km
        self.routeKm = random.randrange(100,400,1)
        
        # today's date
        self.today = datetime.datetime.now()

       

    def getIdNum(self):
        '''
        Incremental id number call function
        '''
        return self.idNum
            
    def plate(self):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        x = self.firstNum[random.randrange(0,len(self.firstNum))]
        y = self.secondNum[random.randrange(0,len(self.secondNum))]
        plate_char_num = random.randrange(1,4)
        list_char = []
        list_num = []
        for i in range(plate_char_num):
            list_char.append(self.alphabet[random.randrange(0,len(self.alphabet))])
            
            
        if plate_char_num<3: 
            for j in range(plate_char_num+1):
                list_num.append(self.secondNum[random.randrange(0,len(self.secondNum))])
        else:
            for j in range(plate_char_num-1):
                list_num.append(self.secondNum[random.randrange(0,len(self.secondNum))])
                
        self.plate = [x, y]+list_char+list_num
        
        return self.plate

    def dateTime(self):
        '''
        definition of timing period during the trip
        '''
        list_timing = []
        # 500m is 0.5 km so calculate how many vertices it will take
        vertices_no = self.routeKm * 2
        self.vertices = vertices_no
        for k in range(vertices_no):
            list_timing.append(self.today + timedelta(seconds=300))
        
        self.dateTime = list_timing
        
        return self.dateTime
    

    def latlon(self):
        """
        According to the randomly assigned route as km, this function
        will create the latitude and longitude properties as step function.
        for every timing duration, the new lat/long properties will be created
        As the step property is assigned as 500m, 0.5km; in each step there
        will be a angle which would convert the vertices into random routes.
        """
        # *
        generateRoute.dateTime(self)
        
        lat_rand = random.randrange(36,42,1) + float("{0:.2f}".format(random.uniform(0, 1)))
        self.lat_rand = lat_rand
        lon_rand = random.randrange(26,45,1) + float("{0:.2f}".format(random.uniform(0, 1)))
        self.lon_rand = lon_rand
        
        
        # 0.01 degree change in latitude and longitude is approximately 1.11km
        # at km accuracy, at the equator.
        lats_route = []
        lons_route = []
        
        for l in range(self.vertices):
            angle = random.randrange(0,20,1)
            
            #random angle for each vertex at latitudes
            lat_prime_deg = float("{0:.3f}".format(np.cos(angle)*self.VERT_CONST/111))
            #burada her hesaplamasında baştakine eklediği için süreklilik yok
            lat_rand += lat_prime_deg
            lats_route.append(lat_rand)
            
            
            #random angle for each vertex at longitudes
            lon_prime_deg = float("{0:.3f}".format(np.sin(angle)*self.VERT_CONST/111))
            lat_rand += lon_prime_deg
            lons_route.append(lat_rand)
            
        self.lats_route = lats_route
        self.lons_route = lons_route
        
        return lats_route and lons_route
    
    
    def plotRoute(self):
        """
        This function will plot the route 
        """
        generateRoute.dateTime(self)        
        generateRoute.latlon(self)
        
        plt.clf()
        plt.figure('route')
        plt.title('Route of Vehicle')
        plt.xlabel('Latitudes')
        plt.ylabel('Longitudes')
        plt.plot(self.lats_route, self.lons_route)
        
        
    def structure(self):
        """
        This function will create the structured table list
        """
        generateRoute.dateTime(self)        
        generateRoute.latlon(self)
        generateRoute.plate(self)
        
        last_points = []
        for m in range(len(self.lats_route)):
            last_points.append(
                {'latitude': self.lats_route[m],
                 'longitude': self.lons_route[m],
                 'vehicle_plate': self.plate,
                 'datetime': self.dateTime[m]})
        
        self.last_points = last_points
        
        return self.last_points
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        
    
k = generateRoute()
k.structure()
k.plotRoute()
