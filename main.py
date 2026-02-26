from data_models import EnvironmentalData
from advisory_engine import generate_advisory

def main():
    sample_data = EnvironmentalData(
        crop="Tomato",
        temperature=32,
        humidity=85,
        soil_type="Loamy",
        soil_moisture=78,
        rainfall=12,
        growth_stage="Flowering"
    )

    advisory = generate_advisory(sample_data)

    print("\n🌾 Agricultural Advisory Report\n")
    for key, value in advisory.items():
        print(f"{key}:\n{value}\n")

if __name__ == "__main__":
    main()
    