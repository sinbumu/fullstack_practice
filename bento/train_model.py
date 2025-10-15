from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import bentoml

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

bentoml.sklearn.save_model(
    "iris_rf_model",
    model,
    signatures={"predict": {"batchable": True}},
)

print("✅ 범우님 모델이 저장되었습니다~")