import pandas as pd
import numpy as np
import csv



from lxml import etree
import os, sys
from unidecode import unidecode


# Parsing For Article CSV Data File

def parseData(context):

    article_array = []
    #title = 'article'
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'booktitle':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'journal':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'mdate':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'month':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'publisher':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

         if elem.tag == 'cite':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

         if elem.tag == 'url':
            if elem.text:
                author_array.append(unidecode(elem.text))      
                       
    return article_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(article):
    columns=['id','author','booktitle','mdate','month','publisher','title','year','cite','url']
    with open ("article.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in article:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('article.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




article=["dblp.xml"]
createCSV(article)











# Parsing For Book CSV Data File


def parseData(context):

    book_array = []
    title = book
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'booktitle':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'mdate':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'month':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'publisher':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        

         if elem.tag == 'url':
            if elem.text:
                author_array.append(unidecode(elem.text))      
                       
    return book_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(book):
    columns=['id','author','booktitle','mdate','month','publisher','title','year','url']
    with open ("book.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in book:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('book.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




book=["dblp.xml"]
createCSV(book)












# Parsing For Incollection CSV Data File


def parseData(context):

    incollection_array = []
    title = incollection
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'booktitle':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'cite':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'mDate':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'publisher':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

         if elem.tag == 'url':
            if elem.text:
                author_array.append(unidecode(elem.text))      
                       
    return incollection_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(incollection):
    columns=['id','author','bookTitle','cite','Mdate','publisher','title','year','url']
    with open ("incollection.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in incollection:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('incollection.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




incollection=["dblp.xml"]
createCSV(incollection)










# Parsing For Inproceeding CSV Data File


def parseData(context):

    inproceeding_array = []
    title = inproceeding
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'booktitle':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'cite':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'mDate':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'publisher':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

         if elem.tag == 'url':
            if elem.text:
                author_array.append(unidecode(elem.text))      
                       
    return inproceeding_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(inproceeding):
    columns=['id','author','bookTitle','cite','Mdate','publisher','title','year','url']
    with open ("inproceeding.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in inproceeding:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('inproceeding.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




inproceeding=["dblp.xml"]
createCSV(inproceeding)












# Parsing For MasterThesis CSV Data File



def parseData(context):

    masterThesis_array = []
    title = masterThesis
    


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
        
        if elem.tag == 'school':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
      
                       
    return masterThesis_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(masterThesis):
    columns=['id','author','mDate','school','title','year']
    with open ("masterThesis.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in masterThesis:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('masterThesis.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




masterThesis=["dblp.xml"]
createCSV(masterThesis)














# Parsing For PhdThesis CSV Data File



ef parseData(context):

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














# Parsing For WWW CSV Data File

ef parseData(context):

    www_array = []
    title = www
    


    for event, elem in context:

        if elem.tag == 'id':
            if elem.text:
                author_array.append(unidecode(elem.text))


        if elem.tag == 'author':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

        if elem.tag == 'cite':
            if elem.text:
                author_array.append(unidecode(elem.text))
        
        if elem.tag == 'editor':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'mDate':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'publisher':
            if elem.text:
                author_array.append(unidecode(elem.text))
                
        if elem.tag == 'title':
            if elem.text:
                author_array.append(unidecode(elem.text))

        if elem.tag == 'year':
            if elem.text:
                author_array.append(unidecode(elem.text))
                

         if elem.tag == 'url':
            if elem.text:
                author_array.append(unidecode(elem.text))      
                       
    return www_array




def arrangeFormat(result):
   
   for in (len(columns))
        xml_copy_list=[]
        xml_copy_list.append(result[i])
        return xml_copy_list



def createCSV(www):
    columns=['id','author','cite','editor','Mdate','publisher','title','url','year']
    with open ("www.csv", 'a') as csvfile:
            header = columns
            writeFiles = csv.Dict(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)


    for i in www:
        context = etree.iterparse(i, load_dtd=True,html=True)
        result=parseData(context)
        result1=arrangeFormat(result)
        df=pd.DataFrame(data=np.asarray(result1).reshape(1,len(columns)))
        with open('www.csv', 'a') as f:
            df.to_csv(f, header=False,index=False)




www=["dblp.xml"]
createCSV(www)