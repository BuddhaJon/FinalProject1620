class InflationCalculator:
    """Class to calculate compound interest."""

    def calculate(self, principal: float, rate: float, time: int, compound_per_year: int = 1) -> float:
        """Calculate the amount of compound interest accrued over time."""
        return principal * (1 + rate / compound_per_year) ** (compound_per_year * time)
