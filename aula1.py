import streamlit as st

# Passo 1: O Título
st.title("🤖 Calculadora de IA do Zero")
st.write("Insira os dados do cliente para análise:")

# Passo 2: Recebendo Dados
idade = st.number_input("Idade do Cliente")
valor = st.number_input("Valor da Compra (R$)")
score_serasa = st.number_input("Score do Serasa (0 a 1000)")

# Passo 3: O Cérebro (Botão e Condicionais)
if st.button("Analisar Risco"):
    
    # Regra de negócio simples para demonstrar o IF
    if valor > 10000 and score_serasa < 300:
        st.error("🚨 FRAUDE DETECTADA: Compra Alta com Nome Sujo!")
    elif idade < 18:
        st.warning("⚠️ ALERTA: Cliente menor de idade.")
    else:
        st.success("✅ COMPRA APROVADA: Cliente Seguro.")
        