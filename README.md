# API Que Executa Um Robô de Coleta de Dados

## Rodando a aplicação

### Instalando Ambiente Virtual

```
python3 -m venv venv
```

### Ativando Ambiente Virtual

```
source venv/bin/activate
```

### Instalando dependências
```
pip install -r requirements.txt
```

### Rodando aplicacação

```
python app.py
```

## Rota que Executa Robô

Localmente:
```
localhost:5000/scraper/notebooks/
```


### OBS:
Caso ocorra algum erro na chamada da rota '/scraper/notebooks/', confira se ja executou o comando:
```
playwright install
```

## Estrutura 
app.py -> Ponto de partida da aplicacação

/scraper -> Módulo que contém os algoritmos dos robõs\
/routes  -> Módulo que contém as rotas da API\
/models  -> Módulo para modelos do banco de dados\
/config  -> Módulo para configuração da aplicação