import pandas as pd

class InputData:
    def __init__(self, path):

        self.datasetPath = path


path = "/content/drive/MyDrive/Mestrado/Reunioes_com_orientador/Orientacao_Individual/artigo_de_metaregras/statlog.csv"
df = pd.read_csv(path)
df.head()