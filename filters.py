import pandas as pd

def load_and_clean_data(filepath):
    """
    Dataset ko load karta hai aur Pandas se missing values handle karta hai.
    """
    df = pd.read_csv(filepath)
    
    # Missing values ko forward fill karne ka naya aur sahi tareeqa
    df = df.ffill().fillna(0)
    
    return df

def apply_filters(df, search_keyword, selected_category, category_column, numerical_column, numerical_range):
    """
    Dashboard ke filters ke mutabiq data ko update (filter) karta hai.
    """
    filtered_df = df.copy()
    
    # 1. Text Search Filter (Keyword Search)
    if search_keyword:
        text_cols = filtered_df.select_dtypes(include=['object']).columns
        if len(text_cols) > 0:
            mask = filtered_df[text_cols].apply(lambda x: x.astype(str).str.contains(search_keyword, case=False)).any(axis=1)
            filtered_df = filtered_df[mask]
        
    # 2. Category Dropdown / Multi-Select Filter
    if category_column and selected_category:
        filtered_df = filtered_df[filtered_df[category_column].isin(selected_category)]
        
    # 3. Numerical Range Slider Filter
    if numerical_column:
        filtered_df = filtered_df[
            (filtered_df[numerical_column] >= numerical_range[0]) & 
            (filtered_df[numerical_column] <= numerical_range[1])
        ]
        
    return filtered_df