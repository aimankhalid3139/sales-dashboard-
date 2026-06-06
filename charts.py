import matplotlib.pyplot as plt
import seaborn as sns

# Professional aur clean visual theme set karne ke liye
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 13})

def plot_pie_chart(df, cat_col):
    """1. Pie Chart - Proportional distribution"""
    fig, ax = plt.subplots()
    data = df[cat_col].value_counts()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax.set_title(f"Proportional Distribution of {cat_col}")
    return fig

def plot_histogram(df, num_col):
    """2. Histogram - Frequency distribution"""
    fig, ax = plt.subplots()
    sns.histplot(df[num_col], kde=True, ax=ax, color="#4a90e2")
    ax.set_title(f"Frequency Distribution of {num_col}")
    ax.set_xlabel(num_col)
    ax.set_ylabel("Frequency")
    return fig

def plot_line_chart(df, x_col, y_col):
    """3. Line Chart - Trends over time/sequence"""
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x=x_col, y=y_col, ax=ax, marker="o", color="#2ecc71")
    ax.set_title(f"{y_col} Trend Over {x_col}")
    plt.xticks(rotation=45)
    return fig

def plot_bar_chart(df, cat_col, num_col):
    """4. Bar Chart - Compare values across categories"""
    fig, ax = plt.subplots()
    sns.barplot(data=df, x=cat_col, y=num_col, ax=ax, palette="muted", errorbar=None)
    ax.set_title(f"Comparison of {num_col} by {cat_col}")
    plt.xticks(rotation=45)
    return fig

def plot_scatter_plot(df, x_num, y_num):
    """5. Scatter Plot - Relationship between two numerical variables"""
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_num, y=y_num, ax=ax, alpha=0.7, color="#9b59b6")
    ax.set_title(f"{y_num} vs {x_num}")
    return fig

def plot_box_plot(df, cat_col, num_col):
    """6. Box Plot - Data spread, median, and outliers"""
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=cat_col, y=num_col, ax=ax, palette="Set2")
    ax.set_title(f"Data Spread of {num_col} across {cat_col}")
    return fig

def plot_heatmap(df):
    """7. Heatmap - Correlation matrix of features"""
    fig, ax = plt.subplots(figsize=(6, 4))
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax, cbar=True)
        ax.set_title("Feature Correlation Matrix")
    return fig

def plot_area_chart(df, x_col, y_col):
    """8. Area Chart - Cumulative trends over time"""
    fig, ax = plt.subplots()
    df_sorted = df.sort_values(by=x_col)
    ax.fill_between(df_sorted[x_col], df_sorted[y_col], alpha=0.4, color="#f39c12")
    ax.plot(df_sorted[x_col], df_sorted[y_col], color="#d35400", alpha=0.8)
    ax.set_title(f"Cumulative Trend of {y_col}")
    plt.xticks(rotation=45)
    return fig

def plot_count_plot(df, cat_col):
    """9. Count Plot - Frequency count of categorical variables"""
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=cat_col, ax=ax, palette="deep")
    ax.set_title(f"Total Counts for {cat_col}")
    plt.xticks(rotation=45)
    return fig

def plot_violin_plot(df, cat_col, num_col):
    """10. Violin Plot - Distribution and probability density"""
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=cat_col, y=num_col, ax=ax, palette="Pastel1")
    ax.set_title(f"Probability Density of {num_col} by {cat_col}")
    return fig