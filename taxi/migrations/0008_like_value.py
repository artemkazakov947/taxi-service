from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0007_rename_like_message_liked_alter_message_author_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
