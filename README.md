# todo-list usando Vue + Vuetify, FastAPI + uvicorn e SQLAlchemy

## Como executar o projeto

Montar as imagens usando docker

```sh
$ docker-compose up -d --build
```

Após montar as imagens executar o seguinte comando para montar o banco

```sh
$ docker compose exec backend python src/init_db.py
```

Por padrão a aplicação está rodando no http://localhost:8080