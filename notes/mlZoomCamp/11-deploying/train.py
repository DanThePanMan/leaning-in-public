
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
 
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


import pickle


# params
C = 1.0
n_splits = 5
output_file = f"model_C={C}.bin"

print(f"Starting training with C={C}, n_splits={n_splits}")
print(f"Output file: {output_file}")

# Data preparation
print("\n[1/6] Loading data...")
df = pd.read_csv('notes/mlZoomCamp/data/churn.csv')  # reads from mlZoomCamp/data/churn.csv
print(f"✓ Loaded {len(df)} records with {len(df.columns)} columns")

print("\n[2/6] Preprocessing data...")
df.columns = df.columns.str.lower().str.replace(' ', '_')
 
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
 
for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')
 
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)
 
df.churn = (df.churn == 'yes').astype(int)
print(f"✓ Preprocessed columns, target distribution: {df.churn.value_counts().to_dict()}")

print("\n[3/6] Splitting data...")
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
print(f"✓ Train: {len(df_full_train)} records, Test: {len(df_test)} records")


numerical = ['tenure', 'monthlycharges', 'totalcharges']
 
categorical = ['gender', 'seniorcitizen', 'partner', 'dependents',
       'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod']



# training
def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
 
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
 
    model = LogisticRegression(C=C, max_iter=5000, solver='lbfgs')
    model.fit(X_train, y_train)
 
    return dv, model


def predict(df, dv, model):
     dicts = df[categorical + numerical].to_dict(orient='records')
 
     X = dv.transform(dicts)
     y_pred = model.predict_proba(X)[:,1]
 
     return y_pred





print(f"\n[4/6] Running {n_splits}-fold cross-validation...")
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)  
 
scores = []
fold = 1
 
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]
 
    y_train = df_train.churn.values
    y_val = df_val.churn.values
 
    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)
 
    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)
    print(f"  Fold {fold}/{n_splits}: AUC = {auc:.4f}")
    fold += 1
 
print(f'✓ Cross-validation complete: C={C} AUC = {np.mean(scores):.3f} ± {np.std(scores):.3f}')
 

print("\n[5/6] Training final model on full training set...")
dv, model = train(df_full_train, df_full_train.churn.values, C=1.0)
y_pred = predict(df_test, dv, model)
y_test = df_test.churn.values
 
auc = roc_auc_score(y_test, y_pred)
print(f"✓ Final model test AUC: {auc:.4f}")
 
 

# exporting the model
print(f"\n[6/6] Saving model to {output_file}...")
with open(output_file, 'wb') as f_out: #wb for write byte
    pickle.dump((dv,model), f_out)
print(f"✓ Model saved successfully!")
print("\n🎉 Training complete!")

