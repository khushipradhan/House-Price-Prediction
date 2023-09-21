#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
#model=search_properties(csv_file, location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget)

def search_properties(csv_file, location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget):
    matching_properties = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            price = float(row['Price'])
            if (
                row['Locality'] == location
                and row['Type'] == property_type
                and row['Transaction'] == new_or_old
                and row['Bathroom'] == bath
                and row['BHK'] == bhk
                and row['Furnishing'] == furnished
                and int(min_budget) <= price <= int(max_budget)
            ):
                matching_properties.append(row)
            print(row['Locality'] + " " + row['Type'] + " " + row['Transaction']+ " " + row['Bathroom']+ " " + row['BHK'] +" "  +row['Furnishing'])
            break



    return matching_properties
'''
csv_file = "C:/Users/Madhav Pradhan/Downloads/buy3/MagicBricksedited.csv" 
location = 'Geeta Colony'
property_type = 'house'
new_or_old = 'Resale'
bath = 2
bhk = 3
furnished = 'Unfurnished'
min_budget = 5000000
max_budget = 10000000

results = search_properties(csv_file, location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget)

if results:
    print("Matching properties:")
    for property in results:
        print(property)
else:
    print("No matching properties found.")


# In[13]:


#import pickle 
#pickle.dump(search_properties,open('buymodel2.pkl','wb'))


# In[ ]:

'''


