import requests 
import os
import json
import logging
import traceback

class SimilarWebApiClient():
    
    def __init__(self):
        self.api_key = os.environ.get('SIMILARWEB_API_KEY')
        if self.api_key is None:
            raise ValueError("no api key specified - please export SIMILARWEB_API_KEY")
        
    API_URL = "https://api.similarweb.com/v1"

    def call_endpoint(
        self,
        api_url,
        PARAMS):
        r = requests.get(api_url,PARAMS)
        try:
            return r.json()
        except Exception as e:
            error = f"ERROR OCCURED: {e}"
            logging.error(error)
            logging.error(traceback.format_exc())
            return None  # or any default value you want to return
    
    
    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        return text

    def build_endpoint_url(
        self,
        folder,
        endpoint, 
        domain="",
        metric="",
        segment_id=""
        ):
        if folder == 'website':
            if domain == "": # anstatt is None, wegen default values?
                raise ValueError("Please specify a domain")
            api_url = self.API_URL + "/" + folder + "/" + domain + "/" + endpoint + "/" + metric 
            return api_url

        elif folder == 'segment':
            api_url = self.API_URL + "/" + folder + "/" + segment_id + "/" + endpoint + "/" + metric
            return api_url

        elif folder == 'segment_list':
            api_url = self.API_URL + "/" + 'segment' + "/" + endpoint + "/" + metric
            return api_url
        else:
            raise ValueError(f'Folder {folder} unknown.')


    def get_total_traffic_visits(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain,
            endpoint="total-traffic-and-engagement",
            metric='visits'
            )

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request

    
    def get_total_traffic_pages_per_visit(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="total-traffic-and-engagement", 
            metric="pages-per-visit")
        
        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }
     
        request = self.call_endpoint(api_url, PARAMS)
        return request

   
    def get_total_traffic_average_visit_duration(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity):
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="total-traffic-and-engagement", 
            metric="average-visit-duration")

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request
    
    
    def get_total_traffic_bounce_rate(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="total-traffic-and-engagement", 
            metric="bounce-rate")

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request


    def get_total_traffic_pages_views(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="total-traffic-and-engagement", 
            metric="page-views")
        
        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }
             
        request = self.call_endpoint(api_url, PARAMS)
        return request
        

    def get_total_traffic_desktop_vs_mobile_split(
        self,
        domain:str, 
        start_date, 
        end_date
        ):
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="total-traffic-and-engagement", 
            metric="visits-split")
        print (api_url)

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de',
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request

    def get_total_traffic_deduplicated_audience(
        self,
        domain:str, 
        start_date, 
        end_date
        ):

        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain, 
            endpoint="dedup", 
            metric="deduplicated-audiences")

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'main_domain_only':'false',   
            'format':'json',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request

    def get_desktop_unique_visitors(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain,
            endpoint="unique-visitors",
            metric='desktop_unique_visitors'
            )

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request

    def get_mobile_web_unique_visitors(
        self,
        domain:str, 
        start_date, 
        end_date,
        granularity
        ):
        
        api_url = self.build_endpoint_url(
            folder = 'website',
            domain = domain,
            endpoint="unique-visitors",
            metric='mobileweb_unique_visitors'
            )

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        return request


    def get_segment_analysis_list_segments(
        self,

        ):
        api_url = self.build_endpoint_url(
            folder = 'segment_list',
            endpoint="traffic-and-engagement", 
            metric="describe")

        PARAMS = {
            'api_key':self.api_key,
            'userOnlySegments':'false'
             }
        
        request = self.call_endpoint(api_url, PARAMS)
        return request


    def get_segment_analysis_segment_traffic_and_engagement(
        self,
        start_date,
        end_date,
        granularity,
        segment_id,
        metrics
        ):
        
        if metrics is None:
            raise ValueError("Please specify a / multiple metric(s).")
           # check =  all(item in METRIC_LIST for item in metrics_list)
        # print(check)
        # if check is False:
        #         raise ValueError(f"{metrics}, at least one of the chosen metrics is not known, please specify a / multiple valid metric(s) of the following list: \
        #         visits,share,pages-per-visit,page-views,bounce-rate,visit-duration,unique-visitors")
        
        api_url = self.build_endpoint_url(
            folder = 'segment',
            endpoint="traffic-and-engagement",
            metric='query',
            segment_id = segment_id)

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'metrics':metrics,
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)

        return request


    def get_segment_analysis_segment_marketing_channels(
        self,
        start_date,
        end_date,
        granularity,
        segment_id,
        metrics):
             
        if metrics is None:
            raise ValueError("Please specify a / multiple metric(s).")

        api_url = self.build_endpoint_url(
            folder = 'segment',
            endpoint="marketing-channels",
            metric='query',
            segment_id = segment_id)

        PARAMS = {
            'api_key':self.api_key,
            'start_date':start_date, 
            'end_date':end_date, 
            'country':'de', 
            'granularity':granularity, 
            'main_domain_only':'false',   
            'format':'json',
            'show_verified':'false',
            'metrics':metrics,
            'mtd':'false',
             }

        request = self.call_endpoint(api_url, PARAMS)
        
        return request
