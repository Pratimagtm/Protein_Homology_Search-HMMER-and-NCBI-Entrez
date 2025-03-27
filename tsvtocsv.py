#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:19:33 2023

@author: pratima
for line in scores:
  splitted_line = line.split(' ')
  for values in splitted_line:
    value_as_int = int(values)
"""

import os, csv
'''
def filtereval(filename):
    e=float('8.5e-11')
    csv_listeval=[]
    
    with open(filename, 'r') as read:
        for line in read.readlines():
            line=line.rstrip()
            line=line.split("\t")
            l=line[-1]
            for value in l:
                value = float(l)
                print(value)
           # l=float(int(l))
            #print(l)
            
            if l == e:
               csv_listeval.append(line.split()[:5])
            print(csv_listeval)
 '''       
    #filename.close()
def tabtocsv(file_list):
    csv_clist=[]
    
    #for f in file_list():
     #   print(f)
    
    rfile=inputfolder+file_list
    with open(rfile, 'r') as read:
        for line in read.readlines():
            if line.split()[0] != "#":
                csv_clist.append(line.split()[:5])
                #if line.split()[4] = 1e**(-30):
                   # csv_listeval.append(line.split()[:5])
            
        #print(csv_clist)
        
    #writingtocsv
    filename= outputfolder+file_list+".csv"
  #  filename2= outputfolder+file_list+"e-30"+ ".csv"
    with open (filename, 'w')as filehandle:
        write= csv.writer(filehandle)
        for data in csv_clist:
            for item in data:
                filehandle.write(item + '\t')
            filehandle.write('\r\n')
    filehandle.close()
#'''            
   # #filtereval(filename)
            
            
 #'''       
            
   # f.close()
   # orthogroup.close
 

            
            
inputfolder ="/home/pratima/Documents/regulator/output/"
outputfolder="/home/pratima/Documents/regulator/outputcsv/"

file_list = []

for f in os.listdir(inputfolder):
    if f.endswith(".fasta.tab"):
        file_list.append(f)

        tabtocsv(f)       
#print(file_list)