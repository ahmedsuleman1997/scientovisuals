import pandas as pd
import numpy as np
import csv



from lxml import etree
import os, sys
from unidecode import unidecode


def parseData(context):

    phdThesis_array = []
    title = phdThesis
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'mdDate':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'month':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
      
                       
    return phdThesis_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(phdThesis):
    columns=['id','author','mDate','month','title','year']
    with open ("phdThesis.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in phdThesis:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('phdThesis.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




phdThesis=["dblp.xml"]
createCSV(phdThesis)