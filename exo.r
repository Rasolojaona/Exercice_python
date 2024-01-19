# Fonction pour calculer le coût
compute_cost <- function(x, y, w, b) {
  m <- length(x)
  y_pred <- w * x + b
  total_cost <- sum((y_pred - y)^2) / (2 * m)
  return(total_cost)
}
