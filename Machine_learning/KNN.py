import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

# Bước 2: Tạo dữ liệu
X, y = make_blobs(n_samples=100, n_features=2, centers=4, cluster_std=1, random_state=4)

# Bước 3: Vẽ dữ liệu gốc
plt.figure(figsize=(9, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', s=50)
plt.title("Dữ liệu gốc")
plt.show()

# Bước 4: Chia train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

plt.figure(figsize=(9, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='o', s=40)
plt.title("Tập kiểm tra")
plt.show()

# Bước 5: KNN với k=5
knn5 = KNeighborsClassifier(5)
knn5.fit(X_train, y_train)
y_pred_5 = knn5.predict(X_test)

plt.figure(figsize=(9, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_5, marker='o', s=40)
plt.title("KNN với k=5")
plt.show()

# Bước 6: KNN với k=1
knn1 = KNeighborsClassifier(1)
knn1.fit(X_train, y_train)
y_pred_1 = knn1.predict(X_test)

plt.figure(figsize=(9, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_1, marker='o', s=40)
plt.title("KNN với k=1")
plt.show()

# Bước 7: Tìm k tối ưu bằng GridSearchCV
knn_grid = GridSearchCV(estimator=KNeighborsClassifier(),
                        param_grid={'n_neighbors': np.arange(1, 10)}, cv=5)
knn_grid.fit(X, y)
print("Best k:", knn_grid.best_params_)

# Bước 8: Vẽ decision boundary cho KNN với k tối ưu
best_k = knn_grid.best_params_['n_neighbors']
knn_best = KNeighborsClassifier(best_k)
knn_best.fit(X_train, y_train)

# Tạo lưới điểm để vẽ boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))

Z = knn_best.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(9, 6))
plt.contourf(xx, yy, Z, alpha=0.3)  # vùng phân loại
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=50)  # dữ liệu gốc
plt.title(f"Decision Boundary với KNN (k={best_k})")
plt.show()
