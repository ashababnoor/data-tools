from google.cloud import bigquery
from helper import Table

class Bigquery:
    def __init__(self, google_cred):
        self._client = Bigquery._get_connection(google_cred)

    def execute(self, query):
        for row in self._client.query(query):
            yield row

    @staticmethod
    def _get_connection(cred):
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
        
        schema_fields_json = []
        for field in table_object.schema:
            schema_field_dict = {
                "name": field.name,
                "type": field.field_type,
                "mode": field.mode,
                "description": field.description,
                # Add other attributes as needed
            }
            schema_fields_json.append(schema_field_dict)

        return schema_fields_json