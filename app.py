import streamlit as st
import streamlit_authenticator as stauth

# Lista de usuários e senhas
names = ['Usuário1']
usernames = ['usuario1']
passwords = ['senha123']

# Criptografa as senhas
hashed_passwords = stauth.Hasher(passwords).generate()

# Cria o autenticador
authenticator = stauth.Authenticate(
    names, usernames, hashed_passwords,
    'meu_app', 'abcdef', cookie_expiry_days=30
)

# Tela de login
name, authentication_status, username = authenticator.login('Login', 'main')

# Conteúdo do app
if authentication_status:
    st.title(f'Bem-vindo, {name}!')
    st.write('Este é seu painel privado.')
elif authentication_status == False:
    st.error('Usuário ou senha incorretos')
else:
    st.warning('Por favor, insira suas credenciais')

