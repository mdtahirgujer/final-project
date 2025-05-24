import numpy as np

def calculate_volume(radius, height):
    """
    Calculate the volume of a cylinder.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    return 3.14159 * radius ** 2 * height

def main():
    # Example usage
    radius = 5.0
    height = 10.0
    volume = calculate_volume(radius, height)
    print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume:.2f}")

if __name__ == "__main__":
    main()
