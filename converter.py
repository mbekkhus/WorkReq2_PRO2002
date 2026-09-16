class FahrenheitToCelsiusConverter:
    """Convert temperatures from Fahrenheit to Celsius."""

    def convert(self, temperature_fahrenheit: float) -> float:
        return (temperature_fahrenheit - 32) * 5 / 9


converter = FahrenheitToCelsiusConverter()
print(converter.convert(212))
