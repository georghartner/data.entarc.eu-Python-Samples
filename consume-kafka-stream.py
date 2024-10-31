from kafka import KafkaConsumer
import json

SASL_USERNAME="?"
SASL_PASSWORD="?"

# Available streams:
# - SASL_USERNAME_permission-market-documents
# - SASL_USERNAME_validated-historical-data
# - SASL_USERNAME_raw-data-in-proprietary-format
# - SASL_USERNAME_aiida-data

consumer = KafkaConsumer(SASL_USERNAME + "_permission-market-documents",
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