## DB Setup


>docker pull postgres

>docker run -d -p 5430:5432 --name postgres-container -e POSTGRES_ROOT_PASSWORD=password -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword postgres

## Back-end Setup

#### move to folder back-end
>cd backend

#### install venv
>pip install virtualenv

#### import library
>pip install -r requirements.txt

#### run server
>python run.py
