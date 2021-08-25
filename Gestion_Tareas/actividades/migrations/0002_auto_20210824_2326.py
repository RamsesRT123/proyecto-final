# Generated by Django 3.2.4 on 2021-08-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tareas',
            options={'ordering': ['created'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='materia',
        ),
        migrations.AddField(
            model_name='tareas',
            name='carrera',
            field=models.TextField(null=True, verbose_name='Carrera del curso'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tareas',
            name='curso',
            field=models.TextField(null=True, verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='duracion',
            field=models.TextField(max_length=12, null=True, verbose_name='Duración'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='hora',
            field=models.CharField(max_length=10, null=True, verbose_name='Turno del curso'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Portada'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='nombre',
            field=models.TextField(null=True, verbose_name='profesor'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
