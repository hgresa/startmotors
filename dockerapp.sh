#!/bin/bash

function containerRunning {
	docker ps | grep "$1" &> /dev/null
	if [ $? -eq 0 ];
	then
		return 0
	fi

	return 1
}

function imageExists {
  docker images | grep "$1" &> /dev/null
  if [ $? -eq 0 ];
  then
      return 0
  fi
  
  return 1
}

function runFlaskContainer {
	docker run --network=host --detach --publish 8088:8080 --volume "$(pwd)":/usr/src/app/ --name startmotors startmotors
}

function runMysqlContainer {
	docker run --rm --detach --publish 3307:3306 --volume /home/hgresa/storage/docker/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123 --name mysql8 mysql:8
}

if ! imageExists startmotors
then
  docker build -t startmotors .
fi

if ! containerRunning startmotors;
then
  runFlaskContainer
else
  read -rep $'startmotors is already running \n enter 1 for stopping it, 2 for rerunning: ' option
  echo "$option"
fi

if ! containerRunning mysql8;
then
  runMysqlContainer
else
  read -rep $'mysql8 is already running \n enter 1 for stopping it, 2 for rerunning: ' option
  echo "$option"
fi
