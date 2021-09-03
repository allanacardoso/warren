# Instructions

## Setup
You can simply use the envrionment variables from your local system
```
export MYSQL_ROOT_HOST=<HOST>
export MYSQL_DATABASE=<DATABASE>
export MYSQL_PASSWORD=<PASSWORD>
export MYSQL_USER=<USER>
```
---

Or even create an .env file to acomplishment it filling with the required fields
```
touch .env
```
```
echo $'MYSQL_ROOT_HOST=<HOST>\nMYSQL_DATABASE=<DATABASE>\nMYSQL_PASSWORD=<PASSWORD>\nMYSQL_USER=<USER>' > .env 
```

**Environment variables**

The ```<HOST>, <DATABASE>, <PASSWORD>, <USER>``` are valid values provided.

---

## Using Docker and Docker-composer

### Starting the db service
```
docker-composer up -d db
```

### Listing all service containers
```
docker ps -a
```

### Going into the container
```
docker exec -it $(docker ps -aqn 1) /bin/bash
```

---
**Instructions**

It goes through the last container id and run docker exec over it point to start the bash as a entrypoint

---

## Acessing MySql database
```
mysql -h $MYSQL_ROOT_HOST -P 3306 -u $MYSQL_USER -p
```

docker commit 4cfe13485fa4 allana/warren:0.1
