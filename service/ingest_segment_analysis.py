from service.ingest_super import SuperIngester
from service.apiclient.api_client import SimilarWebApiClient

class SegmentAnalysisIngester(SuperIngester):

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

    def call_endpoint(self, endpoint, segment_list:list):
        python_callable = None
        if endpoint == 'segment_analysis.segment_traffic_and_engagement':  
            python_callable = self.__ingest_segment_traffic_and_engagement
        elif endpoint == 'segment_analysis.segment_marketing_channels':
            python_callable = self.__ingest_segment_marketing_channels
        else:
            raise ValueError(f"endpoint {endpoint} is unknown")

        list(map(python_callable, segment_list))

    def __ingest_segment_traffic_and_engagement(self, segment: dict):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        # call api for segment data
        segment_data = (
            swc.get_segment_analysis_segment_traffic_and_engagement(
                self.endpoint_params.get('start_date'),
                self.endpoint_params.get('end_date'),
                self.endpoint_params.get('granularity'),
                segment.get('segment_id'),
                segment.get('metrics')))  

        self._store_response(
            data=segment_data,
            identifier=segment.get('segment_id'),
            endpoint="segment_analysis_segment_traffic_and_engagement")

    def __ingest_segment_marketing_channels(self, segment: dict):
        self.subsrc = self._retrieve_folder_date()
        # create seperate metrics list for marketing channels, since the feature doesn't support "share" and "unique-visitors"
        metrics = segment['metrics']
        metrics_marketing = []
        for metric in metrics: #FIXME: Function seems not to work properly 
            if metric in ['visits', 'pages-per-visit', 'page-views', 'bounce-rate', 'visit-duration']:
                metrics_marketing.append(metric)
        swc = SimilarWebApiClient()
        ## call api for segment datagranularity, segment_id, metrics_marketing)  # call api for marketing channels
        marketing_data = (
            swc.get_segment_analysis_segment_marketing_channels(
                self.endpoint_params.get('start_date'), 
                self.endpoint_params.get('end_date'), 
                self.endpoint_params.get('granularity'),
                segment.get('segment_id'),
                metrics))

        self._store_response(
            data=marketing_data,
            identifier=segment.get('segment_id'),
            endpoint="segment_analysis_segment_marketing_channels")


    def ingest_segment_list(self):
        self.subsrc = self._retrieve_folder_date()
        swc = SimilarWebApiClient()
        segment_list = swc.get_segment_analysis_list_segments()
        segment_list_date = (
            segment_list["response"]["traffic_and_engagement"]['countries']['de']["fresh_data"].replace("-", "_"))

        self._store_response(
            data=segment_list,
            identifier=(f"segment_list_{segment_list_date}"),
            endpoint="list_segments")
