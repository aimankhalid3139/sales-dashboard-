import streamlit as st
import os
from filters import load_and_clean_data, apply_filters
import charts as ch

# Page configuration for clean layout
st.set_page_config(page_title="EDA Visualization Dashboard", layout="wide")

st.title("📊 Data Visualization Dashboard Project")
st.markdown("An interactive exploratory web application to analyze data insights dynamically.")
st.markdown("---")

DATA_FOLDER = "."
files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]

if not files:
    st.error("⚠️ No dataset file discovered in the `/data/` directory. Please drop your CSV file inside it.")
else:
    dataset_path = os.path.join(DATA_FOLDER, files[0])
    raw_dataframe = load_and_clean_data(dataset_path)

    numerical_cols = raw_dataframe.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = raw_dataframe.select_dtypes(include=['object', 'category']).columns.tolist()

    # --- SIDEBAR FILTERS ---
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    if st.sidebar.button("Reset / Clear Filters"):
        st.rerun()

    search_input = st.sidebar.text_input("🔍 Keyword Text Search", "")

    chosen_cat_col = st.sidebar.selectbox("Select Categorical Feature Column", categorical_cols if categorical_cols else [None])
    selected_categories = []
    if chosen_cat_col:
        unique_options = raw_dataframe[chosen_cat_col].dropna().unique().tolist()
        selected_categories = st.sidebar.multiselect(f"Filter values for {chosen_cat_col}", unique_options, default=unique_options)

    chosen_num_col = st.sidebar.selectbox("Select Numerical Feature Column", numerical_cols if numerical_cols else [None])
    numeric_range = (0.0, 1.0)
    if chosen_num_col:
        min_val = float(raw_dataframe[chosen_num_col].min())
        max_val = float(raw_dataframe[chosen_num_col].max())
        numeric_range = st.sidebar.slider(f"Filter range for {chosen_num_col}", min_val, max_val, (min_val, max_val))

    df = apply_filters(raw_dataframe, search_input, selected_categories, chosen_cat_col, chosen_num_col, numeric_range)

    # --- KPI SUMMARY CARDS ---
    st.subheader("📈 Key Performance Indicators (KPI)")
    card1, card2, card3 = st.columns(3)
    card1.metric(label="Total Processed Records", value=len(df))
    if chosen_num_col and len(df) > 0:
        card2.metric(label=f"Key Average ({chosen_num_col})", value=f"{df[chosen_num_col].mean():.2f}")
        card3.metric(label=f"Notable High ({chosen_num_col})", value=f"{df[chosen_num_col].max():.2f}")
    st.markdown("---")

    # --- CHART GRID LAYOUT ---
    st.subheader("🎨 Data Visualization Grid Panels")
    column_left, column_right = st.columns(2)

    with column_left:
        if chosen_cat_col and len(df) > 0:
            st.pyplot(ch.plot_pie_chart(df, chosen_cat_col))
            st.pyplot(ch.plot_count_plot(df, chosen_cat_col))
        if chosen_num_col and len(df) > 0:
            st.pyplot(ch.plot_histogram(df, chosen_num_col))

    with column_right:
        if chosen_num_col and chosen_cat_col and len(df) > 0:
            st.pyplot(ch.plot_bar_chart(df, chosen_cat_col, chosen_num_col))
            st.pyplot(ch.plot_box_plot(df, chosen_cat_col, chosen_num_col))
            st.pyplot(ch.plot_violin_plot(df, chosen_cat_col, chosen_num_col))

    st.markdown("---")
    st.subheader("🔗 Multi-Variable Relationship Matrix Plots")
    col_bottom_left, col_bottom_right = st.columns(2)

    with col_bottom_left:
        if len(numerical_cols) >= 2 and len(df) > 0:
            st.pyplot(ch.plot_scatter_plot(df, numerical_cols[0], numerical_cols[1]))
            df_seq = df.reset_index()
            st.pyplot(ch.plot_line_chart(df_seq, df_seq.columns[0], numerical_cols[0]))

    with col_bottom_right:
        if len(df) > 0:
            st.pyplot(ch.plot_heatmap(df))
        if len(numerical_cols) >= 1 and len(df) > 0:
            df_seq = df.reset_index()
            st.pyplot(ch.plot_area_chart(df_seq, df_seq.columns[0], numerical_cols[0]))
