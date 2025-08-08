from sklearn.datasets import load_wine
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler



data = load_wine()
X = data.data
y = data.target

modelo = RandomForestClassifier(random_state=42)
parametros = {
    "n_estimators":[50,100,200],
    "max_features": ["sqrt","log2"],
    "max_depth":[4,5,6,7,8],
    "criterion": ["gini","entropy"]
    }

grid_search = GridSearchCV(estimator=modelo, 
                    param_grid=parametros,
                    cv = 5,
                    scoring="accuracy")

grid_search.fit(X,y)


grid_search.best_params_

