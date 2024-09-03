# ingest-similarweb
Ingestion of similar web data provided by their APO

# local


curl --location --request GET 'http://127.0.0.1:8080?domain=spiegel.de&ingest_type=segments&tart_date=2021-05&end_date=2022-07&granularity=monthly&metrics=visits‘ 



# pytest beispiele

## Alle Tests

python -m pytest test/test_api_client.py

## Einzelner Test

python -m pytest test/test_api_client.py::test_build_endpoint

## Mit Ausgabe

python -m pytest test/test_api_client.py::test_build_endpoint -s