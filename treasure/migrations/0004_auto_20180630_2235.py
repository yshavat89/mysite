# Generated by Django 2.0 on 2018-06-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0003_auto_20180624_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treasure',
            options={'permissions': (('view_treasure', 'Can see available treasure'), ('change_treasure_status', 'Can change the name of treasure'), ('close_treasure', 'Can remove a treasure by setting its status as closed'), ('create_treasure', 'Can create new treasure'))},
        ),
    ]
