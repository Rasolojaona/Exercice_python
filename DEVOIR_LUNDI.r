url <- "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/kc_house_data_NaN.csv"
df <- read.csv(url)

head(df)


library(ggplot2)
library(dplyr)


ggplot(df, aes(x = price)) +
  geom_histogram(fill = "blue", bins = 30) +
  labs(x = "Price", y = "Count", title = "Distribution of House Prices")


ggplot(df, aes(x = bedrooms, y = price)) +
  geom_point(color = "blue") +
  labs(x = "Bedrooms", y = "Price", title = "Number of Bedrooms vs Price")


cor_matrix <- cor(df[, c("price", "bedrooms", "bathrooms", "sqft_living")])
print(cor_matrix)


library(caret)
library(ggplot2)


df_selected <- df[, c("bedrooms", "bathrooms", "sqft_living", "floors", "waterfront", "view", "grade", "yr_built", "zipcode")]


df_selected <- na.omit(df_selected)


set.seed(123)
train_index <- createDataPartition(df_selected$price, p = 0.7, list = FALSE)
train_data <- df_selected[train_index, ]
test_data <- df_selected[-train_index, ]


linear_model <- lm(price ~ ., data = train_data)


summary(linear_model)


test_predictions <- predict(linear_model, newdata = test_data)


rmse <- sqrt(mean((test_predictions - test_data$price)^2))
print(rmse)


ggplot(data = test_data, aes(x = price, y = test_predictions)) +
  geom_point(color = "blue") +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +
  labs(x = "Actual Price", y = "Predicted Price", title = "Actual vs Predicted House Prices")


library(caret)


preprocess <- preProcess(train_data[, -1], method = c("center", "scale", "knnImpute"))


train_data_processed <- predict(preprocess, newdata = train_data[, -1])
test_data_processed <- predict(preprocess, newdata = test_data[, -1])


linear_model_improved <- lm(price ~ ., data = train_data_processed)


summary(linear_model_improved)


test_predictions_improved <- predict(linear_model_improved, newdata = test_data_processed)


rmse_improved <- sqrt(mean((test_predictions_improved - test_data$price)^2))
print(rmse_improved)


ggplot(data = test_data, aes(x = price, y = test_predictions_improved)) +
  geom_point(color = "blue") +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +
  labs(x = "Actual Price", y = "Predicted Price", title = "Actual vs Predicted House Prices (Improved Model)")


Voici la suite du code R équivalent pour le contenu de Peer-graded Assignment_ House Sales in King County.ipynb :


library(caret)


preprocess_poly <- preProcess(train_data[, -1], method = c("center", "scale", "knnImpute", "poly"), degree = 2)


train_data_processed_poly <- predict(preprocess_poly, newdata = train_data[, -1])
test_data_processed_poly <- predict(preprocess_poly, newdata = test_data[, -1])


linear_model_poly <- lm(price ~ ., data = train_data_processed_poly)


summary(linear_model_poly)


test_predictions_poly <- predict(linear_model_poly, newdata = test_data_processed_poly)


rmse_poly <- sqrt(mean((test_predictions_poly - test_data$price)^2))
print(rmse_poly)


ggplot(data = test_data, aes(x = price, y = test_predictions_poly)) +
  geom_point(color = "blue") +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +
  labs(x = "Actual Price", y = "Predicted Price", title = "Actual vs Predicted House Prices (Polynomial Model)")


summary_df <- data.frame(Model = c("Linear Regression", "Improved Linear Regression", "Polynomial Regression"),
                         RMSE = c(rmse, rmse_improved, rmse_poly))
print(summary_df)