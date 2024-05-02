class LoanCalculator:
    """Class to calculate compound loan interest."""

    def CompoundCalculator(self, principal: float, rate: float, time: int, compound_per_year: int = 1) -> float:
        """Calculate the amount of compound interest accrued over time."""
        return principal * (1 + rate / compound_per_year) ** (compound_per_year * time)


class LoanCalculatorSimple:
    """Class to calculate simple loan interest."""

    def Calculate(self, principal: float, rate: float, time: int) -> float:
        """Calculate the amount of interest accrued over time."""
        return principal * rate * time