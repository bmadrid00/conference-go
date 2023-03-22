from json import JSONEncoder
from datetime import datetime
from django.db.models import QuerySet


class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return datetime.isoformat(o)
        else:
            return super().default(o)


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class ModelEncoder(DateEncoder, QuerySetEncoder, JSONEncoder):
    encoders = {}

    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            if hasattr(o, "get_api_url"):
                d["href"] = o.get_api_url()
            for propert in self.properties:
                attr = getattr(o, propert)
                if propert in self.encoders:
                    encoder = self.encoders[propert]
                    attr = encoder.default(attr)
                d[propert] = attr
            d.update(self.get_extra_data(o))
            return d
        else:
            return super().default(o)

    def get_extra_data(self, o):
        return {}
