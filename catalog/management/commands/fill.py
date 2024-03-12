import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('catalog_data.json', 'r') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_data():
            if category['model'] == "catalog.category":
                category_for_create.append(
                    Category(pk=category['pk'], category_name=category['fields']['category_name'],
                             description=category['fields']['description'])
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_data():
            if product['model'] == "catalog.product":
                category_get = Category.objects.get(pk=product['fields']['category'])
                product_for_create.append(
                    Product(pk=product['pk'], product_name=product['fields']['product_name'],
                            product_description=product['fields']['product_description'],
                            category=category_get, purchase_price=product['fields']['purchase_price']
                            )
                )

        Product.objects.bulk_create(product_for_create)
