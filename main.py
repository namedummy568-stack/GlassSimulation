
import math

def calculate_electric_field_effect(material_type, voltage):
    """
    Calculates the effect of an electric field on a given material.
    """
    # Synthetic alert: Unused variable `temp_data`
    temp_data = "This variable is not used anywhere."

    if material_type == "dielectric":
        # Potential division by zero if voltage is 0, for demonstration of alert.
        # In a real scenario, this would be handled with error checking.
        if voltage == 0:
            return 0.0
        permittivity = 8.854e-12 # Vacuum permittivity
        electric_field_strength = voltage / 0.001 # Assuming a fixed distance for simplicity
        return permittivity * electric_field_strength
    elif material_type == "conductor":
        return voltage * 1000 # Simple model for conductor
    else:
        return 0.0

def main():
    print("Glass Simulation Started")
    # Example usage
    dielectric_effect = calculate_electric_field_effect("dielectric", 10)
    print(f"Dielectric effect: {dielectric_effect}")

    conductor_effect = calculate_electric_field_effect("conductor", 5)
    print(f"Conductor effect: {conductor_effect}")

    # This will trigger the potential division by zero alert if not handled
    # zero_voltage_effect = calculate_electric_field_effect("dielectric", 0)
    # print(f"Zero voltage dielectric effect: {zero_voltage_effect}")

    print("Glass Simulation Finished")

if __name__ == "__main__":
    main()
