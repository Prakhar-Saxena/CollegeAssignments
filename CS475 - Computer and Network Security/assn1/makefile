main:
	make clean generate

test:
	python3 test.py

clean:
	truncate -s 0 user_passwords
	truncate -s 0 server_password

generate:
	python3 generate.py

server:
	python3 server.py

client:
	python3 client.py tux3 3141

cgs:
	make clean generate server
