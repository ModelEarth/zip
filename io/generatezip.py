# -*- coding: utf-8 -*-
"""
Generates nested folders for each zip code using uszipcode (https://pypi.org/project/uszipcode/)
"""

from uszipcode import SearchEngine
import os
import json
# from tabulate import tabulate

def main():
    search = SearchEngine()
    
    #to increase run times (the search engine is slow to return results), provide the first 4 digits in a zip as a prefix to the search engine
    for prefix0 in range(10):
        for prefix1 in range(10):
            print("Analyzing prefix: " + str(prefix0) + str(prefix1))
            for prefix2 in range(10):
                for prefix3 in range(10):
                    prefix = str(prefix0) + str(prefix1) + str(prefix2) + str(prefix3)
                    #print("Analyzing prefix: " + str(prefix))
                    zipcodes = search.by_prefix(prefix, returns=11)#all zipcodes starting with prefix (default is to return 5, increasing to 1 more than expected)
                    #for each returned zip code, clean results and write out file
                    for z in zipcodes:
                        zipcode_split = [char for char in z.zipcode]
                        filepath = "data/"
                        for digit in zipcode_split:
                            filepath += digit +"/"
                            if not os.path.exists(filepath):
                                os.mkdir(filepath)
                        
                        zip_dict = z.to_dict()
                        
                        #round decimals
                        num_decimals = 2
                        for key, value in zip_dict.items():
                            if ('bounds' in key) & (not value is None):
                                zip_dict[key] = round(value, num_decimals)
                            elif (('percent' in key) | ('average' in key)) & (not value is None):
                                for sub_dict in value[0]['values']:
                                    if not sub_dict['y'] is None:
                                        sub_dict['y'] = round(sub_dict['y'], num_decimals)
                        
                        #write json file
                        with open(filepath + 'zipinfo.json', 'w') as outfile:
                            json.dump(zip_dict, outfile, indent=4)
                        
                        #clean data and write md file 
                        with open(filepath + 'zipinfo.md', 'w') as outfile:
                            outfile.write(z.zipcode + '\n=====\n') #md file header
                            outfile.write('|||\n|--|--|\n') #table header'
                            for key, value in zip_dict.items():
                                #capitalize keys and replace underscore with spaces
                                key = key.capitalize().replace("_", " ")
                                #clean up lat and long
                                if key == "Lat":
                                    key = "Latitude"
                                elif key == "Lng":
                                    key = "Longitude"
                                #clean up income
                                key = key.replace("income    ", "income, ")
                                key = key.replace("incom:", "income:")
                                #skip polygon
                                if key == "Polygon":
                                    continue
                                    
                                if isinstance(value, list):
                                    #split out dictionaries
                                    if len(value) == 0:
                                        value = None
                                    elif isinstance(value[0], dict):
                                        if ' by age' in key:
                                        #for populations by age, split out dictionary
                                        # if key in ['Population by age', 'Head of household by age', 'Children by age']:
                                            for group_dict in value: #value is a list of dictionaries by gender
                                                group = group_dict['key']
                                                age_dict = group_dict['values'] #values within this dictionary is a list of dictionaries from age to pop
                                                for age in age_dict:
                                                    outfile.write("|" + key + ": " + group.lower() +  ", " + 
                                                                  str(age['x']).lower() + " years old|" +
                                                                  "{:,}".format(age['y']) + "|\n")
                                            continue   
                                        else:
                                               #          if key in ['Population by year', 'Population by gender', 'Population by race', 
                                               # 'Families vs singles', 'Households with kids', 'Housing type',
                                               # 'Year housing was built', 'Housing occupancy', 'Vancancy reason', 
                                               # 'Owner occupied home values']:
                                            for sub_dict in value[0]['values']:
                                                outfile.write("|" + key + ": " + str(sub_dict['x']).lower() + "|" +
                                                              "{:,}".format(sub_dict['y']) + "|\n")
                                            continue 
                                    #convert lists to comma separated strings
                                    else: # isinstance(value, list):   
                                            if(isinstance(value[0], list)):
                                                value = [str(v) for v in value]
                                            value = ", ".join(value)
                                #comma separate numbers
                                elif isinstance(value, int) | isinstance(value, float):
                                    value = "{:,}".format(value)
                                outfile.write('|' + key + "|" + str(value) + '|\n')
                            

                
if __name__== "__main__":
   main()