import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

from get_data import *

features_df, labels_df = Data(1).x()

# Merge on hit_id
dataset = pd.merge(
    features_df,
    labels_df,
    on="hit_id"
)

# Features
X = dataset.drop(columns=["hit_id", "particle_id"])

# Target
y = dataset["particle_id"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Scale data
scaler = StandardScaler()

print("scaling init")
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Neural network
model = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
    verbose=True
)


print("training init")
# Train
model.fit(X_train, y_train)

print("trained init")
# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")
print()
print(classification_report(y_test, predictions))