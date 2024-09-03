import os
from flask import Flask, request
import logging
import traceback
from logging.config import dictConfig
from service.ingest_segment_analysis import SegmentAnalysisIngester
from service.ingest_total_traffic import TotalTrafficIngester
from service.request_mapping_total_traffic import RequestMapperTotalTraffic
from service.request_mapping_segment_analysis import RequestMapperSegmentAnalysis
from trdpipe.structify_publish.helper import loadConfig
from service.helper_dates import calculate_dates
from datetime import date
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(message)s',
    }},
    'handlers': {'console': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
})


app = Flask(__name__)

@app.route('/', methods=['POST'])
def callapi():

    try:
        endpoint = request.args.get('endpoint')    
        env = request.args.get("env")
        granularity = request.args.get("granularity")
        if endpoint is None:
            raise ValueError("Please specify an endpoint.") 
        if env is None:
            raise ValueError("Please specify an environment.")
        if granularity is None:
            raise ValueError("Please specify a granularity.")
        
        config = loadConfig(env,'')
        SEGMENT_MONTH_COUNT = 14 # Parameter to count backwarts: we get 15 months of data for segment analysis provided by similarweb
        DOMAIN_MONTH_COUNT = 2 # and 3 months of data for total traffic analysis
        ingest_list = request.get_json()

        if 'segment_analysis' in endpoint:
            
            start_date = calculate_dates(SEGMENT_MONTH_COUNT,date.today()).get('start_date')
            end_date = calculate_dates(SEGMENT_MONTH_COUNT,date.today()).get('end_date')
            endpoints = RequestMapperSegmentAnalysis().map_request(ingest_list)    
            swi = SegmentAnalysisIngester(
            config=config, 
            endpoint_params={'granularity':granularity,
                                'start_date':start_date,
                                    'end_date':end_date})
            swi.ingest_segment_list()
            for key in endpoints:
                swi.call_endpoint(key, endpoints[key])
            return f"successfully called {endpoint}", 200

        elif 'total_traffic' in endpoint:
  
            start_date = calculate_dates(DOMAIN_MONTH_COUNT,date.today()).get('start_date')
            end_date = calculate_dates(DOMAIN_MONTH_COUNT,date.today()).get('end_date')
            endpoints = RequestMapperTotalTraffic().map_request(ingest_list)    
            swi = TotalTrafficIngester(
                config=config,
                endpoint_params={'granularity':granularity,
                                    'start_date':start_date,
                                        'end_date':end_date})
            for key in endpoints:
                swi.call_endpoint(key,endpoints[key])            
            return f"successfully called {endpoint}", 200
    
    
    except Exception as e:
        error = f"ERROR OCCURED: {e}"
        logging.error(error)
        logging.error(traceback.format_exc())
        return error, 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
