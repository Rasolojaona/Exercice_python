# compute_cost
def compute_cost(x, y, w, b):
    m = x.shape[0]

    total_cost = 0

    for i in range(m):
        y_pred = w * x[i] + b
        total_cost = (y_pred - y[i])**2 + total_cost

    total_cost = (1 / (2 * m)) * total_cost

    return total_cost

# descent gradient
def compute_gradient(x, y, w, b):
    
    m = x.shape[0]
    predictions = w * x + b
    dj_dw = (1 / m) * np.sum((predictions - y) * x)
    dj_db = (1 / m) * np.sum(predictions - y)

    return dj_dw, dj_db