# Generated by Django 4.0.2 on 2022-03-02 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_mensaje_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='usuarios.usuario'),
        ),
    ]