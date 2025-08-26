# codebase-1
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # ------------------ PAGE CONFIG ------------------
# st.set_page_config(
#     page_title="Excel Dashboard",
#     page_icon="📊",
#     layout="wide",
# )

# # ------------------ STYLING ------------------
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f8f9fa;
#     }
#     h1 {
#         color: #2c3e50;
#         text-align: center;
#         font-size: 40px;
#         margin-bottom: 20px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📊 Excel Data Dashboard")

# # ------------------ FILE UPLOAD ------------------
# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

# if uploaded_file:
#     # Load Excel file
#     xls = pd.ExcelFile(uploaded_file)
#     sheet = st.selectbox("Select Sheet", xls.sheet_names)
#     df = pd.read_excel(uploaded_file, sheet_name=sheet)

#     st.subheader("🔍 Data Preview")
#     st.dataframe(df.head(20), use_container_width=True)

#     # ------------------ FILTERS ------------------
#     st.sidebar.header("🔧 Filters")
#     numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
#     category_cols = df.select_dtypes(exclude=['number']).columns.tolist()

#     selected_x = st.sidebar.selectbox("X-Axis", df.columns)
#     selected_y = st.sidebar.selectbox("Y-Axis", numeric_cols)

#     chart_type = st.sidebar.radio(
#         "Choose Chart Type",
#         ["Line", "Bar", "Area", "Scatter", "Pie"]
#     )

#     # ------------------ DASHBOARD LAYOUT ------------------
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.metric("📦 Total Rows", f"{len(df):,}")
#     with col2:
#         st.metric("📑 Columns", len(df.columns))
#     with col3:
#         st.metric("🗂️ Sheet", sheet)

#     # ------------------ CHART RENDER ------------------
#     st.subheader("📈 Visualization")

#     fig = None
#     if chart_type == "Line":
#         fig = px.line(df, x=selected_x, y=selected_y, title="Line Chart")
#     elif chart_type == "Bar":
#         fig = px.bar(df, x=selected_x, y=selected_y, title="Bar Chart")
#     elif chart_type == "Area":
#         fig = px.area(df, x=selected_x, y=selected_y, title="Area Chart")
#     elif chart_type == "Scatter":
#         fig = px.scatter(df, x=selected_x, y=selected_y, title="Scatter Plot")
#     elif chart_type == "Pie":
#         if selected_x in category_cols:
#             fig = px.pie(df, names=selected_x, values=selected_y, title="Pie Chart")
#         else:
#             st.error("Pie chart needs a categorical column for X-axis")

#     if fig:
#         st.plotly_chart(fig, use_container_width=True)
# else:
#     st.info("👆 Upload an Excel file to get started")



# codebase-2
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Excel Dashboard",
#     page_icon="📊",
#     layout="wide",
# )

# # ---------------- STYLING ----------------
# st.markdown("""
#     <style>
#     .main { background-color: #f8f9fa; }
#     h1 { color: #2c3e50; text-align: center; font-size: 38px; margin-bottom: 20px; }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📊 Excel Data Analysis Dashboard")

# # ---------------- FILE UPLOAD ----------------
# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

# if uploaded_file:
#     # Load Excel file
#     xls = pd.ExcelFile(uploaded_file)
#     sheet = st.selectbox("Select Sheet", xls.sheet_names)
#     df = pd.read_excel(uploaded_file, sheet_name=sheet)

#     # ---------------- DATA PREVIEW ----------------
#     st.subheader("🔍 Data Preview")
#     if len(df) > 200:
#         st.dataframe(df.head(200), use_container_width=True)
#         st.info(f"Showing first 200 rows out of {len(df):,}")
#     else:
#         st.dataframe(df, use_container_width=True)

#     # ---------------- METRICS ----------------
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("📦 Total Rows", f"{len(df):,}")
#     with col2:
#         st.metric("📑 Columns", len(df.columns))
#     with col3:
#         st.metric("🗂️ Sheet", sheet)

#     # ---------------- SIDEBAR FILTERS ----------------
#     st.sidebar.header("🔧 Filters")

#     # Select columns
#     numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
#     category_cols = df.select_dtypes(exclude=['number']).columns.tolist()

#     selected_x = st.sidebar.selectbox("X-Axis", df.columns)
#     selected_y = st.sidebar.selectbox("Y-Axis", numeric_cols)

#     # Chart type
#     chart_type = st.sidebar.radio(
#         "Choose Chart Type",
#         ["Line", "Bar", "Area", "Scatter", "Pie"]
#     )

