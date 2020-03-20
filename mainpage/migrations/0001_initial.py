# Generated by Django 3.0.4 on 2020-03-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=100)),
                ('product_nos', models.CharField(max_length=100)),
                ('contract_nos', models.CharField(max_length=100)),
                ('originating_research_org', models.CharField(max_length=100)),
                ('sponsor_org', models.CharField(max_length=100)),
                ('contributor_organizations', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField(verbose_name='date created')),
                ('lanaguage', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('site_url', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_org', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('other_identifying_nos', models.CharField(max_length=100)),
                ('doi_infix', models.CharField(max_length=100)),
                ('software_needed', models.CharField(max_length=100)),
                ('subject_categories_code', models.CharField(max_length=100)),
                ('creatorsblock', models.CharField(max_length=100)),
                ('downloads_int', models.IntegerField(default=0)),
                ('citations_int', models.IntegerField(default=0)),
                ('value_int', models.IntegerField(default=0)),
                ('uniqueness_int', models.IntegerField(default=0)),
            ],
        ),
    ]