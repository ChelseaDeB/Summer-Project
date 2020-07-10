#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse 
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'

params = {
    'from' : 'ACC+ID', #ACC+ID = UniProtKB AC/ID
    'to' : 'P_REFSEQ_AC', #RefSeq Protein = NCBI protein 
                          # or P_ENTREZGENEID  NCBI gene
    'format': 'tab',
    'query' : 'Q239Q2 Q236L2 A4VDZ5' 
    }

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
    response = f.read()
    
    print (response.decode('utf-8'))
    
""" 
    This function is used to convert a Uniprot Id into a NCBI protein 
    ID. ONce called it will prompt the user to input the IDs they wish
    to convert. The IDs will be converted and the NCBI IDs will be printed
    to the screen
    
"""
    
def Convert():
    print('input the Uniprot ID of the protein') 
    queryString = input() #saves the inputed string 
    params = {
    'from' : 'ACC+ID', #ACC+ID = UniProtKB AC/ID
    'to' : 'P_REFSEQ_AC', #RefSeq Protein = NCBI protein 
                          # or P_ENTREZGENEID  NCBI gene
    'format': 'tab',
    'query' : queryString 
    }
    
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read()
    
        print (response.decode('utf-8'))

Convert()
    