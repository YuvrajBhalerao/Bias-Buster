def generate_suggestions(bias_results):
    """
    Generates actionable suggestions based on bias detection results.

    This function takes the dictionary of findings from the detector module
    and creates a corresponding dictionary of human-readable advice for
    mitigating the identified issues.

    Args:
        bias_results (dict): The dictionary of results from the detector.
                             Example: 
                             {
                                 "imbalance_analysis": [...],
                                 "distribution_analysis": [...],
                                 "missing_data_analysis": {...}
                             }

    Returns:
        dict: A dictionary containing lists of suggestions, categorized by
              the type of action required (e.g., resampling, imputation).
    """
    suggestions = {
        "resampling": [],
        "feature_engineering": [],
        "data_imputation": []
    }

    # --- 1. Suggestions for Class Imbalance ---
    # Check if the 'imbalance_analysis' key exists and is not empty.
    if bias_results.get("imbalance_analysis"):
        for item in bias_results["imbalance_analysis"]:
            suggestions["resampling"].append(
                f"For the imbalanced column '{item['column']}', consider using resampling techniques like "
                "**SMOTE** (Synthetic Minority Over-sampling Technique) to create synthetic data for the minority class, "
                "or **RandomOverSampler** to duplicate minority class samples. "
                "Alternatively, **RandomUnderSampler** can reduce the majority class."
            )

    # --- 2. Suggestions for Skewed Distributions ---
    # Check if the 'distribution_analysis' key exists and is not empty.
    if bias_results.get("distribution_analysis"):
        for item in bias_results["distribution_analysis"]:
            suggestions["feature_engineering"].append(
                f"The feature '{item['column']}' is highly skewed (skewness: {item['skewness']}). "
                "This can negatively impact some models. Consider applying a **log transformation** or a "
                "**Box-Cox transformation** to make its distribution more normal."
            )

    # --- 3. Suggestions for Missing Data ---
    # Check if the 'missing_data_analysis' key exists and has the 'has_missing_data' flag set to True.
    if bias_results.get("missing_data_analysis", {}).get("has_missing_data"):
        missing_cols = list(bias_results["missing_data_analysis"]["details"].keys())
        suggestions["data_imputation"].append(
            f"Missing data was found in columns: {', '.join(missing_cols)}. "
            "For numerical data, consider imputing with the **mean or median**. "
            "For categorical data, consider imputing with the **mode**. "
            "For more advanced cases, **KNNImputer** or model-based imputation can be effective."
        )

    return suggestions

