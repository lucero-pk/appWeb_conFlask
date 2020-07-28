This is a working example of a multi-container flask application with postgres, mongo and redis as the database fronted by the nginx reverse proxy.

## Usage

1. Bring up the cluster
```bash
$ docker-compose up -d
```
## Detener instancias de docker

2. En la teminal
```bash
$ ctrl + c
```
## Ver los registros de la Base de Datos

3. En la terminal 
```bash
$ sudo docker ps 
```

4. Copiar ID que diga mongo
```bash
$ sudo docker exec -it <ID> bash
```
5. Comporobar que nos encontramos dentro del contenedor
```bash
$ mongo --version
```

6. Ejecutar solo mongo
```bash
$ mongo
```
7. Listar las bases de datos
```bash
$ show dbs
```
8. Cambiar la base de datos (en este caso testdb)
```bash
$ use testdb
```
  
9. Mostrar las colecciones (tablas)
```bash
$ show collections
```
10. ver los regitros de users y posts
```bash
$ db.users.find()
$ db.posts.find()
```
## Limpiar Bases de Datos
```bash
$ db.post.drop()
```

11. Browse to localhost:8181 to see the app in action.
12. Browse to localhost:5151 to see the postgres manager.

13. Copiar url en el navegador para realizar un registro http://localhost:8181/signup
