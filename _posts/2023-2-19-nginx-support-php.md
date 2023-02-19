安装nginx、php、php-mysql、php-fpm
启用nginx、php-fpm服务

配置文件/etc/nginx/sites-available/www.hihusky.com

server {

	listen 443 ssl http2 default_server;
	listen [::]:443 ssl http2 default_server;

	server_name www.hihusky.com;

	ssl on;
	ssl_certificate /etc/nginx/cert/www.hihusky.com.pem;
	ssl_certificate_key /etc/nginx/cert/www.hihusky.com.key;
	ssl_session_cache shared:SSL:1m;
	ssl_session_timeout 4h;
	# Encryption algorithm
	ssl_ciphers EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH;

	ssl_stapling on;
	ssl_stapling_verify on;
	ssl_trusted_certificate /etc/nginx/cert/www.hihusky.com.pem;

	root /var/www/wordpress/;
	index index.php;

    # 这个是关键，具体参数我也不清楚具体含义
	location ~ \.php {
		fastcgi_pass   unix:/run/php/php7.4-fpm.sock;
		fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include        fastcgi_params;
	}

	location /ray {
		proxy_redirect off;
        proxy_intercept_errors on;
        proxy_pass http://127.0.0.1:20808;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;
	}
}