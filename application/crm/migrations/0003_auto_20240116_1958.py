from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_custom_group_and_permissions(apps, schema_editor):
    # Create the custom group
    custom_group, created = Group.objects.get_or_create(name='YourCustomGroupName')

    # Get ContentType for BusinessCustomer model
    BusinessCustomer = apps.get_model('crm', 'BussinessCustomer')
    business_customer_content_type = ContentType.objects.get_for_model(BusinessCustomer)

    # Assign permissions for BusinessCustomer model
    permissions = Permission.objects.filter(content_type=business_customer_content_type)
    custom_group.permissions.add(*permissions)

    # Get ContentType for SwiftApplication model
    SwiftApplication = apps.get_model('crm', 'SwiftApplication')
    swift_application_content_type = ContentType.objects.get_for_model(SwiftApplication)

    # Assign permissions for SwiftApplication model
    permissions = Permission.objects.filter(content_type=swift_application_content_type)
    custom_group.permissions.add(*permissions)
    admin_permissions = Permission.objects.filter(content_type__app_label='admin')
    for permission in admin_permissions:
        custom_group.permissions.add(permission)
    custom_group.save()
class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_swiftapplication'),
    ]

    operations = [
        migrations.RunPython(create_custom_group_and_permissions),

    ]
