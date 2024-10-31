# data.entarc.eu Python integration

These are the Python implemented pattern programs to link with data.entarc.eu.

Please note that you have to contact entarc.eu to get an account. Then, create a service
and let us know the service id. We will then create a Kafka authentication for you.

Please create your DataNeeds then and mark "Send to Kafka" if you want to consume the Kafka interface.

Hit "Energy data vault" switch if you would like to have your data available online and accessible via the REST API, 
including dataservices.

Then, install python (Python 3 is a requirement) kafka libraries using 
```
pip install -r requirements.txt
```

Go into consume-kafka-stream.py and adapt your service id and credentials. Run using

```
python consume-kafka-stream.py
```

Good luck!