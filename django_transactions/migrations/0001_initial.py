from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExclusiveTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=256)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('ended', models.DateTimeField(null=True)),
                ('error', models.TextField(null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='exclusivetransaction',
            constraint=models.UniqueConstraint(condition=models.Q(('ended__isnull', True)), fields=('slug',), name='django_transactions_exclusivetransaction_slug_ended_uniq'),
        ),
    ]
