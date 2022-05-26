__author__ = "Sam K. Kamau"
__license__ = "MIT"
__maintainer__ = "Sam K. Kamau"
__contact__ = "twitter.com/samkamauk"

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt


country_list = ["Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon",
                "Cape Verde", "Central African Republic", "Chad", "Comoros", "Republic of the Congo", "Democratic Republic of the Congo",
                "Djibouti", "Egypt", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana",
                "Guinea", "Guinea Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali",
                "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria",
                "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone",
                "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

file_name_prefix = "Most-Specialized-Products-by-RCA-Index_"
specialization_data_df = pd.read_csv(file_name_prefix + 'Algeria.csv')
# add a column for country name
specialization_data_df['Country'] = "Algeria"

# read in each dataset
for i in range(len(country_list)):
    file_name = file_name_prefix + country_list[i] + '.csv'
    df = pd.read_csv(file_name)
    # add country name column to dataframe
    df['Country'] = country_list[i]
    specialization_data_df = pd.concat([specialization_data_df, df], axis=0)


# explore the data
# print data exploration
#print("checking specialization data")
# print(specialization_data_df.head())
# print(specialization_data_df.info())
# print(specialization_data_df.describe())

relatedness_file_name_prefix = "Export-Opportunities-by-Relatedness"
relatedness_data_df = pd.read_csv(relatedness_file_name_prefix + '.csv')
# read in each relatedness dataset
for i in range(2, 50):
    file_name = relatedness_file_name_prefix + " " + str(i) + '.csv'
    df = pd.read_csv(file_name)
    relatedness_data_df = pd.concat([relatedness_data_df, df], axis=0)

# explore relatedness data
# print data exploration
#print("checking relatedness data")
# print(relatedness_data_df.head())
# print(relatedness_data_df.info())
# print(relatedness_data_df.describe())

# drop irrelevant columns

# merge data

specialization_data_df.to_csv('country_specialization_data.csv')
relatedness_data_df.to_csv('country_relatedness_data.csv')


#read in data

all_specialization_data = pd.read_csv('country_specialization_data.csv')
all_relatedness_data = pd.read_csv('country_relatedness_data.csv')

# drop unnamed variables
all_specialization_data = all_specialization_data.drop(['Unnamed: 0'], axis=1)
all_relatedness_data = all_relatedness_data.drop(['Unnamed: 0'], axis=1)

# get relevant columns
all_specialization_data = all_specialization_data[[
    'Country', 'HS4', 'Trade Value RCA']]
all_relatedness_data = all_relatedness_data[[
    'Country', 'HS4', 'Trade Value Relatedness']]

# export finalized data for appendices
all_specialization_data.to_csv('refined_country_specialization_data.csv')
all_relatedness_data.to_csv('refined_country_relatedness_data.csv')

# continue to refine datasets to obtain tabular data
refined_specialization_data = all_specialization_data.groupby('Country').apply(
    lambda x: x.nlargest(5, 'Trade Value RCA')).reset_index(drop='True')
refined_relatedness_data = all_relatedness_data.groupby('Country').apply(
    lambda x: x.nlargest(5, 'Trade Value Relatedness')).reset_index(drop='True')

# now we have top 5 for each country, create a table with aggregated data for each country with relevant columns
refined_specialization_data = refined_specialization_data[['Country', 'HS4']]
refined_relatedness_data = refined_relatedness_data[['Country', 'HS4']]

# list out HS4 codes element-wise in one country entry each
refined_specialization_data = refined_specialization_data.groupby(
    'Country').agg(list)
refined_relatedness_data = refined_relatedness_data.groupby(
    'Country').agg(list)

# export tables
refined_specialization_data.to_csv('refined_specialization_table.csv')
refined_relatedness_data.to_csv('refined_relatedness_table.csv')
