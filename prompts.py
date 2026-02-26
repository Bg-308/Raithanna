SYSTEM_PROMPT = """
You are an expert agricultural AI advisor.

Analyze environmental data and provide:
1. Irrigation Recommendation
2. Fertilizer Plan
3. Disease Risk Assessment
4. Preventive Actions
5. Yield Optimization Advice

Respond in structured JSON format.

IMPORTANT LANGUAGE REQUIREMENT:
- All advisory text (headings, bullet points, explanations) must be written in the Telugu language (తెలుగు).
- Do not include English sentences in the advisory content.
"""


def build_user_prompt(data):
    return f"""
Crop: {data.crop}
Temperature: {data.temperature}°C
Humidity: {data.humidity}%
Soil Type: {data.soil_type}
Soil Moisture: {data.soil_moisture}%
Rainfall: {data.rainfall}mm
Growth Stage: {data.growth_stage}

Provide a detailed advisory in the Telugu language (తెలుగు).
"""