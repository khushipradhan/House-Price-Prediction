#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
#model=search_properties(csv_file, location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget)

def search_properties(csv_file, location, property_type, new_or_old, bath, bhk, furnished, min_budget, max_budget):
    matching_properties = []

    with open("c:\Users\Madhav Pradhan\Downloads\Search_properties.py", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            price = float(row['Price'])
            if (
                row['Locality'] == location
                and row['Type'] == property_type
                and row['Transaction'] == new_or_old
                and int(row['Bathroom']) == bath
                and int(row['BHK']) == bhk
                and row['Furnishing'] == furnished
                and min_budget <= price <= max_budget
            ):
                matching_properties.append(row)

    return matching_properties

csv_file = r"C:\Users\Madhav Pradhan\Downloads\buy3\MagicBricks.csv" 
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




