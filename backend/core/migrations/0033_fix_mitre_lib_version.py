# Generated by Django 5.1 on 2024-11-02 01:40

from django.db import migrations


def fix_mitre_urn(apps, schema_editor):
    StoredLibrary = apps.get_model("core", "StoredLibrary")
    LoadedLibrary = apps.get_model("core", "LoadedLibrary")
    mitre_stored_library = StoredLibrary.objects.filter(
        urn="urn:intuitem:risk:library:mitre-attack-v14"
    ).first()
    mitre_loaded_library = LoadedLibrary.objects.filter(
        urn="urn:intuitem:risk:library:mitre-attack-v14"
    ).first()
    if mitre_stored_library:
        mitre_stored_library.urn = "urn:intuitem:risk:library:mitre-attack"
        mitre_stored_library.save()
    if mitre_loaded_library:
        mitre_loaded_library.urn = "urn:intuitem:risk:library:mitre-attack"
        mitre_loaded_library.save()
    for lib in StoredLibrary.objects.all():
        for i in range(len(lib.dependencies)):
            if lib.dependencies[i] == "urn:intuitem:risk:library:mitre-attack-v14":
                lib.dependencies[i] = "urn:intuitem:risk:library:mitre-attack"
                lib.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0032_vulnerability_applied_controls_filteringlabel_and_more"),
    ]

    operations = [
        migrations.RunPython(fix_mitre_urn),
    ]
