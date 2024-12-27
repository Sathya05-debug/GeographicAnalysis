import pandas as pd
import folium
import matplotlib.pyplot as plt
data=pd.read_csv('Dataset.csv')
print(data.head())
data_cleaned=data.dropna(subset=['Latitude','Longitude'])
print(data_cleaned[['Latitude','Longitude']].isnull().sum())
center_lat,center_lon=data_cleaned['Latitude'].mean() ,data_cleaned['Longitude'].mean()
restaurant_map=folium.Map(location=[center_lat,center_lon],zoom_start=12)
for _,row in data_cleaned.iterrows():folium.Marker(location=[row['Latitude'],row['Longitude']],popup=row['Restaurant Name']).add_to(restaurant_map)
restaurant_map.save('restaurant_map.html')
from sklearn.cluster import DBSCAN
import numpy as np
coords=data_cleaned[['Latitude','Longitude']].values
db=DBSCAN(eps=0.1,min_samples=5,metric='haversine').fit(np.radians(coords))
data_cleaned['Cluster']=db.labels_
print(data_cleaned['Cluster'].value_counts())
cluster_map=folium.Map(location=[center_lat,center_lon],zoom_start=12)
cluster_map.save('cluster_map.html')
if not data_cleaned.empty:
 for _, row in data_cleaned.iterrows():
   cluster_color='red' if row['Cluster']==-1 else 'blue'
 folium.CircleMarker(location=[ row['Latitude'],row['Longitude']],radius=5,color='red',fill=True,fill_opacity=0.7).add_to(cluster_map)
cluster_map.save('cluster_map2.html')
plt.figure(figsize=(10,6))
plt.scatter(data_cleaned['Longitude'],data_cleaned['Latitude'],c=data_cleaned['Cluster'],cmap='viridis',marker='o')
plt.title("Restaurant Clusters")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label="Cluster ID")
plt.show()

