# instalar pacote Bar Chart Race
# !pip install bar_chart_race -q

# importar as bibliotecas necessárias
import pandas as pd
import bar_chart_race as bcr
import warnings

# desativar a impressão de avisos
warnings.filterwarnings('ignore')

# importar o dataset dados_série_b
df = pd.read_csv('/home/import_michael/PycharmProjects/barChartRace/dados_serieB_2022_pontos.csv')

# Criação da animação do gráfico
bcr.bar_chart_race(df = df, title = 'Brasileirão Série B | 2022\nPontos dos Clubes',
                   steps_per_period = 10, period_length = 500,
                   figsize = (6, 3.5), orientation = 'h')
