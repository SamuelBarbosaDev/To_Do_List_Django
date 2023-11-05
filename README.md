# To-Do List

Este é um aplicativo de lista de tarefas simples desenvolvido usando o framework Django. Ele permite que os usuários criem, visualizem, atualizem e excluam tarefas de sua lista de afazeres. É um projeto ideal para aprender os conceitos básicos de desenvolvimento web com Django.

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

3. Inicie o servidor de desenvolvimento:

    ```shell
        python manage.py runserver
    ```

4.  Acesse o aplicativo em seu navegador em [http://localhost:8000/](http://localhost:8000/).

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

## Uso

- Adicione tarefas à sua lista de afazeres.
- Marque as tarefas como concluídas.
- Atualize ou exclua tarefas conforme necessário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, enviar solicitações de pull e melhorar o aplicativo.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

Desenvolvido por [Samuel](https://github.com/SamuelBarbosaDev)

