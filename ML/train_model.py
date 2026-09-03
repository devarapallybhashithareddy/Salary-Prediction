import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the dataset
df = pd.read_csv("Data/ds_salaries.csv")

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Select the features we need
df_ml = df[
    [
        'work_year',
        'experience_level',
        'employment_type',
        'job_title',
        'employee_residence',
        'remote_ratio',
        'company_location',
        'company_size',
        'salary_in_usd'
    ]
].copy()

print("\nML Dataset shape:", df_ml.shape)

print("\nFirst 5 rows:")
print(df_ml.head())

# Check for missing values
print("\nMissing values:")
print(df_ml.isnull().sum())

# Separate features and target
X = df_ml.drop('salary_in_usd', axis=1)

y = df_ml['salary_in_usd']

print("\nX shape:", X.shape)
print("y shape:", y.shape)

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining and Testing Shapes:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# Define numerical and categorical features

numeric_features = [
    'work_year',
    'remote_ratio'
]

categorical_features = [
    'experience_level',
    'employment_type',
    'job_title',
    'employee_residence',
    'company_location',
    'company_size'
]

# Create preprocessing pipeline

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),

        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Transform the training data
X_train_processed = preprocessor.fit_transform(X_train)

print("\nProcessed training data shape:")
print(X_train_processed.shape)

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=4,
    random_state=42
)

# Train the model
model.fit(X_train_processed, y_train)

print("\nModel training completed successfully!")

# Transform the test data
X_test_processed = preprocessor.transform(X_test)

# Make predictions
y_pred = model.predict(X_test_processed)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

# Save the trained model
joblib.dump(model, "Model/salary_model.pkl")

# Save the preprocessor
joblib.dump(preprocessor, "Model/preprocessor.pkl")

print("\nModel and preprocessor saved successfully!")