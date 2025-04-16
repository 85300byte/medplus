from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('QuickMedsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]