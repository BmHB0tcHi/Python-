import pandas as pd
import numpy as np 
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.covariance import EllipticEnvelope

pk = pd.read_csv('pokemons.csv')
print('Number of Pokemons: ' +str(len(pk)))

#Problem 1
relevant_col = pk[['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'HP']]
kmeans = KMeans(n_clusters=4)
kmeans.fit(relevant_col)
y_kmeans = kmeans.predict(relevant_col)
#print(y_kmeans)

#Problem 2 
pk.loc[:, 'Cluster'] = y_kmeans.copy()
#print(pk.head())
cluster_means = pk.groupby('Cluster').mean()
#print(cluster_means.head())

#Problem 3
#pk.groupby('Cluster').mean().plot.line(y=['Sp. Atk'])

#Problem 4 
pca = PCA()
pca.fit(relevant_col)

#plt.plot(np.cumsum(pca.explained_variance_ratio_))
#plt.xlabel('number of components')
#plt.ylabel('cumulative explained variance');
#plt.show()

pca = PCA(n_components=2)
pca.fit(relevant_col)
components = pca.transform(relevant_col)
print('Number of Components after Transformation: ' +str(len(components[0])))

#problem 5 

fitting = EllipticEnvelope(random_state=42, contamination= 0.01).fit(relevant_col)
y = fitting.predict(relevant_col)
#print(y)

outliers = []

for i in range(0, len(y)):
    if y[i] == -1:
        outliers.append(y[i])
print(' Number of Pokemons that stand out the most from the rest.: ' +str(len(outliers)))



pk.loc[:, 'Outlier?'] = y.copy()
outliers_dataframe = pk.groupby('Name').mean()
#print(outliers_dataframe.head)


    
      
