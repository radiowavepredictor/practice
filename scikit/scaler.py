import numpy as np
from sklearn.preprocessing import StandardScaler

# サンプルデータ
X = np.array([
    [170, 65],
    [180, 75],
    [160, 55]
])

# sklearnで平均と分散を取得
scaler = StandardScaler()
scaler.fit(X)

mean = scaler.mean_
std = np.sqrt(scaler.var_)  # ← sklearnはvarを持っている

# 手動で標準化
X_manual = (X - mean) / std

print("sklearn:\n", scaler.transform(X))
print("manual:\n", X_manual)