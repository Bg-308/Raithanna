"""
Streamlit UI for Farmer Future - Agricultural Advisory.
"""
import streamlit as st
from data_models import EnvironmentalData
from advisory_engine import generate_advisory

st.set_page_config(
    page_title="Farmer Future | Agricultural Advisory",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom style for a clean, farm-themed look
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #2d5a27;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        color: #5a7d52;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .stMetric {
        background: linear-gradient(135deg, #f0f7ee 0%, #e8f0e4 100%);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2d5a27;
    }
    .advisory-section {
        background: #f8faf8;
        padding: 1.25rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #e0e8dc;
    }
    .advisory-title {
        font-weight: 600;
        color: #2d5a27;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🌾 Farmer Future</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-powered agricultural advisory based on your environmental data</p>', unsafe_allow_html=True)

with st.form("advisory_form"):
    col1, col2 = st.columns(2)

    with col1:
        crop = st.text_input("Crop", value="Tomato", placeholder="e.g. Tomato, Wheat, Rice")
        temperature = st.slider("Temperature (°C)", 0.0, 50.0, 32.0, 0.5)
        humidity = st.slider("Humidity (%)", 0.0, 100.0, 85.0, 1.0)
        soil_type = st.selectbox(
            "Soil Type",
            ["Loamy", "Sandy", "Clay", "Silty", "Peaty", "Chalky"],
            index=0,
        )

    with col2:
        soil_moisture = st.slider("Soil Moisture (%)", 0.0, 100.0, 78.0, 1.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=12.0, step=0.5)
        growth_stage = st.selectbox(
            "Growth Stage",
            ["Seedling", "Vegetative", "Flowering", "Fruiting", "Harvest"],
            index=2,
        )

    submitted = st.form_submit_button("Generate Advisory")

if submitted:
    try:
        env_data = EnvironmentalData(
            crop=crop,
            temperature=temperature,
            humidity=humidity,
            soil_type=soil_type,
            soil_moisture=soil_moisture,
            rainfall=rainfall,
            growth_stage=growth_stage,
        )

        with st.spinner("Generating advisory..."):
            advisory = generate_advisory(env_data)

        st.success("Advisory generated successfully.")

        def format_value(v):
            if isinstance(v, dict):
                lines = []
                for k, val in v.items():
                    label = k.replace("_", " ").title()
                    if isinstance(val, list):
                        lines.append(f"**{label}:**\n" + "\n".join(f"- {item}" for item in val))
                    else:
                        lines.append(f"**{label}:** {val}")
                return "\n\n".join(lines)
            if isinstance(v, list):
                return "\n".join(f"- {item}" for item in v)
            return str(v)

        for key, value in advisory.items():
            title = key.replace("_", " ").title()
            st.subheader(title)
            st.markdown(format_value(value))

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        st.info("Check that OPENAI_API is set in your .env file.")
