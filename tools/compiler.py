from data.dataCompiler import DadaCompiler


class Compiler:

    def testText(self):
        return 'test'

    def psi_in_Pa(self, left: str):
        return str(float(left) * DadaCompiler.PSI_IN_PA)


