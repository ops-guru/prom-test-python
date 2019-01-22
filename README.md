# blue-prom-test-python
Demo code in python to show prometheus statistics

# Build python container

```
docker build -t demo-python -f Docker-python ./
docker run -it --rm --name demo-python -p 8001:8001 demo-python
```

# Install consul service

```
cp demo-go.json /opt/consul/config/
```
