def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    print("The area is:", calculate_area(radius))
