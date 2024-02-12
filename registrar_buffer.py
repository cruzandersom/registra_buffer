import logging
import warnings

import pandas as pd

warnings.filterwarnings("ignore")

logging.basicConfig(filename='importacao_insercao_banco_dados.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

DIRETORIO = 'E:\\PROJETO_OTIF_SEGREGADO\\REPORTS\\'


class RetornaBuffer:

    def __init__(self, arquivo: str):
        self.arquivo = DIRETORIO + arquivo
        self.df = self.retorna_dataframe()

    def retorna_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(
            self.arquivo,
            sep=';',
            encoding='cp1250',
            decimal=',',
            low_memory=False
        )
