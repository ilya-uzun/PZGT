from dataclasses import dataclass


@dataclass(frozen=True)
class DadaCompiler:
    PSI_IN_ATM: float = 0.068046
    PSI_IN_BAR: float = 0.068948
    PSI_IN_PA: float = 6894.76
    BAR_IN_ATM: float = 0.98692
    BAR_IN_PSI: float = 14.504
    BAR_IN_PA: float = 100000.0
    ATM_IN_BAR: float = 1.01325
    ATM_IN_PSI: float = 14.696
    ATM_IN_PA: float = 101325.0
    PA_IN_BAR: float = -100000.0
    PA_IN_ATM: float = 0.0000098692
    PA_IN_PSI: float = 0.00014504
