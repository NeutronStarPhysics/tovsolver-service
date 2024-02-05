.DEFAULT_GOAL := help


help:
	@echo 'Available commands:'
	@echo -e 'bootstrap \t\t - \t Runs flask on debug mode'

bootstrap: 
	APP_FOLDER=./src ./bootstrap.sh

docker-build:
	docker build -t service-configuration-api .

docker-run:
	docker run --name service-configuration-api  -d -p 5000:5000 service-configuration-api