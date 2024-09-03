from service.ingest_super import SuperIngester
from service.apiclient.api_client import SimilarWebApiClient

class TotalTrafficIngester(SuperIngester):
    
    datasource = "similarweb"
    def __init__(self, config, endpoint_params: dict):
        super().__init__(
            config=config,
            subsrc=None,
            params=None,
            endpoint_params=endpoint_params)
    
    def call_endpoints(self, endpoints:dict):
        for key in endpoints:
            self.call_endpoint(key, endpoints[key])    
    
    def call_endpoint(self, endpoint, domain_list:list):
        python_callable = None
        if endpoint == 'total_traffic.visits':
            python_callable = self.__ingest_total_traffic_visits
        elif endpoint == 'total_traffic.pages_per_visit':
            python_callable = self.__ingest_total_traffic_pages_per_visit
        elif endpoint == 'total_traffic.page_views':
            python_callable = self.__ingest_total_traffic_page_views
        elif endpoint == 'total_traffic.deduplicated_audience':
            python_callable = self.__ingest_total_traffic_deduplicated_audience
        elif endpoint == 'desktop.unique_visitors':
            python_callable = self.__ingest_desktop_unique_visitors
        elif endpoint == 'mobile_web.unique_visitors':
            python_callable = self.__ingest_mobile_web_unique_visitors
        elif endpoint == 'total_traffic.desktop_vs_mobile_split':
            python_callable = self.__ingest_total_traffic_desktop_vs_mobile_split

        else:
            raise ValueError(f"endpoint {endpoint} is unknown")

        list(map(python_callable, domain_list))

    def __ingest_total_traffic_visits(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
            swc.get_total_traffic_visits(
                domain.get('url'),
                self.endpoint_params.get('start_date'),  
                self.endpoint_params.get('end_date'),
                self.endpoint_params.get('granularity')))

        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="total_traffic_visits")
        
        
    
    def __ingest_total_traffic_pages_per_visit(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
            swc.get_total_traffic_pages_per_visit(
            domain.get('url'),
            self.endpoint_params.get('start_date'),  
            self.endpoint_params.get('end_date'),
            self.endpoint_params.get('granularity')))
        
        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="total_traffic_pages_per_visit")
        
    
    def __ingest_total_traffic_page_views(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
        swc.get_total_traffic_pages_views(
            domain.get('url'),
            self.endpoint_params.get('start_date'),  
            self.endpoint_params.get('end_date'),
            self.endpoint_params.get('granularity')))
    
        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="total_traffic_page_views")
        
    
    def __ingest_total_traffic_deduplicated_audience(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient() 
        domain_data = (
            swc.get_total_traffic_deduplicated_audience(
                domain.get('url'),
                self.endpoint_params.get('start_date'),  
                self.endpoint_params.get('end_date')))

        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="total_traffic_deduplicated_audience")
        
    def __ingest_desktop_unique_visitors(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
            swc.get_desktop_unique_visitors(domain.get('url'),
            self.endpoint_params.get('start_date'),  
            self.endpoint_params.get('end_date'),
            self.endpoint_params.get('granularity')))
        
        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="desktop_unique_visitors")
        
        
    def __ingest_mobile_web_unique_visitors(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
            swc.get_mobile_web_unique_visitors(
                domain.get('url'),
                self.endpoint_params.get('start_date'),  
                self.endpoint_params.get('end_date'),
                self.endpoint_params.get('granularity')))

        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="mobile_unique_visitors")
        


    def __ingest_total_traffic_desktop_vs_mobile_split(self, domain: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        domain_data = (
            swc.get_total_traffic_desktop_vs_mobile_split(
                domain.get('url'),
                self.endpoint_params.get('start_date'),  
                self.endpoint_params.get('end_date')))
        
        self._store_response(data=domain_data,
                            identifier=domain.get('url').replace(".", "_"),
                            endpoint="total_traffic_desktop_vs_mobile_split")
        
    