import pathlib
from service.ingest_total_traffic import TotalTrafficIngester, SuperIngester
from datetime import datetime

def test_ingest_total_traffic_visits():
    tti = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    tti._TotalTrafficIngester__ingest_total_traffic_visits(
        domain={
            'url': 'bmw.de',
            'start_date': '2022-01',
            'end_date': '2022-07'})

def test_ingest_page_views():
    tti = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    tti._TotalTrafficIngester__ingest_total_traffic_page_views(
        domain={
            'url': 'bmw.de',
            'start_date': '2022-08',
            'end_date': '2022-10'})
       
def test_call_endpoint():
    tti = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    tti.call_endpoint(
        endpoint="total_traffic.deduplicated_audience",
        domain_list=[{'url': 'bmw.de'},
                     {'url': 'porsche.de'}])

def test_call_endpoints():
    tti = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})

    tti.call_endpoints(endpoints={
            'total_traffic.pages_per_visit': [
                {'url': 'abi.de'}, 
                {'url': 'tagesspiegel.de'}, 
                {'url': 'stern.de'}], 
            'desktop.unique_visitors': [
                {'url': 'abi.unicum.de'}]})

def test_store_errorlog():
    tti = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    
    tti.append_to_errorlog({'gdtgedtgedt':'123'})

    tti.store_error_log("testb")

    tti2 = TotalTrafficIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    
    tti2.append_to_errorlog({'gduheudhuehdt':'23'})
    tti2.append_to_errorlog({'gadeuduehduuuuuuu':'3'})

    tti2.store_error_log("testa")