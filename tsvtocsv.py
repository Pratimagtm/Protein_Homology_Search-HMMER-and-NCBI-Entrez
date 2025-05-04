#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:19:33 2023

@author: pratima
"""

import os, csv

def tabtocsv(file_list):
    csv_clist=[]
    
    rfile = inputfolder + file_list
    with open(rfile, 'r') as read:
        for line in read.readlines():
            if line.split()[0] != "#":
                csv_clist.append(line.split()[:5])

    filename= outputfolder+file_list+".csv"

    with open (filename, 'w')as filehandle:
        write= csv.writer(filehandle)
        for data in csv_clist:
            for item in data:
                filehandle.write(item + '\t')
            filehandle.write('\r\n')
    filehandle.close()
            
inputfolder ="../Documents/regulator/output/"
outputfolder="../Documents/regulator/outputcsv/"

file_list = []

for f in os.listdir(inputfolder):
    if f.endswith(".fasta.tab"):
        file_list.append(f)

        tabtocsv(f)