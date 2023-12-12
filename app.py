#Jogo de charadas
import streamlit as st

questoes={"Eu sou seu irmão, mas você não é meu irmão. Como isso é possível?": "Você é minha irmã", 
          "Quantas patas tem um casal de patos?": "5",
          "Se o dia anterior a ontem é 21, que dia será que vem depois de amanhã?": "25",
          "O que sobe uma chaminé para baixo, mas não desce uma chaminé para cima?": "Um guarda-chuva",
          "O que pode corree, mas nunca anda?": "O rio",
          "Se eu entrei 4 vezes em um lugar, quantas vezes tenho que sair?": "3"}

st.title("Jogo de Charadas")
st.write("Adivinhe as respostas das charadas!")

acertos = 0
erros = 0

for question, answer in questoes.items():
    user_answer = st.text_input(question)
    if user_answer.lower() == answer.lower():
        acertos += 1
        st.write("Resposta correta!")
    else:
              erros += 1
              st.write("Resposta errada. A resposta correta é:", answer)

st.write(f"Você acertou {acertos} charadas e errou {erros} charadas.")
