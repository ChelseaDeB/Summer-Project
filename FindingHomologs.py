#!/usr/bin/env python3
# -*- coding: utf-8 -*-


''' 
Given the output of BLAST+ in the output format 5, which outputs an xml 
file, this file will check if the proteins found in the blast search are 
homologous and then output a file with the IDs of the homologos names 
Homologous.txt . 

The xml output file from the BLAST+ search is to be called results.xml

video used: https://www.youtube.com/watch?v=r6dyk68gymk
'''

import xml.etree.ElementTree as ET
mytree = ET.parse('results.xml') #parses the xml file
myroot=mytree.getroot() #gets root
    
#Hits points to the beginning of the sequences that were hits    
Hits=myroot[8][0][4]
 

#finds the len of the sequence a blast search was done on, 
#then converts the number from a str type to an int.
BlastOutput_queryLen=int(myroot[6].text)

Homologs=[] #keeps track of any Homologous

'''
loops through the results.xml file's hits to check if they are
homologos by checking if the homologous segment pairs cover at least 80% 
of the protein length and if their similarity is over 35%.
'''
for x in Hits.findall('Hit'):
    
    #extracting necessary data
    result_id=x.find("Hit_accession").text
    alignLen=int(x[5][0].find('Hsp_align-len').text)
    HspPos=int(x[5][0].find('Hsp_positive').text)
   
    #checking
    if (alignLen/BlastOutput_queryLen >= 0.8) and (HspPos/alignLen >= 0.35):
        #if they are homologos the protein's id is saved
        Homologs.append(result_id)

HomologsFile = open("Homologs.txt", "w")

HomologsFile.writelines("Protein understudy: \n")

HomologsFile.writelines(myroot[5].text)

HomologsFile.writelines("\nHomologs found:\n")

for h in Homologs:
    HomologsFile.writelines(h + "\n")

HomologsFile.close
