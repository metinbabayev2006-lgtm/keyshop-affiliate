from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_order_productkey"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="icon_key",
            field=models.CharField(
                choices=[
                    ("default", "Default"),
                    ("fortnite", "Fortnite"),
                    ("valorant", "Valorant"),
                    ("spotify", "Spotify"),
                    ("youtube", "YouTube"),
                ],
                default="default",
                max_length=20,
            ),
        ),
    ]
