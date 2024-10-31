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

## Kafka API Integration

Go into consume-kafka-stream.py and adapt your service id and credentials. Run using

```
python consume-kafka-stream.py
```

## REST API Integration

In order to test the REST API integration, search for an accounting point that you have collected data for already
that is stored in the Energy Data Vault.

Also, go into file get_rest_api_data_for_ap.py and adapt credentials. The example file will show you how to get 
authenticated and how to draw data. Please check further the OpenAPI Documentation for further details and updates of
functionality.

```
python get_rest_api_data_for_ap.py
```

Good luck!