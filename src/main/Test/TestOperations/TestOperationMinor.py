from TestOperation import TestOperation

class TestOperationMin(TestOperation):

    def assert_operation(self, left_side, rigth_side):
        return left_side < rigth_side