# tâche 1
plt.scatter(diamonds['carat'], diamonds['price'])
plt.xlabel('Carat')
plt.ylabel('Prix')
plt.title('Diagramme de dispersion : Prix par rapport au Carat')
plt.show()

# tâche 2
plt.hist(diamonds['carat'], bins=30)
plt.xlabel('Carat')
plt.ylabel('Fréquence')
plt.title('Histogramme : Carat')
plt.show()

# tâche 3
sns.boxplot(x=diamonds['cut'], y=diamonds['price'])
plt.xlabel('Cut')
plt.ylabel('Prix')
plt.title('Diagramme en boîte : Cut par rapport au Prix')
plt.show()

# tâche 4
corr_matrix = diamonds[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matrice de corrélation')
plt.show()