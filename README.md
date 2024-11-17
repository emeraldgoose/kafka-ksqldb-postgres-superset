# kafka-ksqldb-postgres-superset

## Diagram
<img width="1365" alt="19" src="https://github.com/user-attachments/assets/8f4dacc6-dd6b-449a-8bd0-1c2b1c755c64">

## Postgres Deployment
```
kubectl create ns postgres
kubectl apply -f postgresql/ -n postgres
```
## Kafka Deployment
```
kubectl create ns kafka
kubectl apply -f kafka/ -n kafka
```
## Superset Deployment
```
kubectl create ns superset
helm repo add superset http://apache.github.io/superset/
helm repo update
```
### SUPERSET_SECRET_KEY
```
openssl rand -base64 42
```
```
# superset/values.yaml
extraSecretEnv:
    SUPERSET_SECRET_KEY: write here
```
```
helm install superset superset/superset -n superset -f superset/values.yaml
```
or
```
helm install superset superset/superset -n superset --set envSecretEnv.SUPERSET_SECRET_KEY=$(openssl rand -base64 42)
```
## Post
- [https://emeraldgoose.github.io/data-engineer/kafka-pipeline/](https://emeraldgoose.github.io/data-engineer/kafka-pipeline/)
