import math


def hydraulic_analysis(d_small_cm, d_large_cm, e1, e2):
    """
    Calculates mechanical and displacement amplification between two syringes.

    Parameters:
    - d_small_cm: Diameter of the smaller syringe (cm)
    - d_large_cm: Diameter of the larger syringe (cm)
    - e1: Displacement of the larger syringe
    - e2: Displacement of the smaller syringe

    Returns:
    - A dictionary with area_small, area_large, mechanical_advantage,
      displacement_amplification_lift, displacement_amplification_load
    """

    # Convert diameters to radii
    r_small = d_small_cm / 2
    r_large = d_large_cm / 2

    # Compute areas using πr²
    area_small = math.pi * r_small ** 2
    area_large = math.pi * r_large ** 2

    # Mechanical Advantage = Area_large / Area_small
    mechanical_advantage = area_large / area_small

    # Displacement Amplification for both objectives (based on user input)
    displacement_amplification_lift = e2 / e1   # Higher lift: small/big
    displacement_amplification_load = e1 / e2   # Higher load: big/small

    return {
        "area_small_cm²": round(area_small, 3),
        "area_large_cm²": round(area_large, 3),
        "mechanical_advantage": round(mechanical_advantage, 2),
        "displacement_amplification_lift": round(displacement_amplification_lift, 2),
        "displacement_amplification_load": round(displacement_amplification_load, 2)
    }


# Example usage with user input
d_small_cm = float(input("Enter diameter of the smaller syringe (cm): "))
d_large_cm = float(input("Enter diameter of the larger syringe (cm): "))
e1 = float(input("Enter displacement of the larger syringe (E1): "))
e2 = float(input("Enter displacement of the smaller syringe (E2): "))

results = hydraulic_analysis(d_small_cm=d_small_cm, d_large_cm=d_large_cm, e1=e1, e2=e2)
print("Results:")
for key, value in results.items():
    print(f"{key}: {value}")