# Como rodar o projeto?

- Primeiro instale as dependencias do backend do projeto:

```
pip install -r requirements.txt
```
- Entre na pasta frontend:

```
cd frontend
```
- Instale as dependencias do frontend:
```
npm install
```
- Retorne à raiz do projeto:
```
cd ..
```
- Rode a API de acesso ao bot:
```
python services/api.py
```
- Rode a aplicação frontend:
```
node frontend/index.js
```

### Agora é só interagir com o bot 😁

# Observação:

### Este projeto utiliza algumas libs que podem entrar em conflito com novas versões do python, então caso esteja utilizando Python 3.9 ou versão acima e encontre algum erro, aqui está uma solução:

- Caso ocorra algum erro ao rodar a API ou o BOT, atualize o sqlalchemy para uma versão compativel:

```
pip install sqlalchemy==1.3.24
```

### Após a correção é só rodar e ser feliz 😁
