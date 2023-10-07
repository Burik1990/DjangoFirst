import  json

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import  BASE_DIR
class Command(BaseCommand):
    help = '?????????? ???? ?????? ??????????'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open(BASE_DIR/'data_category.json', encoding='utf-8') as fp:
            category_data = json.load(fp)
            for item in category_data:
                Category.objects.create(
                    pk= item['pk'],
                    name = item["fields"]["name"],
                    description = item["fields"]["description"]
                )
        with open(BASE_DIR/'data.json', encoding='utf-8') as fp:
            product_data = json.load(fp)
            for item in product_data:
                category_pk = item["fields"]["category"]
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"],
                    preview=item["fields"]["preview"],
                    category=category,
                    price=item["fields"]["price"],
                    date_of_creation=item["fields"]["date_of_creation"],
                    last_modified_date=item["fields"]["last_modified_date"]
                )
