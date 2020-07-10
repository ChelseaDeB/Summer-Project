#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:31:05 2020

@author: chelsea
"""

import urllib.parse 
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'

params = {
    'from' : 'ACC+ID',
    'to' : 'P_REFSEQ_AC', #RefSeq Protein = NCBI protein 
                          # or P_ENTREZGENEID  NCBI gene
    'format': 'tab',
    'query' : 'P40925 P40926 O43175 Q9UM73 P97793' #ACC+ID = UniProtKB AC/ID
    }

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
    response = f.read()
    
    print (response.decode('utf-8'))