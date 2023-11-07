# To-Do List

Este é um aplicativo de lista de tarefas simples desenvolvido usando o framework Django. Ele permite que os usuários criem, visualizem, atualizem e excluam tarefas de sua lista de afazeres. É um projeto ideal para aprender os conceitos básicos de desenvolvimento web com Django.

### Índice:
- [To-Do List](#to-do-list)
    - [Índice:](#índice)
  - [Uso](#uso)
  - [Requisitos](#requisitos)
  - [Instalação](#instalação)
  - [Configurando banco de dados](#configurando-banco-de-dados)
  - [Configurando Variáveis De Ambiente](#configurando-variáveis-de-ambiente)
  - [Execute o Projeto:](#execute-o-projeto)
  - [Rotas da API](#rotas-da-api)
    - [Cria uma nova tarefas:](#cria-uma-nova-tarefas)
    - [Deleta uma tarefas:](#deleta-uma-tarefas)
    - [Listar as tarefas do usuário:](#listar-as-tarefas-do-usuário)
    - [Altera parcialmente uma tarefa:](#altera-parcialmente-uma-tarefa)
    - [Altera totalmente uma tarefa:](#altera-totalmente-uma-tarefa)
  - [Contribuição](#contribuição)
  - [Licença](#licença)

## Uso

- Adicione tarefas à sua lista de afazeres.
- Marque as tarefas como concluídas.
- Atualize ou exclua tarefas conforme necessário.

## Requisitos

Certifique-se de ter as seguintes ferramentas instaladas antes de executar o aplicativo:

- Python 3.10
- Django 4.2
- Um ambiente virtual (recomendado)

## Instalação

1. Clone o repositório para o seu ambiente local:
    ```shell
        git clone https://github.com/SamuelBarbosaDev/To_Do_List_Django.git
    ```
2. Navegue até o diretório do projeto:
   ```shell
        cd To_Do_List_Django
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```shell
        python -m venv venv
    ```

4. Ative o ambiente virtual:

- No Windows:

    ```shell
        venv\Scripts\activate
    ```

- No macOS e Linux:

    ```shell
        source venv/bin/activate
    ```

5. Instale as dependências do projeto:

    ```shell
        pip install -r requirements.txt
    ```

## Configurando banco de dados
1. Crie o volume:

   ```shell
    docker run \
    --name to_do_list_django \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=to_do_list \
    -d \
    -p 5434:5432 \
    -v postgres-data:/var/lib/postgresql/data \
    postgres:latest
   ```

2. Execute as migrações do banco de dados:

    ```shell
        python manage.py migrate
    ```

## Configurando Variáveis De Ambiente

1. Crie o arquivo `.env`:
    ```shell
        touch .env
    ```
2. Adicione ao arquivo `.env` as variáveis de ambiente:
    ```shell
        SECRET_KEY=CHANGE-ME

        # 0 False, 1 True
        DEBUG=1

        # Comma separated values
        ALLOWED_HOSTS="127.0.0.1, localhost"

        DB_ENGINE=django.db.backends.postgresql
        POSTGRES_DB=CHANGE-ME
        POSTGRES_USER=CHANGE-ME
        POSTGRES_PASSWORD=CHANGE-ME
        POSTGRES_HOST=localhost
        POSTGRES_PORT=5432
    ```

3. Entre no python shell:
    ```shell
        python3
    ```

4. Gere a `SECRET_KEY`:
    ```shell
        from django.core.management.utils import get_random_secret_key

        print(get_random_secret_key())
    ```


## Execute o Projeto:
1. Inicie o servidor de desenvolvimento:

    ```shell
        python manage.py runserver
    ```

2.  Acesse o aplicativo em seu navegador em [http://localhost:8000/](http://localhost:8000/).

## Rotas da API
A seguir estão listadas as rotas da API com os métodos HTTP correspondentes e os parâmetros necessários, quando aplicável.

### Cria uma nova tarefas:
- **Método**: POST
- **Rota**: 
```url
  /api/tarefas/?username=name
```
- **Descrição**: Cria uma nova tarefa para o usuário com o nome de usuário especificado.

### Deleta uma tarefas:
- **Método**: DELETE
- **Rota**: 
```url
  /api/tarefas/pk/?username=name
```
- **Descrição**: Deleta uma tarefa específico com base no ID (pk) especificado para o usuário com o nome de usuário especificado.

### Listar as tarefas do usuário:

- **Método**: GET
- **Rota**: 
```url
  /api/tarefas/?username=name
```
- **Descrição**: Retorna a lista de tarefas do usuário com o nome de usuário especificado.

### Altera parcialmente uma tarefa:

- **Método**: PATCH
- **Rota**:
```url
  /api/tarefas/pk/?username=name
```
- **Descrição**: Realiza uma modificação parcial em uma tarefa com base no ID (pk) da tarefa e no nome do usuário.

### Altera totalmente uma tarefa:

- **Método**: PUT
- **Rota**:
```url
  /api/tarefas/pk/?username=name
```
- **Descrição**: Realiza uma modificação completa em uma tarefa com base no ID (pk) da tarefa e no nome do usuário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, enviar solicitações de pull e melhorar o aplicativo.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

Desenvolvido por [Samuel](https://github.com/SamuelBarbosaDev)

