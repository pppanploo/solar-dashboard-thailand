
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="☀️ Solar Dashboard", layout="wide")

st.title("☀️ Solar Monitoring Dashboard")
st.markdown("อัปโหลดไฟล์ CSV เพื่อดูข้อมูลพลังงานจาก Inverter")

uploaded_file = st.file_uploader("เลือกไฟล์ CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # ตรวจสอบคอลัมน์
    required_cols = {"site", "inverter", "brand", "timestamp", "power_kw", "energy_today_kwh", "energy_total_kwh"}
    if not required_cols.issubset(df.columns):
        st.error(f"ไฟล์ต้องมีคอลัมน์ดังนี้: {', '.join(required_cols)}")
    else:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        site_selected = st.selectbox("เลือกไซต์", ["ทั้งหมด"] + sorted(df["site"].unique().tolist()))
        if site_selected != "ทั้งหมด":
            df = df[df["site"] == site_selected]

        inverter_selected = st.selectbox("เลือก Inverter", ["ทั้งหมด"] + sorted(df["inverter"].unique().tolist()))
        if inverter_selected != "ทั้งหมด":
            df = df[df["inverter"] == inverter_selected]

        st.markdown("### กราฟพลังงาน (kW)")
        st.line_chart(df.set_index("timestamp")["power_kw"])

        st.markdown("### ตารางข้อมูลล่าสุด")
        st.dataframe(df.tail(20), use_container_width=True)

        st.markdown("### 💳 คำนวณค่าพลังงาน (Billing)")
        rate = st.number_input("ราคาต่อหน่วย (บาท/หน่วย)", value=4.20)
        total_energy = df["energy_today_kwh"].iloc[-1]
        total_cost = total_energy * rate
        st.success(f"พลังงานวันนี้: {total_energy:.2f} kWh → ค่าไฟฟ้าโดยประมาณ: {total_cost:.2f} บาท")

        st.markdown("### 📥 Export เป็น Excel")
        export_btn = st.button("📤 ดาวน์โหลดข้อมูลเป็น Excel")
        if export_btn:
            towrite = io.BytesIO()
            with pd.ExcelWriter(towrite, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="EnergyData")
            towrite.seek(0)
            st.download_button("📄 ดาวน์โหลด Excel", data=towrite, file_name="energy_export.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
else:
    st.info("กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้น")
