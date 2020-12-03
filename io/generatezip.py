# -*- coding: utf-8 -*-
"""
Generates nested folders for each zip code
"""

from uszipcode import SearchEngine
import os
import json

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
            with open(filepath+'zipinfo.json', 'w') as outfile:
                json.dump(z.to_dict(), outfile, indent=4)
                
if __name__== "__main__":
   main()