#     # Optional category filter
#     filter_col = st.sidebar.selectbox("Filter by Column", [None] + category_cols)
#     if filter_col:
#         unique_vals = df[filter_col].dropna().unique()
#         selected_vals = st.sidebar.multiselect("Select Values", unique_vals, default=unique_vals)
#         df = df[df[filter_col].isin(selected_vals)]

#     # ---------------- CHART RENDER ----------------
#     st.subheader("📈 Visualization")

#     fig = None
#     if chart_type == "Line":
#         fig = px.line(df, x=selected_x, y=selected_y, title="Line Chart")
#     elif chart_type == "Bar":
#         fig = px.bar(df, x=selected_x, y=selected_y, title="Bar Chart")
#     elif chart_type == "Area":
#         fig = px.area(df, x=selected_x, y=selected_y, title="Area Chart")
#     elif chart_type == "Scatter":
#         fig = px.scatter(df, x=selected_x, y=selected_y, title="Scatter Plot")
#     elif chart_type == "Pie":
#         if selected_x in category_cols:
#             fig = px.pie(df, names=selected_x, values=selected_y, title="Pie Chart")
#         else:
#             st.error("Pie chart needs a categorical column for X-axis")

#     if fig:
#         st.plotly_chart(fig, use_container_width=True)
# else:
#     st.info("👆 Upload an Excel file to get started")



# codebase 3 -> Added date filter if exist 
import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Excel Data Analysis",
    page_icon="./public/excel.png",   # 👈 Change this icon (see notes below)
    layout="wide",
)

# ---------------- STYLING ----------------
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2c3e50; text-align: center; font-size: 38px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# st.title("📊 Excel Data Analysis Dashboard")
# Display headings of the page
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
img_base64 = get_base64_image("./public/excel.png")

st.markdown(f"""
<h1 class="custom-header" >
    <img src="data:image/png;base64,{img_base64}" class="header-icon">
    <span class="header-text">Excel Data Analysis Dashboard</span>
</h1>
""", unsafe_allow_html=True)

