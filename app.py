import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="BDM Pro Analytics", page_icon="📈", layout="wide")

# --- ADVANCED BLUE THEME & ANIMATIONS ---
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');
    
    .main { background-color: #0e1117; }
    
    /* Fix invisible KPI text from previous version */
    div[data-testid="stMetricValue"] {
        font-size: 32px !important;
        color: #00d4ff !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #e0e0e0 !important;
        font-size: 16px !important;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .header-text {
        color: #00d4ff;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="header-text animate__animated animate__fadeInLeft">📊 BDM: Advanced Business Data Analytics</h1>', unsafe_allow_html=True)
st.write("---")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 📥 Data Management")
    uploaded_file = st.file_uploader("Upload Transaction CSV", type=["csv"])

if uploaded_file:
    @st.cache_data
    def load_and_clean(file):
        df = pd.read_csv(file)
        # Clean quotes and whitespace
        df.columns = df.columns.str.strip().str.replace("'", "")
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].astype(str).str.replace("'", "").str.strip()
        
        df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
        df['Hour'] = df['Transaction_Date'].dt.hour
        return df

    df = load_and_clean(uploaded_file)

    # --- FILTERS ---
    st.sidebar.markdown("### 🔍 Global Filters")
    date_range = st.sidebar.date_input("Select Date Range", [df['Transaction_Date'].min(), df['Transaction_Date'].max()])
    selected_status = st.sidebar.multiselect("Status", options=df['Status'].unique(), default=df['Status'].unique())
    selected_mode = st.sidebar.multiselect("Payment Mode", options=df['Payment_Mode'].unique(), default=df['Payment_Mode'].unique())

    mask = (df['Transaction_Date'].dt.date >= date_range[0]) & \
           (df['Transaction_Date'].dt.date <= date_range[1]) & \
           (df['Status'].isin(selected_status)) & \
           (df['Payment_Mode'].isin(selected_mode))
    
    f_df = df.loc[mask]

    # --- KPI CARDS ---
    c1, c2, c3, c4 = st.columns(4)
    total_gmv = f_df['Amount'].sum()
    total_txns = len(f_df)
    success_count = len(f_df[f_df['Status'].str.upper() == 'SUCCESS'])
    sr = (success_count / total_txns * 100) if total_txns > 0 else 0

    c1.metric("Total GMV", f"₹{total_gmv:,.0f}")
    c2.metric("Orders", f"{total_txns}")
    c3.metric("Avg Ticket Size", f"₹{ (total_gmv/total_txns) if total_txns > 0 else 0:,.2f}")
    c4.metric("Success Rate", f"{sr:.1f}%")

    # --- MAIN DASHBOARD CHARTS ---
    st.markdown("### 📈 Visual Insights")
    col1, col2 = st.columns(2)

    with col1:
        # Area chart for revenue
        rev_trend = f_df.set_index('Transaction_Date').resample('D')['Amount'].sum().reset_index()
        fig1 = px.area(rev_trend, x='Transaction_Date', y='Amount', title="Daily Revenue Trend",
                       color_discrete_sequence=['#00d4ff'])
        fig1.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # Donut chart for payment modes
        fig2 = px.pie(f_df, names='Payment_Mode', values='Amount', hole=0.5, title="Revenue by Payment Mode")
        fig2.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    # --- DATA TABLE WITH ERROR HANDLING ---
    st.markdown("---")
    show_table = st.checkbox("📁 Show Detailed Data Table")
    
    if show_table:
        try:
            # Try to show with fancy colors (requires matplotlib)
            st.dataframe(f_df.style.background_gradient(cmap='Blues', subset=['Amount']), use_container_width=True)
        except ImportError:
            # Fallback if matplotlib is missing
            st.warning("Install matplotlib to see color gradients in the table. Showing standard table instead.")
            st.dataframe(f_df, use_container_width=True)

    # Export Button
    st.sidebar.markdown("---")
    st.sidebar.download_button("📥 Export Filtered Data", f_df.to_csv(index=False), "bdm_export.csv", "text/csv")

else:
    st.info("👈 Please upload your transaction CSV file in the sidebar to begin.")
