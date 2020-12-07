# -*- coding: utf-8 -*-
"""
Generates nested folders for each zip code
"""

from uszipcode import SearchEngine
import os
import json
from tabulate import tabulate

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
            
            #write md file (after converting lists to comma separated strings)
            for key, value in zip_dict.items():
                if isinstance(value, list):
                    zip_dict[key] = ", ".join(value)            
            with open(filepath + 'zipinfo.md', 'w') as outfile:
                outfile.write(z.zipcode + '\n=====\n')
                outfile.write (tabulate(zip_dict.items(), tablefmt='github', 
                         headers = ['Variable', 'Value']))    

                
if __name__== "__main__":
   main()