from multiprocessing.context import assert_spawning
import pytest
from service.apiclient.api_client import SimilarWebApiClient



####### general tests #######

def test_build_endpoint():
    sc = SimilarWebApiClient()
    api_url = sc.build_endpoint_url(folder='website',domain="spiegel.de",endpoint="total-traffic-and-engagement",metric="visits")
    assert api_url == "https://api.similarweb.com/v1/website/spiegel.de/total-traffic-and-engagement/visits"

def test_build_endpoint_2():
    sc = SimilarWebApiClient()
    api_url = sc.build_endpoint_url(folder='segment',endpoint="traffic-and-engagement",metric="query", segment_id='04075af1-fae9-4f04-9691-e120758ee102')
    assert api_url == "https://api.similarweb.com/v1/segment/04075af1-fae9-4f04-9691-e120758ee102/traffic-and-engagement/query"


def test_build_endpoint_3():
    sc = SimilarWebApiClient()
    api_url =  sc.build_endpoint_url(folder='segment_list',endpoint="traffic-and-engagement",metric="describe")
    assert api_url == "https://api.similarweb.com/v1/segment/traffic-and-engagement/describe"

def test_call_endpoint(): #### TEST WILL FAIL DUE TO MISSING APY_KEY
    sc = SimilarWebApiClient()
    
    api_url = sc.build_endpoint_url(
            folder = 'website',
            endpoint="total-traffic-and-engagement",
            domain = 'spiegel.de',
            metric='visits')
    PARAMS = {
            'api_key':'', # Enter Key for testing purpose
            'start_date':'2022-01', 
            'end_date':'2022-04', 
            'country':'de', 
            'granularity':'monthly', 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }
    response = sc.call_endpoint(api_url, PARAMS)
    assert 'visits' in response 
    assert 'meta' in response 
    assert response.get('visits')[0].get('visits') == pytest.approx(89006932, abs = 1)




######## website tests ##########
# Assert response values are deactivated due to necessary change of dates every month and therefore changing values

def test_api_client_1():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_visits(domain="spiegel.de",start_date="2023-01",end_date="2023-03",granularity='monthly')
    assert 'visits' in response 
    assert 'meta' in response 
    #assert response.get('visits')[0].get('visits') == pytest.approx(89006932, abs = 1)
        
def test_api_client_2():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_pages_per_visit(domain="spiegel.de",start_date="2022-10",end_date="2022-11",granularity='monthly')
    assert 'pages_per_visit' in response 
    assert 'meta' in response 
    #assert response.get('pages_per_visit')[0].get('pages_per_visit') == pytest.approx(2, abs = 1)

def test_api_client_3():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_average_visit_duration(domain="spiegel.de",start_date="2022-10",end_date="2022-11",granularity='monthly')
    assert 'average_visit_duration' in response 
    assert 'meta' in response 
    #assert response.get('average_visit_duration')[0].get('average_visit_duration') == pytest.approx(229, abs = 1)

def test_api_client_4():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_bounce_rate(domain="spiegel.de",start_date="2022-10",end_date="2022-11",granularity='monthly')
    assert 'bounce_rate' in response 
    assert 'meta' in response 
    #assert response.get('bounce_rate')[0].get('bounce_rate') == pytest.approx(0.5, abs = 1)

def test_api_client_5():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_pages_views(domain="spiegel.de",start_date="2022-10",end_date="2022-11",granularity='monthly')
    assert 'pages_views' in response 
    assert 'meta' in response 
    #assert response.get('pages_views')[0].get('pages_views') == pytest.approx(207887306, abs = 1)

def test_api_client_6():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_desktop_vs_mobile_split(domain="spiegel.de",start_date="2022-10",end_date="2022-11")
    assert 'mobile_web_visit_share' in response 
    assert 'meta' in response 
    #assert response.get('desktop_visit_share') == pytest.approx(0.4, abs = 1)

def test_api_client_7():
    sc = SimilarWebApiClient()
    response = sc.get_total_traffic_deduplicated_audience(domain="spiegel.de",start_date="2022-10",end_date="2022-11")
    assert 'data' in response 
    assert 'meta' in response 
    #assert response.get('data')[0].get('dedup_data').get('desktop_only_audience_share') == pytest.approx(0.2, abs = 1)



######## segment tests #########

def test_api_client_9():
    sc = SimilarWebApiClient()
    response = sc.get_segment_analysis_segment_traffic_and_engagement(start_date="2022-01",end_date="2022-04",granularity='daily', segment_id = "04075af1-fae9-4f04-9691-e120758ee102", metrics ='visits,share,pages-per-visit,page-views,bounce-rate,visit-duration')
    assert 'visits' in response["segments"][0] 
    assert 'meta' in response 
    assert response.get('segments')[0].get('visits') == pytest.approx(1094, abs = 1)
    assert response.get('segments')[0].get('page_views') == pytest.approx(13129, abs = 1)

'''def test_api_client_10():
    sc = SimilarWebApiClient()
    response = sc.get_segment_analysis_segment_marketing_channels(start_date="2022-01",end_date="2022-04",granularity='monthly', segment_id = "04075af1-fae9-4f04-9691-e120758ee102", metrics ='visits,pages-per-visit,page-views,bounce-rate,visit-duration')
    print(response)
    assert 'bounce_rate' in response["segments"][0]['metrics'][0]
    assert 'meta' in response 
    assert response.get('segments')[0].get('metrics')[0].get('bounce_rate') == pytest.approx(0.4, abs = 1)
    assert response.get('segments')[0].get('metrics')[0].get('visit_duration') == pytest.approx(446, abs = 1) '''