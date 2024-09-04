FROM confluentinc/cp-kafka-connect-base:latest

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.11 && \
    confluent-hub install --no-prompt debezium/debezium-connector-postgresql:2.5.4
