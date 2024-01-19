import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/heart.csv'
df = pd.read_csv(url)

df.head()

df['target'].unique()

df.describe()

df.dtypes

df.head()

df['sex'] = df['sex'].astype('category')

df.info()

df['sex'].value_counts()

df.isna().sum()

sns.countplot(x='target', data=df)
plt.xlabel('Valeur Cible')
plt.ylabel('Nombre de Comptages')
plt.title('Nombre de Comptages par Valeur Cible')
plt.show()

sns.pairplot(df[['age', 'trestbps', 'chol', 'thalach', 'target']], hue='target')
plt.show()

corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Afficher la carte de chaleur
plt.title('Corrélation entre les colonnes')
plt.show()

X = df.drop('target', axis=1)
y = df['target']

X.head()

y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)

print("Dimensions de l'ensemble d'entraînement (X_train, y_train):", X_train.shape, y_train.shape)
print("Dimensions de l'ensemble de test (X_test, y_test):", X_test.shape, y_test.shape)