from behave import given, when, then
from src.model.product import Product, Version, SUPORTED

@given(u'A new product with name {name} and id {id}')
def impl_step(context, name, id):
    context.product = Product(name, int(id))

@when(u'It is tried to add it the system')
def step_impl(context):
    context.added = context.product.can_be_persisted()


@then(u'It fails because it has no versions')
def step_impl(context):
    if context.added:
        raise Exception("Should not be possible to add the product")


@when(u'A version {version} is added to it')
def step_impl(context, version):
    version = Version(1, version, SUPORTED, context.product)
    context.version = version


@then(u'The version is associated with the product')
def step_impl(context):
    if not context.version.associated_to(context.product):
        raise Exception("Version was not associated to product")


@then(u'The product gets added to the system')
def step_impl(context):
    if not context.added:
        raise Exception("Product was not added to the system")


@given(u'Versions {versions} associated to it')
def step_impl(context, versions):
    version_range = range(1, len(versions) + 1)
    version_objects = []
    for version_id, version_number in zip(version_range, versions):
        new_version = Version(version_id, version_number, SUPORTED, context.product)
        version_objects.append(new_version)
    
    context.versions = version_objects

@when(u'The product versions are retrieved')
def step_impl(context):
    context.retrieved_versions = context.product.get_versions()


@then(u'All versions of the product are shown')
def step_impl(context):
    for version, retrieved in zip(context.versions, context.retrieved_versions):
        if version != retrieved:
            raise Exception("A version was different from its retrieved counterpart")