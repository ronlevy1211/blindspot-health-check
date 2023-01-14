# BlindSpot Home Assignment

Welcome to BlindSpot Home Assignment

![](./diagram.png)

## Prerequisites
- python
- GitHub personal access token

## SetUp

### Configure access token 

To run the healthy service you will need first to add your personal access token to the healthy config.ini file.

Go to `healthy/config.ini` and add your token under 'GitHub' section and token key.

### Run unit tests  

To run unit test for HealthCheck run the following command

```bash
cd healthy && python -m unittest tests/HealthCheck/TestHealthCheck.py 
```

### Run the microservices

To start the healthy service run the following commands

```bash
cd healthy && python main.py 
```

To start the resty service run the following commands

```bash
cd resty && python main.py 
```


## Usage

Add the resy.com DNS name to hosts file

```bash
echo "127.0.0.1     resty.com" >> /etc/hosts 
```

Example usage

```bash
curl http://resty.com:5000/check_security  -H 'Content-Type: application/json' -d '{"packages":["package", "npm", "express", "nx", "lodash", "cloudinary", "axios", "karma", "molecular", "grunt"]}'
```