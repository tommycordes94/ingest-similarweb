from service.request_mapping_total_traffic import RequestMapperTotalTraffic
from service.request_mapping_segment_analysis import RequestMapperSegmentAnalysis

def test_map_request_total_traffic():
    rq = RequestMapperTotalTraffic()
    domain_list = [
        {'url': 'abi.de', 'start_date': '2022-08', 'end_date': '2022-10',
            'endpoint': 'total_traffic.pages_per_visit'},
        {'url': 'tagesspiegel.de', 'start_date': '2022-08',
            'end_date': '2022-10', 'endpoint': 'total_traffic.pages_per_visit'},
        {'url': 'stern.de', 'start_date': '2022-08', 'end_date': '2022-10',
            'endpoint': 'total_traffic.pages_per_visit'},
        {'url': 'abi.unicum.de', 'start_date': '2022-02', 'end_date': '2022-10', 'endpoint': 'desktop.unique_visitors'}
    ]
    
    result = rq.map_request(domain_list=domain_list)

    """
    expected_result = {
        'total_traffic.pages_per_visit' : [
            {'url': 'abi.de', 'start_date': '2022-02', 'end_date': '2022-10'},
            {'url': 'tagesspiegel.de', 'start_date': '2022-06', 'end_date': '2022-10'},
            {'url': 'stern.de', 'start_date': '2022-08', 'end_date': '2022-10'}
        ],
        'desktop.unique_visitors':[
            {'url': 'abi.unicum.de', 'start_date': '2022-02', 'end_date': '2022-10'}
        ]
    }"""

    assert 'total_traffic.pages_per_visit' in result
    assert 'desktop.unique_visitors' in result
    assert len(result.get('total_traffic.pages_per_visit')) == 3
    assert len(result.get('desktop.unique_visitors')) == 1


def test_map_request_segment_analysis():
    rq = RequestMapperSegmentAnalysis()
    segment_list = [
        {'segment_id': 'a6fa00d0-cce4-46f8-b09c-7cc27569292e', 'start_date': '2022-08', 'end_date': '2022-10',
            'endpoint': 'segment_analysis.segment_traffic_and_engagement', 'metrics': 'visits, unique-visitors'},
        {'segment_id': '5c8a7398-35b3-47be-a5af-c2767cc086c4', 'start_date': '2022-08',
            'end_date': '2022-10', 'endpoint': 'segment_analysis.segment_traffic_and_engagement', 'metrics': 'visits, unique-visitors'},
        {'segment_id': '41230ad0-c198-45d3-99d2-a9fe567185cd', 'start_date': '2022-08', 'end_date': '2022-10',
            'endpoint': 'segment_analysis.segment_marketing_channels', 'metrics': 'visits, unique-visitors'},
        {'segment_id': '3be39240-7b6c-4bb3-8155-ab86e497b5e3', 'start_date': '2022-02', 'end_date': '2022-10', 
            'endpoint': 'segment_analysis.segment_traffic_and_engagement', 'metrics': 'visits, unique-visitors'}
    ]
    
    result = rq.map_request(segment_list=segment_list)
    print(result)

    assert 'segment_analysis.segment_traffic_and_engagement' in result
    assert 'segment_analysis.segment_marketing_channels' in result
    assert len(result.get('segment_analysis.segment_traffic_and_engagement')) == 3
    assert len(result.get('segment_analysis.segment_marketing_channels')) == 1