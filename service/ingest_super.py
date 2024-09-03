from trdpipe.structify_publish.pipe import BasePipe
from trdpipe.structify_publish.const import STAGE_RAW
from datetime import date
import json

class SuperIngester(BasePipe):

    def __init__(self, subsrc, params, config, endpoint_params: dict):
        super().__init__(
            config=config,
            subsrc=None,
            params=None)

        self.endpoint_params = endpoint_params

    def _retrieve_folder_date(self):
        today = date.today()
        today = date.strftime(today, "%Y%m%d")
        return today

    def _store_response(self, data, identifier, endpoint):
         # save data to json locally
        filename = f"/tmp/{endpoint}_{identifier}.json"
        with open(filename, "w") as f:
            json.dump(data, f)
        self._pushFile(
            filename=filename,
            timestamp=None,
            create_latest=False,
            create_timebased=False,
            stage=STAGE_RAW
        )