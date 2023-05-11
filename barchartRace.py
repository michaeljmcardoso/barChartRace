# importar as bibliotecas necessárias
import pandas as pd
import bar_chart_race as bcr
import warnings

# desativar a impressão de avisos
warnings.filterwarnings('ignore')

# Ler o arquivo e salvar na variável df
df = pd.read_csv('/home/import_michael/PycharmProjects/barChartRace/dados_serieB_2023_pontos.csv')

# Definindo a coluna Rodadas como índice
df = df.set_index(['Rodadas'])

# Criação da animação do gráfico
bcr.bar_chart_race(
    df=df,  # variável dos dados
    filename='grafico_animado.mp4',  # insira aqui um nome + .mp4 ou .html para gerar o arquivo
    orientation='h',  # orientação do gráfico: horizontal ou vertical
    sort='desc',  # orientar a organização dos dados: ascendente ou descendente
    fixed_max=True,  # mantém o valor máximo fixo (por default é False)
    n_bars=20,  # limita a quantidade de barras no gráfico
    fixed_order=False,  # mantém uma ordem fixa das barras
    steps_per_period=40,  # passos por período
    tick_label_size=7,  # tamanho do texto do eixo x
    bar_label_size=5,  # tamanho do texto do eixo y
    title='Brasileirão Série-B | 2022\nPontos dos Clubes',  # título do gráfico
    title_size='smaller',  # tamanho do título
    period_length=1000,  # quantidade de tempo por período
    interpolate_period=False,  # interpolar linearmente o valor do período
    label_bars=True,  # colocar texto nas barras (por default é True)
    bar_size=.95,  # tamanho das barras
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'color': 'gray', 'va': 'center'},  # texto dos períodos
    cmap='dark24',  # mapa de cores
    filter_column_colors=True)  # filtrar cores das colunas para reduzir repetição
