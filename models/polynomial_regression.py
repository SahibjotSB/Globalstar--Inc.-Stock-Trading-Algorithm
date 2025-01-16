
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def train_model(X_train, y_train):
    """Train polynomial regression model."""
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X_train)
    model = LinearRegression()
    model.fit(X_poly, y_train)
    return model, poly
