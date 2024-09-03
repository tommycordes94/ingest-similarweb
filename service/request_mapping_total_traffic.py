class RequestMapperTotalTraffic():

    def __init__(self):
        pass

    def map_request(self, domain_list:list):
        mapped = {}
        for d in domain_list:
            endpoint_list = mapped.get(d['endpoint'])
            if endpoint_list is None:
                endpoint_list = []
                mapped[d['endpoint']] = endpoint_list
                
            endpoint_list.append({'url':d.get('url')})
        
        return mapped