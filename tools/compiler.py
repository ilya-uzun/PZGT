from data.dataCompiler import DadaCompiler


class Compiler:

    def testText(self):
        return 'test'

    def psi_in_Pa(self, left: str):
        print(left)
        print(type(left))

        # x = float(left)
        # print(x)
        # print(type(x))
        return str(float(left) * DadaCompiler.PSI_IN_PA)


