import pandas as pd

def load_and_validate_dataset(filepath):
    """
    Loads a dataset from a CSV file and performs basic validation.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        tuple: A pandas DataFrame and a dictionary with validation info.
    """
    try:
        # Load the dataset
        df = pd.read_csv(filepath)
        
        # Perform basic validation
        num_rows, num_cols = df.shape
        missing_values = df.isnull().sum().sum()
        
        validation_info = {
            "rows": num_rows,
            "columns": num_cols,
            "total_missing_values": int(missing_values),
            "status": "Success",
            "message": "Dataset loaded successfully."
        }
        
        return df, validation_info

    except FileNotFoundError:
        raise Exception(f"File not found at path: {filepath}")
    except pd.errors.EmptyDataError:
        raise Exception("The uploaded file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")

