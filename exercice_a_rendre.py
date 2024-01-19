# exercice 1
url = 'https://raw.githubusercontent.com/moncoachdata/MasterClass_DS_ML/main/fandango_scrape.csv'
fandango = pd.read_csv(url)

fandango.head()
fandango.info()

# exercice 2
fandango.describe()

plt.scatter(fandango['RATING'], fandango['VOTES'], alpha=0.5)
plt.xlabel('Notes')
plt.ylabel('Votes')
plt.title('Relation entre les notes et les votes des films')
plt.grid(True)
plt.show()

# exercice 3
correlation_matrix = fandango.corr()
print(correlation_matrix)

# exercice 4
fandango['YEAR'] = fandango['FILM'].str.extract(r'\((\d+)\)')
print(fandango.head())

# exercice 5
films_par_annee = fandango['YEAR'].value_counts()
print(films_par_annee)

# exercice 6
plt.figure(figsize=(12,7))
sns.scatterplot(data=fandango, x='RATING', y='VOTES');

# exercice 7
top_10_films_votes = fandango.nlargest(10, 'VOTES')
print(top_10_films_votes[['FILM', 'VOTES']])

# exercice 8
films_sans_avis = fandango[fandango['VOTES'] == 0]
nombre_films_sans_avis = films_sans_avis.shape[0]
print(nombre_films_sans_avis)

# exercice 9
movies_per_year.reset_index()

# exercice 10
sns.barplot(x=movies_per_year.index, y=movies_per_year)
plt.ylabel('count')
plt.xlabel('Year');

# exercice 11
fandango.nlargest(10, 'VOTES')

# exercie 12
votes = 0
fandango.query('VOTES == @votes').shape[0]

# exercice 13
fan_reviewed = fandango[fandango['VOTES']>0]

# exercice 14
fan_reviewed.head()

# exercice 15
plt.figure(figsize=(9, 4), dpi=100)
sns.kdeplot(data=fandango_voted, x='RATING', clip=(0, 5), fill=True, label='True Rating')
sns.kdeplot(data=fandango_voted, x='STARS', clip=(0, 5), fill=True, label='Stars Displayed')
plt.legend(loc='upper left')
plt.show()

fandango_voted['STARS_DIFF'] = round(fandango_voted['STARS'] - fandango_voted['RATING'], 1)
fandango_voted.head()

# exercice 16
plt.figure(figsize=(10,3))
sns.countplot(data=fandango_voted, x='STARS_DIFF', palette='magma');

# exercice 17
fandango_voted.query('STARS_DIFF == 1')

# exercice 18
all_sites.head()
all_sites.info()
all_sites.describe()

# exercice 22
sns.scatterplot(data=all_sites, x='RottenTomatoes', y='RottenTomatoes_User')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.plot([0, 100], [0, 100], ls='dotted', label='Agreement')
plt.legend()
plt.show()

# exercice 23
all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']
all_sites.head()

# exercice 24
all_sites['Rotten_Diff'].abs().mean().round(2)

# exercice 25
plt.figure(figsize=(9, 4))
sns.histplot(all_sites['Rotten_Diff'], bins=25, kde=True)
plt.title('RT Critics Score minus RT User Score');

# exercice 26
plt.figure(figsize=(9, 4))
sns.histplot(all_sites['Rotten_Diff'].abs(), bins=25, kde=True)
plt.title('Abs Difference between RT Critics Score and RT User Score');
