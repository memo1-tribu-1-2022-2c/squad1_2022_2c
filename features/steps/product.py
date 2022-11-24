from behave import given, when, then
from model.product import Product


@given(u'A new product with name {name} and id {id}')
def impl_step(context, name, id):
    context.product = Product(name, int(id))

@when(u'It is tried to add it the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: When It is tried to add it the system')


@then(u'It fails because it has no versions')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then It fails because it has no versions')


@when(u'A version {version} is added to it')
def step_impl(context, version):
    raise NotImplementedError(u'STEP: When A version 1.1 is added to it')


@then(u'The version is associated with the product')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The version is associated with the product')


@then(u'The product gets added to the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The product gets added to the system')


@given(u'Versions {versions} associated to it')
def step_impl(context, versions):
    raise NotImplementedError(u'STEP: Given Versions [2.3, 4.5, 6.7, 10.8] associated to it')


@when(u'The product versions are retrieved')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The product versions are retrieve')


@then(u'All versions of the product are shown')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then All versions of the product are shown')