# CSS Styling
st.markdown("""
<style>           
            
.main {
    background-color: #f8f9fa;
}
            
.custom-header {
    display:flex;align-items:center;justify-content:center;flex-wrap:wrap;
    text-align:center;margin:0;padding:15px;border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);gap:10px;
}
.custom-header .header-icon {
    width:50px;height:50px;flex-shrink:0;transition:transform .2s;
}
.custom-header .header-icon:hover {
    transform: scale(1.1);
}
.custom-header .header-text {
    font-size:2rem;font-weight:700;color:#808080;line-height:1.2;
}

/* Tablet */
@media (max-width: 768px) {
    .custom-header {padding:12px;gap:8px;}
    .custom-header .header-icon {width:40px;height:40px;}
    .custom-header .header-text {font-size:1.5rem;}
}

/* Mobile */
@media (max-width: 480px) {
    .custom-header {flex-direction:column;padding:10px;}
    .custom-header .header-icon {width:48px;height:48px;}
    .custom-header .header-text {font-size:1.5rem;text-align:center;}
}

/* Very small screens */
@media (max-width: 320px) {
    .custom-header .header-text {font-size:1.1rem;word-break:break-word;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

if uploaded_file:
    # Load Excel file
    xls = pd.ExcelFile(uploaded_file)
    sheet = st.selectbox("Select Sheet", xls.sheet_names)
    df = pd.read_excel(uploaded_file, sheet_name=sheet)

    # Handle datetime formatting dynamically
    for col in df.select_dtypes(include=["datetime64[ns]", "datetime64[ns, UTC]"]).columns:
        # Check if all times are midnight (00:00:00)
        if (df[col].dt.time == pd.to_datetime("00:00:00").time()).all():
            df[col] = df[col].dt.date  # only date
        else:
            df[col] = df[col].dt.strftime("%Y-%m-%d %H:%M:%S")  # keep full datetime

    # ---------------- DATA PREVIEW ----------------
    # st.subheader("🔍 Data Preview")
    # if len(df) > 200:
    #     st.dataframe(df.head(200), use_container_width=True)
    #     st.info(f"Showing first 200 rows out of {len(df):,}")
    # else:
    #     st.dataframe(df, use_container_width=True)


    # ---------------- DATA PREVIEW ----------------
    st.subheader("🔍 Data Preview")
    # --- make a stable original row number (once per dataset) ---
    fingerprint = (tuple(df.columns), len(df))
    if "orig_row_fp" not in st.session_state or st.session_state.orig_row_fp != fingerprint:
        st.session_state.orig_row_fp = fingerprint
        # 1-based original positions aligned to current df.index
        st.session_state.orig_row = pd.Series(
            range(1, len(df) + 1), index=df.index, name="Row #"
        )

    # local copy with "Row #" as a real column (don’t mutate your main df)
    display_df = df.copy()
    if "Row #" not in display_df.columns:
        # align by index to survive prior filters/reindexing
        display_df.insert(0, "Row #", st.session_state.orig_row.reindex(display_df.index))

    # --- pagination controls ---
    rows_per_page = st.selectbox("Rows per page", [50, 100, 200, 500], index=2)
    total_rows = len(display_df)

    if total_rows > rows_per_page:
        total_pages = (total_rows - 1) // rows_per_page + 1

        if "page" not in st.session_state:
            st.session_state.page = 1
        if "prev_rpp" not in st.session_state:
            st.session_state.prev_rpp = rows_per_page
        if st.session_state.prev_rpp != rows_per_page:
            st.session_state.page = 1
            st.session_state.prev_rpp = rows_per_page

        c1, c2, c3, c4 = st.columns([1, 2, 2, 1])
        with c1:
            if st.button("⬅️ Previous") and st.session_state.page > 1:
                st.session_state.page -= 1
        with c4:
            if st.button("Next ➡️") and st.session_state.page < total_pages:
                st.session_state.page += 1
        with c2:
            st.markdown(
                f"<p style='text-align:center;'>Page {st.session_state.page} of {total_pages}</p>",
                unsafe_allow_html=True
            )
        with c3:
            jump = st.number_input(
                "Jump to page",
                min_value=1,
                max_value=total_pages,
                value=st.session_state.page,
                step=1,
                key="jump_page"
            )
            if jump != st.session_state.page:
                st.session_state.page = jump

        start = (st.session_state.page - 1) * rows_per_page
        end = start + rows_per_page

        # set the visible index to the original row numbers
        page_df = display_df.iloc[start:end].set_index("Row #")
        st.dataframe(page_df, use_container_width=True)

        # info bar shows true original positions based on the visible index
        shown_min = int(page_df.index.min()) if not page_df.empty else 0
        shown_max = int(page_df.index.max()) if not page_df.empty else 0
        st.info(f"Showing rows {shown_min} to {shown_max} of {total_rows:,}")
    else:
        st.dataframe(display_df.set_index("Row #"), use_container_width=True)
        st.success(f"Showing all {total_rows:,} rows")


    # ---------------- METRICS ----------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Total Rows", f"{len(df):,}")
    with col2:
        st.metric("📑 Columns", len(df.columns))
    with col3:
        st.metric("🗂️ Sheet", sheet)

    # ---------------- SIDEBAR FILTERS ----------------
    st.sidebar.header("🔧 Filters")

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    category_cols = df.select_dtypes(exclude=['number']).columns.tolist()

    selected_x = st.sidebar.selectbox("X-Axis", df.columns)
    selected_y = st.sidebar.selectbox("Y-Axis", numeric_cols)

    chart_type = st.sidebar.radio(
        "Choose Chart Type",
        ["Line", "Bar", "Area", "Scatter", "Pie"]
    )

    # Category filter
    filter_col = st.sidebar.selectbox("Filter by Column", [None] + category_cols)
    if filter_col:
        unique_vals = df[filter_col].dropna().unique()
        selected_vals = st.sidebar.multiselect("Select Values", unique_vals, default=unique_vals)
        df = df[df[filter_col].isin(selected_vals)]

    # Date filter
    date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    if date_cols:
        date_col = st.sidebar.selectbox("Filter by Date Column", [None] + date_cols)
        if date_col:
            min_date = df[date_col].min()
            max_date = df[date_col].max()
            start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])
            if isinstance(start_date, pd.Timestamp):  # date_input returns either list or scalar
                start_date, end_date = [start_date, end_date]
            df = df[(df[date_col] >= pd.to_datetime(start_date)) & (df[date_col] <= pd.to_datetime(end_date))]

    # ---------------- CHART RENDER ----------------
    st.subheader("📈 Visualization")

    fig = None
    if chart_type == "Line":
        fig = px.line(df, x=selected_x, y=selected_y, title="Line Chart")
    elif chart_type == "Bar":
        fig = px.bar(df, x=selected_x, y=selected_y, title="Bar Chart")
    elif chart_type == "Area":
        fig = px.area(df, x=selected_x, y=selected_y, title="Area Chart")
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=selected_x, y=selected_y, title="Scatter Plot")
    elif chart_type == "Pie":
        if selected_x in category_cols:
            fig = px.pie(df, names=selected_x, values=selected_y, title="Pie Chart")
        else:
            st.error("Pie chart needs a categorical column for X-axis")

    if fig:
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👆 Upload an Excel file to get started")
