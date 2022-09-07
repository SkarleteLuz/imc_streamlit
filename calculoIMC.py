import streamlit as st

st.title('Calculadora de IMC')

peso = st.number_input("Digite o seu peso (em kg)")
status= st.radio("Selecione opção de altura", ('cms', 'metros'))

if(status=='cms'):
	altura = st.number_input("Digite a altura em centímetros")

	try:
		imc = peso / ((altura / 100) **2)
	except:
		st.error("Insira algum valor de altura")

elif(status=='metros'):
	altura = st.number_input("Digite a altura em metros")

	try:
		imc= peso /(altura ** 2)
	except:
		st.error("Insira algum valor de altura")

if altura and peso:

		if(st.button('Calcular IMC')):
			st.text(f'Seu índice de IMC é {imc}')

			if (imc < 16):
				st.error('Extremamente abaixo do peso!')
			elif (imc >= 16 and imc <= 18.5):
				st.error('Abaixo do peso')
			elif (imc >= 18.5 and imc < 25):
				st.success('Você está no peso ideal!')
			elif (imc >= 25 and imc < 30):
				st.warning('Acima do peso!')
			elif (imc >= 30):
				st.warning('Extremamente acima do peso!')
