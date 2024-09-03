class RequestMapperSegmentAnalysis():

    def __init__(self):
        pass

    def map_request(self, segment_list:list):
        mapped = {}
        for d in segment_list:
            endpoint_list = mapped.get(d['endpoint'])
            if endpoint_list is None:
                endpoint_list = []
                mapped[d['endpoint']] = endpoint_list
                
            endpoint_list.append({'segment_id':d.get('segment_id'),'metrics':d.get('metrics')})
        
        return mapped