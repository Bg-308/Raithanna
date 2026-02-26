from pydantic import BaseModel

class EnvironmentalData(BaseModel):
    crop: str
    temperature: float
    humidity: float
    soil_type: str
    soil_moisture: float
    rainfall: float
    growth_stage: str
    