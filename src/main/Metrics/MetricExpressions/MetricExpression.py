import abc
from Metrics import Metric

class MetricExpression(Metric, metaclass=abc.ABCMeta):

    def __init__(self, metric):
        self._metric = metric

    def evaluate(self, value, metric_context):
        pass

    def get_metric_result(self):
        pass
