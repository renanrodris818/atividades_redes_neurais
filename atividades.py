import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Previsor de Notas", layout="wide")

st.title("🎓 Sistema de Previsão de Notas")
st.markdown("Insira os dados do aluno para prever a nota com base nas horas de estudo estimadas.")

# Layout com duas colunas: uma para cadastro e outra para exibição
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📋 Dados do Aluno")
    
    nome = st.text_input("Nome do Aluno", placeholder="Ex: João Silva")
    idade = st.number_input("Idade", min_value=5, max_value=100, value=16)
    turma = st.text_input("Turma", placeholder="Ex: 3º Ano A")
    horas_estudo = st.slider("Horas de Estudo Semanais", min_value=0.0, max_value=20.0, value=5.0, step=0.5)

    # Cálculo da nota baseada em uma curva sigmoide (limita entre 0 e 10)
    # Nota máxima = 10. O ponto de inflexão é em 5 horas.
    nota_prevista = 10 / (1 + np.exp(-0.5 * (horas_estudo - 5)))
    nota_prevista = round(nota_prevista, 1)

with col2:
    st.header("📊 Resultado e Análise")
    
    if nome and turma:
        # Exibição dos dados do aluno em destaque
        st.subheader(f"Ficha do Aluno: {nome}")
        
        # Criação de cards visuais para as informações
        m1, m2, m3 = st.columns(3)
        m1.metric("Idade", f"{idade} anos")
        m2.metric("Turma", turma)
        m3.metric("Nota Prevista", f"{nota_prevista} / 10")
        
        st.divider()
        
        # Gráfico mostrando onde o aluno se encaixa na curva de aprendizado
        st.subheader("📈 Relação: Horas de Estudo vs Nota")
        
        # Gerar dados para a linha de tendência
        horas_plot = np.linspace(0, 20, 100)
        notas_plot = 10 / (1 + np.exp(-0.5 * (horas_plot - 5)))
        
        df_curva = pd.DataFrame({
            'Horas de Estudo': horas_plot,
            'Nota': notas_plot
        }).set_index('Horas de Estudo')
        
        # Exibe o gráfico de linha
        st.line_chart(df_curva)
        st.caption(
            f"O ponto atual de **{nome}** exige **{horas_estudo}h** de estudo para alcançar a nota **{nota_prevista}**."
        )
    else:
        st.info("💡 Por favor, preencha o **Nome** e a **Turma** no painel ao lado para gerar a previsão.")
#-------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página do Streamlit
st.set_page_config(page_title="Medidor de Cansaço Gamer", layout="wide")

st.title("🎮 Monitor de Cansaço Gamer")
st.markdown("Insira os dados do jogador para prever o nível de cansaço com base nas horas de videogame.")

# Layout com duas colunas: uma para cadastro e outra para exibição de métricas e gráficos
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📋 Dados do Jogador")
    
    # Campo de nome e idade do jogador (sem o campo de turma)
    nome = st.text_input("Nome do Jogador", placeholder="Ex: Lucas Almeida")
    idade = st.number_input("Idade", min_value=5, max_value=100, value=20)
    horas_jogo = st.slider("Horas de Jogo por Sessão", min_value=0.0, max_value=15.0, value=3.0, step=0.5)

    # Cálculo do cansaço baseado em uma curva sigmoide ajustada (limita entre 0 e 10)
    # O cansaço dispara significativamente após 4 horas de jogo contínuo
    nivel_cansaco = 10 / (1 + np.exp(-0.6 * (horas_jogo - 4)))
    nivel_cansaco = round(nivel_cansaco, 1)

