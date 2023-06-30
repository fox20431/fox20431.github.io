---
title: kafka tutorial
---

# Kafka Tutorial

> Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

## Preface

The tutorial references the following:

- [Kafka Offical Documentation](https://kafka.apache.org/documentation)

## Get Started

1. Get the package.

   Download the archive:

   ```shell
   # specified the version
   KAFKA_VERSION=3.5.0
   # specified the scala version
   SCALA_VERSION=2.13
   wget wget https://downloads.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
   ```

   Extract the package:

    ```shell
    tar -xzf kafka_2.13-3.5.0.tgz
    cd kafka_2.13-3.5.0
    ```

2. Start the Kafka environment.

   **Kafka with Zookeeper**

   ```shell
   # Start the Zookeeper service
   bin/zookeeper-server-start.sh config/zookeeper.properties
   # Start the Kafka broker service
   bin/kafka-server-start.sh config/server.properties
   ```

   **Kafka with Kraft**

   ```shell
   # Generate a Cluster UUID
   KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
   # Format Log Directories
   bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
   # Start the Kafka Server
   bin/kafka-server-start.sh config/kraft/server.properties
   ```

3. Create a topic to store your events.

   Before you can write your first events, you must create a topic.

   ```shell
   # Create a topic named quickstart-events
   bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
   ```

   Check the topic description:

   ```shell
   bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
   # Output
   Topic: quickstart-events        TopicId: 6cU0Jo5iTLmp7c1bTnBBdg PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
           Topic: quickstart-events        Partition: 0    Leader: 1       Replicas: 1     Isr: 1
   ```

4. Write some events into the topic.

   ```shell
   bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
   This is my first event
   This is my second event
   ```

5. Read the events

   ```shell
   bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
   This is my first event
   This is my second event
   ```

6. Import/export your data as streams of events with kafka connect.

   In this quickstart, we'll see how to run Kafka Connect with simple connectors that **import data from a file** to a Kafka topic and **export data from a Kafka topic to a file**.

   First, make sure to add `connect-file-3.5.0.jar` to the `plugin.path` property in the connect worker's configuration.

   ```shell
   echo "plugin.path=libs/connect-file-3.5.0.jar" >> config/connect-standalone.properties
   ```

   Start by creating some seed data to test with:

   ```shell
   echo -e "foo\nbar" > test.txt
   ```

   Next, we'll start two connectors running in *standalone* mode, We provide three configuration files as parameters. The first is always the configuration for the Kafka Connect process, containing common configuration such as the Kafka brokers to connect to and the serialization format for data. The remaining configuration files each specify a connector to create. These files include a unique connector name, the connector class to instantiate, and any other configuration required by the connector.

   ```shell
   bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
   ```

   We can verify the data has been delivered through the entire pipeline by examining the contents of the output file:

   ```shell
   more test.sink.txt
   ```

   Note that the data is being stored in the Kafka topic `connect-test`, so we can also run a console consumer to see the data in the topic(or use the custom consumer code to process it):

   ```shell
   bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic connect-test --from-beginning
   
   # Output
   {"schema":{"type":"string","optional":false},"payload":"foo"}
   {"schema":{"type":"string","optional":false},"payload":"bar"}
   ...
   ```

   The connectors continue to process data, so we can add data to the file and see it move through the pipeline:

   ```shell
   echo Another line >> test.txt
   ```

   You should see the line appear in the console consumer output and in the sink file.

7. Process your events with Kafka Streams

   Due to the code being too long, please check [the code](https://github.com/fox20431/java-ext-cookbook/tree/master/kafka).

   **THERE BE DRAGON:**

   The application on Windows can't connect Kafka that runs on WSL; the root cause seems to be that WSL2 is broken with regards to IPv6 and localhost.

   Solve the question:

   ```shell
   sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
   sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
   ```

   Please see [the StackOverflow posts](https://stackoverflow.com/questions/64177422/unable-to-produce-to-kafka-topic-that-is-running-on-wsl-2-from-windows) for more details.

8. Terminate the Kafka environment.

   `Ctrl-C`

   If you also want to delete any data of your local Kafka environment, including any events you have created along the way, run the command:

   ```sh
   rm -rf /tmp/kafka-logs /tmp/zookeeper /tmp/kraft-combined-logs
   ```

   

   

