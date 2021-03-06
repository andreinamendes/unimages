# Generated by Django 4.0.1 on 2022-01-27 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginas', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem_favorita',
            name='imagem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paginas.imagem'),
        ),
        migrations.AlterField(
            model_name='imagem_favorita',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
