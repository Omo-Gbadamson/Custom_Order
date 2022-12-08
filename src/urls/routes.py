from ..views.customOrder import CustomOrdersApi, CustomOrderApi, CustomSearchApi
from ..views.measurement import MeasurementsApi, MeasurementApi, MeasureSearchApi 


def start_route(api):
    api.add_resource(CustomOrdersApi, "/api/orders")
    api.add_resource(CustomOrderApi, "/api/order/<id>")
    api.add_resource(CustomSearchApi, "/api/order/search/")

    api.add_resource(MeasurementsApi, "/api/measurement")
    api.add_resource(MeasurementApi, "/api/measurement/<id>")
    api.add_resource(MeasureSearchApi, "/api/measurement/search")