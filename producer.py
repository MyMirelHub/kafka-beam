import apache_beam as beam
from apache_beam.io.external.kafka import WriteToKafka
import typing, json

brokers = 'localhost:9092'
kafka_topic = 'topic1'

def run_pipeline():
  with beam.Pipeline() as p:
    (p
     | beam.Create([{'a' : 'hello'}, {'b' : 'world'}])
     | 'Convert dict to byte string' >> beam.Map(lambda x: (b'', json.dumps(x).encode('utf-8')))
     | beam.Map(lambda x : x).with_output_types(typing.Tuple[bytes, bytes])
#     | beam.Map(print)
     | WriteToKafka(producer_config = {'bootstrap.servers': brokers}
                            , topic=kafka_topic)
    )

if __name__ == '__main__':
  run_pipeline()
    