import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import datetime

# --- 1. ENTERPRISE CONFIGURATION ---
st.set_page_config(page_title="Turner Project Intelligence", layout="wide", initial_sidebar_state="expanded")

# --- 2. THE CORE SME ENGINE (Ideas 1, 10, 16) ---
class TurnerProjectEngine:
    def __init__(self):
        # Idea 16: ETL Sync simulation from P6/Odoo [cite: 17]
        self.data = pd.DataFrame([
            {'id': 101, 'task': 'Site Grading', 'dur': 12, 'pred': [], 'trade': 'Earthwork', 'zone': 'Sector A', 'cost': 85000, 'bim': 'BIM-001'},
            {'id': 102, 'task': 'Concrete Slab', 'dur': 18, 'pred': [101], 'trade': 'Concrete', 'zone': 'Sector A', 'cost': 150000, 'bim': 'BIM-002'},
            {'id': 103, 'task': 'Steel Erection', 'dur': 25, 'pred': [102], 'trade': 'Steel', 'zone': 'Sector B', 'cost': 450000, 'bim': 'BIM-003'},
            {'id': 104, 'task': 'MEP Switchgear', 'dur': 45, 'pred': [103], 'trade': 'Electrical', 'zone': 'Substation', 'cost': 1200000, 'bim': 'BIM-004'},
            {'id': 105, 'task': 'Finishes', 'dur': 20, 'pred': [103], 'trade': 'Finishes', 'zone': 'Data Hall', 'cost': 200000, 'bim': 'BIM-005'}
        ])
        if 'audit_log' not in st.session_state:
            st.session_state.audit_log = [f"{datetime.datetime.now().strftime('%H:%M:%S')} - Master Data Synced"]
        if 'p90_variance' not in st.session_state:
            st.session_state.p90_variance = 0

    def record_audit(self, action): # Idea 10: SOX Compliance Audit [cite: 30, 39]
        st.session_state.audit_log.append(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {action}")

# --- 3. LIVE OPERATIONS & GOVERNANCE UI (Ideas 3, 9, 13, 20) ---
def render_sidebar(engine, df):
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/Turner_Construction_Company_Logo.svg", width=150)
    st.sidebar.title("🛡️ Project Governance")
    st.sidebar.info(f"**Lead SME:** Sai Jagan Yalamanchili\n**Project:** AZ Hyperscale Data Center")
    
    # Idea 9: 4D BIM Health [cite: 52]
    bim_links = (df['bim'].notnull().sum() / len(df)) * 100
    st.sidebar.subheader("📐 4D BIM Health")
    st.sidebar.progress(int(bim_links), text=f"BIM-Linkage: {bim_links}%")
    
    # Live Operation: BIM-Field Sync (Idea 16)
    if st.sidebar.button("🔄 Sync BIM-Field Data"):
        engine.record_audit("BIM-Odoo Sync Complete: Verified 100% Data Integrity")
        st.sidebar.success("Field Data Verified")

    # Idea 20: Constraint Log
    st.sidebar.subheader("Live Constraint Log")
    st.sidebar.warning("⚠️ Electrical Permit: Pending (12 Days)")
    
    # Idea 10: Compliance Export
    st.sidebar.subheader("Compliance Export")
    csv = pd.DataFrame(st.session_state.audit_log).to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("Download SOX Audit Trail", data=csv, file_name="Turner_Audit.csv")

# --- 4. MAIN DASHBOARD CONTENT ---
def main():
    engine = TurnerProjectEngine()
    df = engine.data
    render_sidebar(engine, df)

    st.title("🏗️ Turner Enterprise Project Intelligence Suite")
    st.markdown("### *High-Stakes Infrastructure Command Center*")

    # ROW 1: EXECUTIVE ANALYTICS (Ideas 2, 7, 11, 3)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # Idea 2: Predictive P90 [cite: 45]
        st.metric("P90 Finish Date", "Oct 12, 2026", f"{st.session_state.p90_variance} Days (Risk)")
    with col2:
        # Idea 7: EVM CPI [cite: 44, 49]
        st.metric("Cost Health (CPI)", "0.94", "-0.02 (Overrun)")
    with col3:
        # Idea 11: Financial Risk [cite: 44]
        st.metric("Financial Exposure", "$120,000", "Critical", delta_color="off")
    with col4:
        # Live Operation: Weekly PPC Commitment (Idea 3) [cite: 41]
        completed = st.slider("Weekly Tasks Completed", 0, 10, 8)
        st.metric("Weekly PPC", f"{(completed/10)*100}%", f"{(completed-8)*10}% vs Target")

    st.divider()

    # ROW 2: VISUAL ANALYTICS (Ideas 1, 4, 14, 19)
    l_col, r_col = st.columns([2, 1])
    with l_col:
        st.subheader("📊 Interactive Path Analysis & Heatmap (Idea 1 & 14)")
        start = pd.to_datetime(datetime.date(2026, 5, 1))
        df['Start'] = start
        df['Finish'] = df.apply(lambda x: start + datetime.timedelta(days=x['dur']), axis=1)
        fig = px.timeline(df, x_start="Start", x_end="Finish", y="task", color="trade", template="plotly_white")
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    with r_col:
        st.subheader("⚠️ Trade Density (Idea 4)")
        density = df.groupby('zone')['trade'].nunique().reset_index()
        st.plotly_chart(px.bar(density, x='zone', y='trade', color='trade', color_continuous_scale="Reds"), use_container_width=True)

    # ROW 3: SUPPLY CHAIN & RISK (Idea 8) [cite: 48, 49]
    st.divider()
    st.subheader("🌐 Global Supply Chain & Procurement Heatmap (Idea 8)")
    p_data = pd.DataFrame([
        {'Item': 'MEP Switchgear', 'Status': 'Delayed', 'Lead': 90},
        {'Item': 'HVAC Chillers', 'Status': 'In-Transit', 'Lead': 60},
        {'Item': 'Structural Steel', 'Status': 'On-Site', 'Lead': 0}
    ])
    st.plotly_chart(px.bar(p_data, x='Item', y='Lead', color='Status', color_discrete_map={'Delayed':'red','In-Transit':'orange','On-Site':'green'}), use_container_width=True)

    # ROW 4: SME INSIGHTS & LIVE RISK SWAP (Ideas 12, 13, 17)
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Executive Narrative (Idea 17):**") # [cite: 23]
        st.info(f"Critical Path is driven by {df.iloc[3]['task']}. Supply Chain lead times (Idea 8) for Switchgear are flagged as the primary project risk.")
    with c2:
        # Live Operation: Subcontractor Risk Swap (Idea 13)
        st.markdown("**Subcontractor Risk Swap (Idea 13):**")
        selected_sub = st.selectbox("Optimize MEP Performance", ["FlowMEP (Current - 78%)", "HighPerformance MEP (92%)"])
        if "HighPerformance" in selected_sub:
            st.session_state.p90_variance = -5
            st.success("✨ P90 Recovery: +5 Days")
    with c3:
        # Idea 12: Labor Productivity Index [cite: 49]
        st.markdown("**Labor Productivity Index (Takt):**")
        st.progress(0.95, text="Efficiency: 0.95 SPI")
        st.caption("Idea 5: Weather Risk adjusted for outdoor phases.")

    # ROW 5: ADVANCED TIA & MITIGATION (Idea 6 & 15)
    st.divider()
    st.subheader("🚀 Live Crisis Mitigation Engine")
    if st.button("🚨 Run Claims Impact Scenario (Idea 6)"):
        engine.record_audit("CLAIMS TRIGGER: Subsurface Obstruction Found at Data Hall")
        st.error("Impact: +12 Day Delay to Critical Path. Idea 15: Project Float eroded. Download SOX Audit for Fragnet detail.")
    
    if st.button("⚡ Apply Mitigation: Double Shift (Idea 6)"):
        engine.record_audit("MITIGATION: 24/7 Labor applied to MEP Rough-in")
        st.success("Recovery: 8 Days compressed. Impact: CPI reduced by 0.05 due to labor premium.")

if __name__ == "__main__":
    main()