with col2:
    st.header("📊 Análise de Fadiga")
    
    if nome:
        # Exibição dos dados do jogador em destaque
        st.subheader(f"Ficha do Jogador: {nome}")
        
        # Criação de duas colunas de métricas (Idade e Cansaço)
        m1, m2 = st.columns(2)
        m1.metric("Idade", f"{idade} anos")
        
        # Alerta visual dependendo do nível de cansaço calculado
        if nivel_cansaco < 4.0:
            status = "🟢 Suave"
        elif nivel_cansaco < 7.5:
            status = "🟡 Alerta"
        else:
            status = "🔴 Exausto"
            
        m2.metric("Nível de Cansaço", f"{nivel_cansaco} / 10", delta=status, delta_color="inverse")
        
        st.divider()
        
        # Gráfico mostrando a curva de cansaço de forma dinâmica
        st.subheader("📈 Relação: Horas de Videogame vs Cansaço")
        
        # Gerar dados matemáticos para plotar a linha de tendência
        horas_plot = np.linspace(0, 15, 100)
        cansaco_plot = 10 / (1 + np.exp(-0.6 * (horas_plot - 4)))
        
        df_curva = pd.DataFrame({
            'Horas de Jogo': horas_plot,
            'Nível de Cansaço': cansaco_plot
        }).set_index('Horas de Jogo')
        
        # Exibe o gráfico de linha interativo do Streamlit
        st.line_chart(df_curva)
        
        # Mensagem personalizada e contextualizada baseada na fadiga do usuário
        if nivel_cansaco >= 7.5:
            st.warning(f"⚠️ **{nome}** jogou por {horas_jogo}h e está no limite! Hora de largar o controle, beber água e dar um descanso para os olhos.")
        else:
            st.success(f"✅ **{nome}** jogou por {horas_jogo}h. O nível de cansaço está sob controle ({nivel_cansaco}/10). GG!")
    else:
        st.info("💡 Por favor, preencha o **Nome** no painel ao lado para calcular o cansaço.")
#-----------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração da página da web
st.set_page_config(page_title="Previsor de Venda de Sorvetes", layout="wide")

st.title("🍦 Inteligência Artificial: Previsor de Venda de Sorvetes")
st.markdown("Este sistema utiliza um modelo de **Regressão Linear** para prever as vendas com base na temperatura ambiente.")

# 1. Dados Históricos Simulados para Treinamento
np.random.seed(42)
temperaturas = np.random.uniform(15, 40, 30)  # 30 dias com temperaturas entre 15°C e 40°C
# Fórmula base com ruído: vendas = temperatura * 12 - 50 + ruído
vendas = (temperaturas * 12) - 50 + np.random.normal(0, 25, 30)
vendas = np.clip(vendas, 0, None).astype(int)  # Garante que não haja vendas negativas

