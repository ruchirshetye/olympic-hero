# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(index=str, columns={"Total":"Total_Medals"}, inplace = True)

data.head()
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event']) 
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)



# --------------
#Code starts here





top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(top_countries,column_name):
    country_list= []
    country_list = list((top_countries.nlargest(10,column_name)['Country_Name']))
    return country_list

def IntersecOfSets(arr1, arr2, arr3): 
    # Converting the arrays into sets 
    s1 = set(arr1) 
    s2 = set(arr2) 
    s3 = set(arr3) 
      
    # Calculates intersection of  
    # sets on s1 and s2 
    set1 = s1.intersection(s2)
      
    # Calculates intersection of sets 
    # on set1 and s3 
    result_set = set1.intersection(s3) 
      
    final_list = list(result_set) 
    return final_list 

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = IntersecOfSets(top_10_summer, top_10_winter, top_10)
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1)
ax_1 = summer_df.plot.bar(x='Country_Name',y='Total_Summer')
ax_2 = winter_df.plot.bar(x='Country_Name',y='Total_Winter')
ax_3 = top_df.plot.bar(x='Country_Name',y='Total_Medals')



# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summermaxid = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summermaxid]['Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
wintermaxid = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[wintermaxid]['Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
topmaxid = top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[topmaxid]['Country_Name']




# --------------
#Code starts here
data_1 = data.drop(data.index[len(data)-1])
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
most_points_index = data_1['Total_Points'].idxmax()
best_country = data_1.loc[most_points_index]['Country_Name']




# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


