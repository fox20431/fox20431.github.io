## Docker Compose

Docker Compose 有个很好的特性是可以创建默认网络（`<projectname_default>`），可以通过服务名称来指定对应服务的网络地址。

### Common

```yaml
version: "3"

services:
  kafka-0:
    container_name: kafka-0
    image: docker.io/bitnami/kafka:3.3
    ports:
      - "9092:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_BROKER_ID=0
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
      - ALLOW_PLAINTEXT_LISTENER=yes
    volumes:
      - kafka_0_data:/bitnami/kafka

  kafka-1:
    container_name: kafka-1
    image: docker.io/bitnami/kafka:3.3
    ports:
      - "9192:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_CFG_BROKER_ID=1
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
    volumes:
      - kafka_1_data:/bitnami/kafka

  kafka-2:
    container_name: kafka-2
    image: docker.io/bitnami/kafka:3.3
    ports:
      - "9292:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_CFG_BROKER_ID=2
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
    volumes:
      - kafka_2_data:/bitnami/kafka

volumes:
  kafka_0_data:
    driver: local
  kafka_1_data:
    driver: local
  kafka_2_data:
    driver: local
```

### With Nginx

如果想将每个服务独立的网段设置在同一网络上，可以使用 Nginx 进行网络代理。

```diff
version: "3"

services:
  kafka-0:
    container_name: kafka-0
    image: docker.io/bitnami/kafka:3.3
-    ports:
-      - "9092:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_BROKER_ID=0
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
      - ALLOW_PLAINTEXT_LISTENER=yes
    volumes:
      - kafka_0_data:/bitnami/kafka

  kafka-1:
    container_name: kafka-1
    image: docker.io/bitnami/kafka:3.3
-    ports:
-      - "9192:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_CFG_BROKER_ID=1
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
    volumes:
      - kafka_1_data:/bitnami/kafka

  kafka-2:
    container_name: kafka-2
    image: docker.io/bitnami/kafka:3.3
-    ports:
-      - "9292:9092"
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_CFG_BROKER_ID=2
      - KAFKA_KRAFT_CLUSTER_ID=LelM2dIFQkiUFvXCEcqRWA
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
    volumes:
      - kafka_2_data:/bitnami/kafka
+  nginx:
+    container_name: nginx
+    hostname: nginx
+    image: nginx:1.23.3
+    volumes:
+      - ./nginx.conf:/etc/nginx/nginx.conf:ro
+    ports:
+      - "9093:9093"
+      - "9193:9193"
+      - "9293:9293"
+    depends_on:
+      - kafka-0
+      - kafka-1
+      - kafka-2

volumes:
  kafka_0_data:
    driver: local
  kafka_1_data:
    driver: local
  kafka_2_data:
    driver: local
```

在当前目录下创建`nginx.conf`，并写入如下：

```conf
user                nginx;
worker_processes    auto;
error_log           /var/log/nginx/error.log notice;
pid                 /var/run/nginx.pid;

events {
    worker_connections    1024;
}

stream {
    upstream kafka-0 {
        server kafka-0:9092;
    }
    upstream kafka-1 {
        server kafka-1:9092;
    }
    upstream kafka-2 {
        server kafka-2:9092;
    }

    server {
        listen      9092;
        proxy_pass  kafka-0;
    }
    server {
        listen      9192;
        proxy_pass  kafka-1;
    }
    server {
        listen      9292;
        proxy_pass  kafka-2;
    }
}

http {
    include         /etc/nginx/mime.types;
    default_type    application/octet-stream;

    log_format      main    '$remote_addr - $remote_user [$time_local]  $status '
                            '"$request" $body_bytes_sent "$http_referer" '
                            '"$http_user_agent" "$http_x_forwarded_for"';

    access_log   /var/log/nginx/access.log  main;

    sendfile     on;

    keepalive_timeout   60;

    include         /etc/nginx/conf.d/*.conf;
}
```

## Command

创建主题（三个分区、两个副本）

```sh
docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create --bootstrap-server kafka-0:9092 \
    --topic my-topic \
    --partitions 3 --replication-factor 2
```

创建生产者

```sh
docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-console-producer.sh \
    --bootstrap-server kafka-0:9092 \
    --topic my-topic
```

创建消费者

```sh
docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka-0:9092 \
    --topic my-topic
```