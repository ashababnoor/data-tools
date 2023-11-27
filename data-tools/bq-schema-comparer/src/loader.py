from google.cloud import bigquery
from helper import Table, Schema


class Bigquery:
    def __init__(self, google_cred: str):
        self._client = Bigquery._get_connection(google_cred)

    def execute(self, query: str):
        for row in self._client.query(query):
            yield row

    @staticmethod
    def _get_connection(cred: str) -> bigquery.Client:
        if cred is not None:
            import os

            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred
        return bigquery.Client()
    
    def get_client(self):
        return self._client
    
    def get_schema(self, table: Table):
        # Get the table reference
        table_reference = self._client.dataset(
            dataset_id=table.dataset_id, 
            project=table.project_id
        ).table(table_id=table.table_id)
        
        # Get the table object
        table_object = self._client.get_table(table_reference)
        
        return Schema(
            project_id=table.project_id,
            dataset_id=table.dataset_id,
            table_id=table.table_id,
            schema=table_object.schema
        )