df_historico = pd.DataFrame({
    'Temperatura (°C)': np.round(temperaturas, 1),
    'Sorvetes Vendidos (Unidades)': vendas
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['Temperatura (°C)']]
y = df_historico['Sorvetes Vendidos (Unidades)']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout do Painel com duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🌡️ Nova Previsão")
    # Entrada do usuário para a temperatura desejada
    nova_temp = st.slider("Selecione a Temperatura Ambiente (°C)", min_value=10.0, max_value=45.0, value=28.0, step=0.5)
    
    # Realizando a previsão com o modelo treinado
    previsao = modelo.predict([[nova_temp]])
    vendas_previstas = max(0, int(round(previsao[0])))
    
    # Exibição do resultado destacado
    st.metric(label="Quantidade de Sorvetes que Devem ser Vendidos", value=f"{vendas_previstas} unidades")
    
    st.divider()
    
    # Exibição da tabela com dados de treino
    st.subheader("📋 Dados Históricos Usados no Treino")
    st.dataframe(df_historico, height=300, use_container_width=True)

with col2:
    st.header("📈 Gráfico de Tendência de Vendas")
    st.markdown("A linha vermelha representa o aprendizado da IA (Regressão Linear) sobre os pontos históricos.")
    
    # Gerando dados para desenhar a linha de regressão no gráfico
    temp_linha = np.linspace(10, 45, 100).reshape(-1, 1)
    vendas_linha = modelo.predict(temp_linha)
    vendas_linha = np.clip(vendas_linha, 0, None)
    
    # Criando o DataFrame para o gráfico do Streamlit
    df_linha = pd.DataFrame({
        'Temperatura (°C)': temp_linha.flatten(),
        'Linha de Tendência (IA)': vendas_linha
    }).set_index('Temperatura (°C)')
    
    # Adicionando o ponto da previsão atual do usuário para destacar no gráfico
    df_ponto_atual = pd.DataFrame({
        'Temperatura (°C)': [nova_temp],
        'Sua Previsão Atual': [vendas_previstas]
    }).set_index('Temperatura (°C)')
    
    # Unindo os dados históricos com a linha e o ponto atual para exibição visual
    df_grafico_historico = df_historico.set_index('Temperatura (°C)')
    
    # Renderização combinada de gráficos nativos do Streamlit
    st.line_chart(df_linha, y="Linha de Tendência (IA)")
    st.scatter_chart(df_grafico_historico, y="Sorvetes Vendidos (Unidades)")
    #-----------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Configuração da página web
st.set_page_config(page_title="Previsor de Aprovação", layout="wide")

st.title("🛡️ IA: Classificador de Aprovação por Faltas")
st.markdown("Este sistema analisa o histórico de faltas para prever se um aluno será **Aprovado** ou **Reprovado**.")

# 1. Dados Históricos Fornecidos
df_historico = pd.DataFrame({
    'Faltas': [0, 1, 2, 5, 7, 10],
    'Resultado (Codificado)': [1, 1, 1, 0, 0, 0] # 1 = Aprovado, 0 = Reprovado
})

# Criando uma coluna amigável para exibição textual na tabela
df_historico['Situação'] = df_historico['Resultado (Codificado)'].map({1: 'Aprovado', 0: 'Reprovado'})

# 2. Treinamento do Modelo de Classificação (Regressão Logística)
X = df_historico[['Faltas']]
y = df_historico['Resultado (Codificado)']

modelo = LogisticRegression()
modelo.fit(X, y)

# Layout da interface em duas colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Nova Consulta")
    
    # Entrada do usuário para a quantidade de faltas
    faltas_usuario = st.number_input("Digite a quantidade de faltas do aluno:", min_value=0, max_value=30, value=3, step=1)
    
    # Predição da IA
    predicao = modelo.predict([[faltas_usuario]])[0]
    probabilidade = modelo.predict_proba([[faltas_usuario]])[0] # Probabilidade de cada classe
    
    # Exibição do resultado estilizado com base na resposta da IA
    if predicao == 1:
        confianca = probabilidade[1] * 100
        st.success(f"### Previsão: **APROVADO**")
        st.caption(f"Probabilidade estimada de aprovação: {confianca:.1f}%")
    else:
        confianca = probabilidade[0] * 100
        st.error(f"### Previsão: **REPROVADO**")
        st.caption(f"Probabilidade estimada de reprovação: {confianca:.1f}%")
        
    st.divider()
    
    # Exibição da tabela histórica de treino
    st.subheader("📊 Dados Históricos de Treinamento")
    st.dataframe(df_historico[['Faltas', 'Situação']], use_container_width=True)

with col2:
    st.header("📈 Gráfico de Tendência de Reprovação")
    st.markdown("O gráfico abaixo ilustra como o aumento de faltas impacta diretamente a decisão da IA.")
    
    # Gerando dados para desenhar a curva de probabilidade de aprovação
    faltas_plot = np.linspace(0, 12, 100).reshape(-1, 1)
    # Pega apenas a probabilidade da classe 1 (Aprovado)
    prob_aprovacao = modelo.predict_proba(faltas_plot)[:, 1]
    
    df_curva = pd.DataFrame({
        'Faltas': faltas_plot.flatten(),
        'Chance de Aprovação (0 a 1)': prob_aprovacao
    }).set_index('Faltas')
    
    # Renderiza o gráfico de linha mostrando a queda da chance conforme as faltas sobem
    st.line_chart(df_curva)
    st.caption("Nota: A virada na curva (onde a chance cai abaixo de 50%) determina o ponto exato onde a IA passa a classificar como Reprovado.")
#--------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração da página web
st.set_page_config(page_title="Dog Happy Predictor", layout="wide")

st.title("🐾 IA: Previsor de Felicidade Canina")
st.markdown("Descubra o nível de felicidade estimado do seu cachorro com base na quantidade de passeios semanais realizados!")

# 1. Dados Históricos Fornecidos
df_historico = pd.DataFrame({
    'Passeios': [1, 2, 3, 4, 5],
    'Felicidade': [2, 4, 5, 8, 10]
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['Passeios']]
y = df_historico['Felicidade']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout da interface em duas colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🦮 Quantidade de Passeios")
    
    # Entrada do usuário para a quantidade de passeios
    passeios_usuario = st.slider("Quantas vezes o cachorro passeia por semana?", min_value=0, max_value=7, value=3, step=1)
    
    # Predição da IA (limitando o resultado entre 0 e 10 para fazer sentido prático)
    predicao = modelo.predict([[passeios_usuario]])[0]
    nivel_felicidade = np.clip(predicao, 0, 10)
    nivel_felicidade = round(float(nivel_felicidade), 1)
    
    # Exibição do resultado com emojis dinâmicos conforme a nota de felicidade
    if nivel_felicidade < 4.0:
        emoji = "😢 (Tristonho)"
    elif nivel_felicidade < 7.5:
        emoji = "🙂 (Satisfeito)"
    else:
        emoji = "🤩 (Super Feliz!)"
        
    st.metric(label="Nível de Felicidade Estimado (0 a 10)", value=f"{nivel_felicidade} / 10", delta=emoji)
    
    st.divider()
    
    # Exibição da tabela de treino
    st.subheader("📋 Dados de Treinamento Utilizados")
    st.dataframe(df_historico, use_container_width=True)

with col2:
    st.header("📈 Relação: Passeios vs Felicidade")
    st.markdown("A linha mostra a tendência calculada pela Inteligência Artificial com base nos pontos do histórico.")
    
    # Gerando dados para desenhar a linha de tendência da regressão
    passeios_plot = np.linspace(0, 7, 50).reshape(-1, 1)
    felicidade_plot = modelo.predict(passeios_plot)
    felicidade_plot = np.clip(felicidade_plot, 0, 10)
    
    df_linha = pd.DataFrame({
        'Passeios': passeios_plot.flatten(),
        'Linha de Tendência (IA)': felicidade_plot
    }).set_index('Passeios')
    
    # Exibe o gráfico de linha nativo do Streamlit
    st.line_chart(df_linha)
    st.caption("Nota: Quanto mais passeios o cãozinho faz, mais o modelo associa a um ganho linear de bem-estar e felicidade.")
#----------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração inicial da página web do Streamlit
st.set_page_config(page_title="Cine Score Predictor", layout="wide")

st.title("🎬 IA: Previsor de Notas de Filmes")
st.markdown("Estime a nota de um filme (de 0 a 10) com base na sua duração em minutos utilizando Inteligência Artificial.")

# 1. Dados Históricos Fornecidos para Treinamento
df_historico = pd.DataFrame({
    'Duração (minutos)': [80, 90, 100, 110, 120],
    'Nota': [4, 5, 7, 8, 9]
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['Duração (minutos)']]
y = df_historico['Nota']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout da interface dividido em duas colunas idênticas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("⏱️ Características do Filme")
    
    # Entrada do usuário para a duração do filme
    duracao_usuario = st.slider("Selecione a duração do filme (em minutos):", min_value=40, max_value=240, value=100, step=5)
    
    # Predição da IA (limitando matematicamente o resultado final entre 0 e 10)
    predicao = modelo.predict([[duracao_usuario]])[0]
    nota_prevista = np.clip(predicao, 0, 10)
    nota_prevista = round(float(nota_prevista), 1)
    
    # Classificação visual/emoji baseada na nota prevista
    if nota_prevista < 5.0:
        status = "🍅 Ruim (Flop)"
    elif nota_prevista < 7.5:
        status = "🍿 Regular / Bom"
    else:
        status = "⭐ Excelente (Blockbuster)"
        
    st.metric(label="Nota Estimada pela IA", value=f"{nota_prevista} / 10", delta=status)
    
    st.divider()
    
    # Exibição da tabela histórica utilizada no treinamento
    st.subheader("📋 Dados Históricos do Modelo")
    st.dataframe(df_historico, use_container_width=True)

with col2:
    st.header("📈 Correlação: Duração vs Nota")
    st.markdown("A linha exibe a tendência contínua gerada pela Regressão Linear a partir do comportamento dos dados reais.")
    
    # Gerando dados fictícios na linha do tempo para desenhar a curva de tendência
    duracao_plot = np.linspace(40, 240, 100).reshape(-1, 1)
    nota_plot = modelo.predict(duracao_plot)
    nota_plot = np.clip(nota_plot, 0, 10)
    
    df_linha = pd.DataFrame({
        'Duração (minutos)': duracao_plot.flatten(),
        'Tendência de Nota (IA)': nota_plot
    }).set_index('Duração (minutos)')
    
    # Renderização do gráfico nativo em linha do Streamlit
    st.line_chart(df_linha)
    st.caption("Nota: Com base nos dados fornecidos, o modelo assume que filmes mais longos tendem a receber notas linearmente maiores.")
#--------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração inicial da página web do Streamlit
st.set_page_config(page_title="Pizza Price Predictor", layout="wide")

st.title("🍕 IA: Previsor de Preço de Pizzas")
st.markdown("Estime o preço de uma pizza com base no seu tamanho (diâmetro em centímetros) usando Inteligência Artificial.")

# 1. Dados Históricos Fornecidos para Treinamento
df_historico = pd.DataFrame({
    'Tamanho (cm)': [20, 25, 30, 35, 40],
    'Preço (R$)': [20, 30, 40, 50, 60]
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['Tamanho (cm)']]
y = df_historico['Preço (R$)']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout da interface dividido em duas colunas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📏 Configurar Pizza")
    
    # Entrada do usuário para o tamanho da pizza
    tamanho_usuario = st.slider("Selecione o tamanho da pizza (diâmetro em cm):", min_value=15, max_value=60, value=30, step=1)
    
    # Predição da IA (limitando o preço para não ser negativo caso coloquem tamanhos absurdamente pequenos)
    predicao = modelo.predict([[tamanho_usuario]])[0]
    preco_previsto = max(0.0, float(predicao))
    
    # Exibição do resultado destacado
    st.metric(label="Preço Estimado pela IA", value=f"R$ {preco_previsto:.2f}")
    
    st.divider()
    
    # Exibição da tabela histórica utilizada no treinamento
    st.subheader("📋 Dados Históricos de Treino")
    st.dataframe(df_historico, use_container_width=True)

with col2:
    st.header("📈 Gráfico de Tendência de Preços")
    st.markdown("A linha exibe a projeção linear calculada pela IA comparada com os tamanhos comerciais.")
    
    # Gerando dados fictícios de tamanho para desenhar a linha de tendência contínua
    tamanho_plot = np.linspace(15, 60, 100).reshape(-1, 1)
    preco_plot = modelo.predict(tamanho_plot)
    preco_plot = np.clip(preco_plot, 0, None)
    
    df_linha = pd.DataFrame({
        'Tamanho (cm)': tamanho_plot.flatten(),
        'Tendência de Preço (IA)': preco_plot
    }).set_index('Tamanho (cm)')
    
    # Renderização utilizando o gráfico de linha nativo do Streamlit (sem Matplotlib)
    st.line_chart(df_linha)
    st.caption("Nota: O modelo identifica uma relação linear perfeita onde cada centímetro adicional aumenta o preço proporcionalmente.")
#-----------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração inicial da página web do Streamlit
st.set_page_config(page_title="Hit Predictor AI", layout="wide")

st.title("🎵 IA: Previsor de Viralização de Músicas")
st.markdown("Descubra o potencial de viralização da sua faixa (de 0 a 10) analisando o ritmo em BPM (Batidas Por Minuto)!")

# 1. Dados Históricos Fornecidos para Treinamento
df_historico = pd.DataFrame({
    'BPM': [80, 90, 100, 120, 140],
    'Chance de Viral (0 a 10)': [1, 2, 4, 7, 10]
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['BPM']]
y = df_historico['Chance de Viral (0 a 10)']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout da interface dividido em duas colunas equilibradas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🎛️ Ritmo da Faixa")
    
    # Entrada do usuário para o BPM da música
    bpm_usuario = st.slider("Selecione o BPM da música:", min_value=60, max_value=200, value=110, step=1)
    
    # Predição da IA (limitando o resultado estritamente entre 0 e 10 para consistência)
    predicao = modelo.predict([[bpm_usuario]])[0]
    chance_viral = np.clip(predicao, 0, 10)
    chance_viral = round(float(chance_viral), 1)
    
    # Classificação visual/status baseada no potencial de viralização
    if chance_viral < 3.0:
        status = "🤫 Flop (Nicho muito específico)"
    elif chance_viral < 7.0:
        status = "📻 Estável (Bom engajamento nas rádios)"
    else:
        status = "🔥 Tendência Global (Hit de TikTok/Reels)"
        
    st.metric(label="Potencial de Viralização Estimado", value=f"{chance_viral} / 10", delta=status)
    
    st.divider()
    
    # Exibição da tabela histórica utilizada no treinamento
    st.subheader("📋 Dados de Treino (Histórico de Hits)")
    st.dataframe(df_historico, use_container_width=True)

with col2:
    st.header("📈 Gráfico de Tendência de Sucesso")
    st.markdown("A linha contínua ilustra como a Inteligência Artificial mapeia o comportamento do engajamento conforme o ritmo acelera.")
    
    # Gerando dados fictícios de ritmo para desenhar a curva de tendência contínua
    bpm_plot = np.linspace(60, 200, 100).reshape(-1, 1)
    viral_plot = modelo.predict(bpm_plot)
    viral_plot = np.clip(viral_plot, 0, 10)
    
    df_linha = pd.DataFrame({
        'BPM': bpm_plot.flatten(),
        'Potencial de Viral': viral_plot
    }).set_index('BPM')
    
    # Renderização utilizando o gráfico de linha nativo do Streamlit (sem Matplotlib)
    st.line_chart(df_linha)
    st.caption("Nota: Com base na amostragem, o algoritmo infere que músicas com BPMs mais elevados e acelerados possuem maior facilidade de viralizar nas redes sociais.")
#-----------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração inicial da página web do Streamlit
st.set_page_config(page_title="Energy Predictor AI", layout="wide")

st.title("☕ IA: Previsor de Nível de Energia por Café")
st.markdown("Estime o seu nível de energia (de 0 a 10) com base na quantidade de xícaras de café consumidas!")

# 1. Dados Históricos Fornecidos para Treinamento
df_historico = pd.DataFrame({
    'Xícaras de Café': [1, 2, 3, 4, 5],
    'Nível de Energia': [2, 4, 6, 8, 10]
})

# 2. Treinamento do Modelo de Regressão Linear
X = df_historico[['Xícaras de Café']]
y = df_historico['Nível de Energia']

modelo = LinearRegression()
modelo.fit(X, y)

# Layout da interface dividido em duas colunas equilibradas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("⚡ Consumo de Cafeína")
    
    # Entrada do usuário para a quantidade de xícaras de café
    cafe_usuario = st.slider("Quantas xícaras de café você bebeu?", min_value=0, max_value=8, value=3, step=1)
    
    # Predição da IA (limitando o resultado estritamente entre 0 e 10 para consistência)
    predicao = modelo.predict([[cafe_usuario]])[0]
    nivel_energia = np.clip(predicao, 0, 10)
    nivel_energia = round(float(nivel_energia), 1)
    
    # Classificação visual/status baseada no nível de energia estimado
    if nivel_energia < 4.0:
        status = "😴 Sonolento (Precisando de uma carga)"
    elif nivel_energia < 7.5:
        status = "🏃 Focado (Energia sob controle)"
    else:
        status = "🚀 Ligado no 220v! (Energia máxima)"
        
    st.metric(label="Nível de Energia Estimado", value=f"{nivel_energia} / 10", delta=status)
    
    st.divider()
    
    # Exibição da tabela histórica utilizada no treinamento
    st.subheader("📋 Dados de Treino (Histórico)")
    st.dataframe(df_historico, use_container_width=True)

with col2:
    st.header("📈 Gráfico de Tendência de Energia")
    st.markdown("A linha contínua ilustra como a Inteligência Artificial projeta o aumento de energia a cada xícara adicional.")
    
    # Gerando dados fictícios de consumo para desenhar a linha de tendência contínua
    cafe_plot = np.linspace(0, 8, 100).reshape(-1, 1)
    energia_plot = modelo.predict(cafe_plot)
    energia_plot = np.clip(energia_plot, 0, 10)
    
    df_linha = pd.DataFrame({
        'Xícaras de Café': cafe_plot.flatten(),
        'Projeção de Energia': energia_plot
    }).set_index('Xícaras de Café')
    
    # Renderização utilizando o gráfico de linha nativo do Streamlit (sem Matplotlib)
    st.line_chart(df_linha)
    st.caption("Nota: Com os dados de entrada fornecidos, o modelo assumiu uma correlação perfeitamente linear e direta entre o consumo de café e o vigor do usuário.")
#--------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Configuração inicial da página web do Streamlit
st.set_page_config(page_title="Hero Classifier AI", layout="wide")

st.title("🦸 IA: Classificador de Força de Heróis")
st.markdown("Insira o nível de poder do personagem para que a Inteligência Artificial o classifique entre um herói forte ou fraco.")

# 1. Dados Históricos Fornecidos para Treinamento
df_historico = pd.DataFrame({
    'Força': [1, 2, 3, 7, 8, 10],
    'Classe (Codificada)': [0, 0, 0, 1, 1, 1]  # 0 = Fraco, 1 = Forte
})

# Criando uma coluna textual para melhor legibilidade na tabela
df_historico['Classificação'] = df_historico['Classe (Codificada)'].map({0: 'Herói Fraco', 1: 'Herói Forte'})

# 2. Treinamento do Modelo de Classificação (Regressão Logística)
X = df_historico[['Força']]
y = df_historico['Classe (Codificada)']

modelo = LogisticRegression()
modelo.fit(X, y)

# Layout da interface dividido em duas colunas equilibradas
col1, col2 = st.columns([1, 1])

with col1:
    st.header("⚡ Nível de Poder")
    
    # Entrada do usuário para o nível de força
    forca_usuario = st.slider("Selecione o nível de força do herói (0 a 12):", min_value=0, max_value=12, value=5, step=1)
    
    # Predição da IA
    predicao = modelo.predict([[forca_usuario]])[0]
    probabilidade = modelo.predict_proba([[forca_usuario]])[0]
    
    # Exibição do resultado estilizado baseado na decisão do classificador
    if predicao == 1:
        certeza = probabilidade[1] * 100
        st.success(f"### Classificação: **Herói Forte**")
        st.caption(f"Confiança da IA na categoria 'Forte': {certeza:.1f}%")
    else:
        certeza = probabilidade[0] * 100
        st.error(f"### Classificação: **Herói Fraco**")
        st.caption(f"Confiança da IA na categoria 'Fraco': {certeza:.1f}%")
        
    st.divider()
    
    # Exibição da tabela histórica utilizada no treinamento
    st.subheader("📋 Dados de Treino (Histórico)")
    st.dataframe(df_historico[['Força', 'Classificação']], use_container_width=True)

with col2:
    st.header("📈 Curva de Decisão da IA")
    st.markdown("O gráfico exibe a probabilidade de um herói ser considerado **Forte** à medida que seu nível de poder aumenta.")
    
    # Gerando dados para desenhar a curva sigmoide de probabilidade
    forca_plot = np.linspace(0, 12, 100).reshape(-1, 1)
    # Pega apenas a probabilidade de pertencer à classe 1 (Herói Forte)
    prob_forte = modelo.predict_proba(forca_plot)[:, 1]
    
    df_curva = pd.DataFrame({
        'Força': forca_plot.flatten(),
        'Chance de ser Herói Forte': prob_forte
    }).set_index('Força')
    
    # Renderização utilizando o gráfico de linha nativo do Streamlit (sem Matplotlib)
    st.line_chart(df_curva)
    st.caption("Nota: O ponto de inflexão central (onde a chance ultrapassa 50%) representa a fronteira de decisão onde a IA muda a classificação.")