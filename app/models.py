from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html_join, format_html
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )
    url = models.SlugField(max_length=55, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(verbose_name="цена", default=0)
    img = models.ImageField(verbose_name='картинка', upload_to="products/")
    description = models.TextField(verbose_name='описание')

    def get_count_comments(self):
        return self.comment.count()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name="comment", on_delete=models.CASCADE)


class Card(models.Model):
    user = models.ForeignKey(User, verbose_name='Потзыватель', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.user}"

    def get_cart_items(self):
        return self.carditem_set.all()


class CardItem(models.Model):
    card = models.ForeignKey(Card, verbose_name='Пользыватель', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество", default=0)
    price_sum = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.price_sum = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Order(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_table_products(self):
        table_body = format_html_join(
            '\n',
            """<tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                </tr>
            """,
            ((item.product.name, item.quantity, item.price_sum) for item in self.card.get_cart_items())
        )

        return format_html(
           """
           <table style='width:100%;'>
                <tr>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Price Sum</th>
                </tr>
                <tbody>
                    {0}
                </tbody>
           </table>
           """,
            table_body
        )

    get_table_products.allow_tags = True


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Card.objects.create(user=instance)