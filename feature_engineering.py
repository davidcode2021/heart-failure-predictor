

#  Custom transformer for feature engineering
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self  # nothing to learn

    def transform(self, X):
        X = X.copy()
        # Example engineered features
        X["creatinine_ratio"] = X["serum_creatinine"] / X["serum_sodium"]
        X["age_group"] = X["age"] // 10
        X["risk_score"] = X["ejection_fraction"] * (X["serum_sodium"] / X["creatinine_phosphokinase"])
        
        X['age_x_creatinine'] = X['age'] * X['serum_creatinine']
        X['platelets_x_age'] = X['platelets'] * X['age']
        X['bp_x_diabetes'] = X['high_blood_pressure'] * X['diabetes']
        X['sex_x_smoking'] = X['sex'] * X['smoking']
        
        X['creatinine_per_platelet'] = X['serum_creatinine'] / (X['platelets'] + 1e-5)
        X['sodium_creatinine_ratio'] = X['serum_sodium'] / (X['serum_creatinine'] + 1e-5)
        
        X['creatinine_per_time'] = X['serum_creatinine'] / (X['time'] + 1)
        X['platelets_per_time'] = X['platelets'] / (X['time'] + 1)
        
        X['anaemia_diabetes'] = ((X['anaemia'] == 1) & (X['diabetes'] == 1)).astype(int)
        X['elderly_smoker'] = ((X['age'] > 65) & (X['smoking'] == 1)).astype(int)
        X['high_risk_group'] = ((X['ejection_fraction'] < 30) & (X['serum_creatinine'] > 1.5)).astype(int)
        return X
