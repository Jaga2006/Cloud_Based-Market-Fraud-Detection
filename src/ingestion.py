import os
from azure.eventhub import EventHubConsumerClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STR = os.getenv("AZURE_EVENTHUB_CONNECTION_STR")
EVENTHUB_NAME = os.getenv("AZURE_EVENTHUB_NAME")

def on_event(partition_context, event):
    # Print the event data (In production, this would go to a database or stream processor)
    print(f"Received event from partition: {partition_context.partition_id}")
    print(f"Data: {event.body_as_str()}")
    partition_context.update_checkpoint(event)

def start_ingestion():
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENTHUB_NAME
    )
    with client:
        client.receive(on_event=on_event, starting_position="-1")

if __name__ == "__main__":
    start_ingestion()
