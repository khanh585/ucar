docker setup
install postgresql

docker pull postgres
docker run -d -p 5432:5432 --name postgres-container -e POSTGRES_PASSWORD=mypassword -e POSTGRES_USER=dev postgres

docker run -p 5432:5432 --name psql -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=myuser -d 

docker run -d -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_USER=myuser -e MYSQL_PASSWORD=mypassword mysql

docker run -d -p 5430:5432 --name postgres-container -e POSTGRES_ROOT_PASSWORD=password -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword postgres
