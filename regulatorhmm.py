#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:41:46 2023

@author: pratima
"""


import json
from Bio import Entrez, SearchIO
import xml.etree.ElementTree as ET
import os, os.path, csv, datetime, copy
from os import path
import subprocess

Entrez.email ="abc@abc.com"

def call_hmmer(hmmscan_arg):
    
    print('---- Start call hmmer, Creating .tab file ----')
    subprocess.call(hmmscan_arg, stdout=open(os.devnull, 'w'))
    print('----Call hmmer Ended----')
    #read tab file and create a list of TF potein accession.
    
    #select_TF(hmmscan_output, samplelist)
    
    
def run_hmmer(hmminputfile, eval, DB_path):
    #print(eval, DB_path, hmminputfile)

    print('---start run hmmer---')
    hmmscan_arg = (['hmmscan','--tblout', hmmscan_output, '-E', str(eval), \
                    str(DB_path), hmminputfile])
    print('---Run hmmr ended---')
    call_hmmer(hmmscan_arg) 
    
def parse(biosampleacc):
    biosample= samplelist.partition(" ") [0]
    #print(biosample)
    handle = Entrez.esearch(db="nuccore",term=(biosampleacc), idtype='acc',retmax=400, usehistory="y")
#   Entrez.parse(handle)
    Element =ET.parse(handle)
    xmlElement= Element.getroot()
    reflist= []
    gbklist= []
    genomelist = []
    
    for IdList in xmlElement.findall("IdList"):
        for Id in IdList.iter("Id"):
        #    value = Id.find("Id").text
            if "_" in Id.text:
                reflist.append(Id.text)
            else:
                gbklist.append(Id.text)    
        
        if len(reflist) == 0:
            genomelist = gbklist
        else:
            genomelist =reflist
            
    outputfile= "../regulator/genome/"+ biosampleacc +".fasta"
    out_handle = open(outputfile, "w")
    
    for genomeid in genomelist:     
        handleprotein = Entrez.efetch(db="nuccore",id=str(genomeid),
                                      rettype='fasta_cds_aa', retmode="text")
#       print(outputfile)
        out_handle.write(handleprotein.read())
    
        
    out_handle.close()
# open and read json file, assign biosampleId to a list. iterate list and assign to a variable
Inputfilename = "../input.json"
fastapath= "../regulator/genome/"
with open('input.json') as json_file:
    data = json.load(json_file)
    
# create a variable to hold dbPath value for later use.
eval = data["Hmmer"]["Max_eval"] 
DB_path = data["Hmmer"]["DB_path"]

 # create a fasta file using hmm scan, for genome accession number from json file. 
biosampleid = []    
for genome in data['Genomes']: #from json file
    biosampleid.append(genome["Biosample"] + " " + genome["Name"])
    
#print(biosampleid)
# create a tab file using hmm scan, for genome accession number from json file, using fasta file.
for samplelist in biosampleid:
    parse(samplelist)
    
fastafile_list = []
isfile = os.path.exists(fastapath)
for f in os.listdir(fastapath):
    if f.endswith(".fasta"):
        fastafile_list.append(f)
for fastafile in fastafile_list:
    hmminputfile= fastapath+fastafile
    hmmscan_output="../regulator/output/"+ fastafile +".tab"
    run_hmmer(hmminputfile, eval, DB_path) #outputfile from parse(biosampleacc) is an input for HMMER search.