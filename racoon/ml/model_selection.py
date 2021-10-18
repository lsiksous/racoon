import pandas as pd

def stratified_split(data: pd.DataFrame,
                     target: str,
                     n_samples: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Stratified data split.
    Splits data into training and testing dataframes whilst stratifying
    to maintain target variable proportions.
    Args:
        data (DataFrame): Full dataframe including predictors as well as
            target variable.
        target (str): The name of the column containing the target
            variable.
        n_samples (int): The number of samples to include in the test
            set from each target label category.
    Returns:
        tuple: The training and testing dataframes.
    """
    n = min(n_samples, data[target].value_counts().min())
    test_df = data.groupby(target).apply(lambda x: x.sample(n))
    test_df.index = test_df.index.droplevel(0)
    train_df = data[~data.index.isin(test_df.index)]
    return train_df, test_df
