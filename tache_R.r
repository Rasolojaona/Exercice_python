# tâche 1
plot(diamonds$carat, diamonds$price, 
     xlab = "Carat", ylab = "Prix", 
     main = "Diagramme de dispersion : Prix par rapport au Carat")

# tâche 2
hist(diamonds$carat, breaks = 30, 
     xlab = "Carat", ylab = "Fréquence", 
     main = "Histogramme : Carat")

# tâche 3
boxplot(diamonds$price ~ diamonds$cut, 
        xlab = "Cut", ylab = "Prix", 
        main = "Diagramme en boîte : Cut par rapport au Prix")

# tâche 4
corr_matrix <- cor(diamonds[c("carat", "depth", "table", "price", "x", "y", "z")])
heatmap(corr_matrix, 
        main = "Matrice de corrélation", 
        col = colorRampPalette(c("blue", "white", "red"))(100), 
        symm = TRUE, 
        margins = c(10, 10))
