class Converter:
    # Conversion factors to meters for each unit
    conversion_to_meters = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.344,
        'kilometers': 1000.0,
        'meters': 1.0,
        'centimeters': 0.01,
        'millimeters': 0.001
    }

    def __init__(self, length, unit):  # Corrected the constructor name to __init__
        if unit not in self.conversion_to_meters:
            raise ValueError("Invalid unit. Supported units are: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")
        self.length_in_meters = length * self.conversion_to_meters[unit]

    def inches(self):
        return self.length_in_meters / self.conversion_to_meters['inches']

    def feet(self):
        return self.length_in_meters / self.conversion_to_meters['feet']

    def yards(self):
        return self.length_in_meters / self.conversion_to_meters['yards']

    def miles(self):
        return self.length_in_meters / self.conversion_to_meters['miles']

    def kilometers(self):
        return self.length_in_meters / self.conversion_to_meters['kilometers']

    def meters(self):
        return self.length_in_meters

    def centimeters(self):
        return self.length_in_meters / self.conversion_to_meters['centimeters']

    def millimeters(self):
        return self.length_in_meters / self.conversion_to_meters['millimeters']

# Example usage
c = Converter(9, 'inches')  # 9 inches as the input

# Displaying the conversions
print("Original Length: 9 inches")
print("Converted to Meters (base unit):", c.meters())  # 9 * 0.0254 = 0.2286 meters
print("Converted to Feet:", c.feet())  # Conversion to feet
print("Converted to Yards:", c.yards())  # Conversion to yards
print("Converted to Miles:", c.miles())  # Conversion to miles
print("Converted to Kilometers:", c.kilometers())  # Conversion to kilometers
print("Converted to Centimeters:", c.centimeters())  # Conversion to centimeters
print("Converted to Millimeters:", c.millimeters())  # Conversion to millimeters
