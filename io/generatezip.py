# -*- coding: utf-8 -*-
"""
Generates nested folders for each zip code
"""

from uszipcode import SearchEngine
import os
import json
# from tabulate import tabulate

def main():
    search = SearchEngine(simple_zipcode=True)
    
    for prefix in ["3031"]: #range(10):
        print("Analyzing prefix: " + prefix)
        zipcodes = search.by_prefix(prefix)#all zipcodes starting with prefix
        for z in zipcodes:
            zipcode_split = [char for char in z.zipcode]
            filepath = "data/"
            for digit in zipcode_split:
                filepath += digit +"/"
                if not os.path.exists(filepath):
                    os.mkdir(filepath)
            
            #write json file
            zip_dict = z.to_dict()
            with open(filepath + 'zipinfo.json', 'w') as outfile:
                json.dump(zip_dict, outfile, indent=4)
            
            #clean dictionary for md file
            # cleaned_zip_dict = {}
            # for key, value in zip_dict.items():
            #     #capitalize keys and replace underscore with spaces
            #     key = key.capitalize().replace("_", " ")
            #     #clean up lat and long
            #     if key == "Lat":
            #         key = "Latitude"
            #     elif key == "Lng":
            #         key = "Longitude"
            #     #convert lists to comma separated strings
            #     if isinstance(value, list):          
            #         value = ", ".join(value)
            #     #comma separate numbers
            #     elif isinstance(value, int) | isinstance(value, float):
            #         value = "{:,}".format(value)
            #     cleaned_zip_dict[key] = value
                # outfile.write(tabulate(cleaned_zip_dict.items(), tablefmt='github'))    
                
            #clean data and write md file 
            with open(filepath + 'zipinfo.md', 'w') as outfile:
                outfile.write(z.zipcode + '\n=====\n') #md file header
                # outfile.write('|Zipcode|' + zip_dict['zipcode'] + 
                #               '|\n|--|--|\n') #table header
                # zip_dict.pop('zipcode')
                outfile.write('|--|--|\n') #table header'
                for key, value in zip_dict.items():
                    #capitalize keys and replace underscore with spaces
                    key = key.capitalize().replace("_", " ")
                    #clean up lat and long
                    if key == "Lat":
                        key = "Latitude"
                    elif key == "Lng":
                        key = "Longitude"
                    #convert lists to comma separated strings
                    if isinstance(value, list):          
                        value = ", ".join(value)
                    #comma separate numbers
                    elif isinstance(value, int) | isinstance(value, float):
                        value = "{:,}".format(value)
                    outfile.write('|' + key + "|" + value + '|\n')
                

                
if __name__== "__main__":
   main()