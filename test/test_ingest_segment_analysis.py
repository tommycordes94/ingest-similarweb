import pathlib
from service.ingest_segment_analysis import SegmentAnalysisIngester


def test_ingest__ingest_segment_traffic_and_engagements():
    tti = SegmentAnalysisIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    tti._SegmentAnalysisIngester__ingest_segment_traffic_and_engagement(
        segment={
            'segment_id': '16453587-4b0e-474c-ad02-44ec0d5f7f94',
            'metrics': 'visits',
            'granularity': 'monthly',
            'start_date': '2022-01',
            'end_date': '2022-07'})


def test_call_endpoint():
    tti = SegmentAnalysisIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})
    tti.call_endpoint(
        endpoint="segment_analysis.segment_traffic_and_engagement",
        segment_list=[{'segment_id': '5c8a7398-35b3-47be-a5af-c2767cc086c4',
                      'start_date': '2022-01',
                      'end_date': '2022-07',
                      'metrics': 'visits,unique-visitors'},
                     {'segment_id': '7e094d2e-0989-46d4-b512-d745ac69036a',
                      'start_date': '2022-01',
                      'end_date': '2022-07',
                      'metrics': 'visits,unique-visitors'}])


def test_call_endpoints():
    tti = SegmentAnalysisIngester(config={
        'base_path': str(pathlib.Path(__file__).parent)},
        endpoint_params={})

    tti.call_endpoints(endpoints={'segment_analysis.segment_traffic_and_engagement': [{'segment_id': 'a6fa00d0-cce4-46f8-b09c-7cc27569292e', 'metrics': 'visits, unique-visitors'}, {'segment_id': '5c8a7398-35b3-47be-a5af-c2767cc086c4', 'metrics': 'visits, unique-visitors'}, {'segment_id': '3be39240-7b6c-4bb3-8155-ab86e497b5e3', 'metrics': 'visits, unique-visitors'}], 'segment_analysis.segment_marketing_channels': [{'segment_id': '41230ad0-c198-45d3-99d2-a9fe567185cd', 'metrics': 'visits, unique-visitors'}]})

def test_ingest_segment_list():
    tti = SegmentAnalysisIngester(config={
    'base_path': str(pathlib.Path(__file__).parent)},
    endpoint_params={})
    
    tti.ingest_segment_list()
