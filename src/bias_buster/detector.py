import pandas as pd

# A simple threshold to decide if a class is imbalanced.
# E.g., if the minority class is less than 20% of the majority class.
IMBALANCE_THRESHOLD = 0.2 

def detect_biases(df):
    """
    Analyzes a DataFrame to detect potential sources of bias.

    Args:
        df (pd.DataFrame): The input dataset.

    Returns:
        dict: A dictionary containing the results of the bias detection analysis.
    """
    results = {
        "imbalance_analysis": [],
        "distribution_analysis": [],
        "missing_data_analysis": {}
    }

    # --- 1. Imbalance Analysis (for categorical columns) ---
    # We'll treat columns with a small number of unique values as potential targets.
    for col in df.select_dtypes(include=['object', 'category']).columns:
        if 2 <= df[col].nunique() <= 10: # Heuristic for likely target/sensitive attribute
            value_counts = df[col].value_counts(normalize=True)
            minority_class_percent = value_counts.min()
            majority_class_percent = value_counts.max()

            # Check for significant imbalance
            if minority_class_percent / majority_class_percent < IMBALANCE_THRESHOLD:
                results["imbalance_analysis"].append({
                    "column": col,
                    "is_imbalanced": True,
                    "message": f"'{col}' is highly imbalanced.",
                    "details": value_counts.to_dict()
                })

    # --- 2. Distribution Analysis (for numerical columns) ---
    for col in df.select_dtypes(include=['number']).columns:
        skewness = df[col].skew()
        # High skewness can indicate bias
        if abs(skewness) > 1.0:
            results["distribution_analysis"].append({
                "column": col,
                "skewness": round(skewness, 2),
                "message": f"'{col}' is highly skewed. This might affect model performance."
            })

    # --- 3. Missing Data Analysis ---
    missing_counts = df.isnull().sum()
    missing_percent = (missing_counts / len(df)) * 100
    missing_data = missing_percent[missing_percent > 0].round(2)
    if not missing_data.empty:
        results["missing_data_analysis"] = {
            "has_missing_data": True,
            "details": missing_data.to_dict()
        }
    else:
        results["missing_data_analysis"] = {
            "has_missing_data": False,
            "details": {}
        }

    return results

