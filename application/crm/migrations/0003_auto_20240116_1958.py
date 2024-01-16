from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_custom_group_and_permissions(apps, schema_editor):
    # Create the custom group
    custom_group, created = Group.objects.get_or_create(name='Customer Relation Manager')

    # Assign permissions for BusinessCustomer model
    business_customer_content_type = ContentType.objects.get(app_label='crm', model='BussinessCustomer')
    permissions = Permission.objects.filter(content_type=business_customer_content_type)
    custom_group.permissions.add(*permissions)

    # Assign permissions for SwiftApplication model
    swift_application_content_type = ContentType.objects.get(app_label='crm', model='SwiftApplication')
    permissions = Permission.objects.filter(content_type=swift_application_content_type)
    custom_group.permissions.add(*permissions)

    # Assign permissions for Django admin login
    admin_login_permission = Permission.objects.get(codename='log in to admin site')
    custom_group.permissions.add(admin_login_permission)
class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_swiftapplication'),
    ]

    operations = [
        migrations.RunPython(create_custom_group_and_permissions),

    ]
