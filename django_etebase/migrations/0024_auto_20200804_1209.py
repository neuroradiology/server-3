# Generated by Django 3.0.3 on 2020-08-04 12:09

from django.db import migrations


def change_chunk_to_collections(apps, schema_editor):
    CollectionItemChunk = apps.get_model("django_etebase", "CollectionItemChunk")

    for chunk in CollectionItemChunk.objects.all():
        chunk.collection = chunk.item.collection
        chunk.save()


class Migration(migrations.Migration):

    dependencies = [
        ("django_etebase", "0023_collectionitemchunk_collection"),
    ]

    operations = [
        migrations.RunPython(change_chunk_to_collections),
    ]
