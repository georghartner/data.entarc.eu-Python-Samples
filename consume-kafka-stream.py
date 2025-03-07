from kafka import KafkaConsumer
import json

SASL_USERNAME="?"
SASL_PASSWORD="?"

# Available streams:
#SERVICEID_status-messages
#SERVICEID_validated-historical-data
#SERVICEID_raw-data-in-proprietary-format
#SERVICEID_aiida-data
#SERVICEID_realtime-consumption-info
#SERVICEID_realtime-consumption-val-info

consumer = KafkaConsumer(SASL_USERNAME + "_validated-historical-data",
                         value_deserializer= lambda m: json.loads(m.decode('utf-8')),
                         security_protocol="SASL_SSL",
                         ssl_check_hostname=True,
                         ssl_cafile="CARoot.pem",
                         sasl_mechanism="PLAIN",
                         sasl_plain_username=SASL_USERNAME,
                         sasl_plain_password=SASL_PASSWORD,
                         bootstrap_servers='data.entarc.eu:9097')
for msg in consumer:
    print(json.dumps(msg.value, indent=2))