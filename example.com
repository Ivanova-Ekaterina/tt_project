server {
	listen 80;
	location /API/ {
		proxy_pass http://127.0.0.1:8000;
	}
	location / {
		root /home/ekaterina/tt_project/public;
	}
}
