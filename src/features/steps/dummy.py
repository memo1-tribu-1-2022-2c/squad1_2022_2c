from behave import given, when, then

class DummySum():

    def __init__(self, number_1: int, number_2: int):

        self.number_1 = number_1
        self.number_2 = number_2
        self.number_sum = 0

    def sum_self(self) -> None:
        self.number_sum= self.number_1 + self.number_2

    def get_sum(self) -> int:
        return self.number_sum
    

@given(u'That I have {number_1} and {number_2}')
def step_impl(context, number_1, number_2):
    context.sum = DummySum(int(number_1), int(number_2))

@when(u'I sum them')
def step_impl(context):
    context.sum.sum_self()

@then(u'I have {result}')
def step_impl(context, result):
    if context.sum.get_sum() != int(result):
        string = f"Sum was not equal to: {result} it was: {context.sum.get_sum()}"
        raise Exception(string)