from django.db import models

# Create your models here.
choices = [
    ('1', ''),
    ('2', 'Customer'),
    ('3', 'Admin'),
]

class Customer(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
        blank=True,
        null=True,
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Email Address',
        unique=True,
        blank=True,
        null=True,
    )
    mobile = models.IntegerField(
        verbose_name='Mobile No.',
        blank=True,
        null=True,
    )
    password = models.CharField(
        verbose_name='Password',
        max_length=200,
        blank=True,
        null=True,
    )
    role = models.CharField(
        verbose_name="Role",
        max_length=2,
        choices=choices,
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name='Is active',
        default=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Purchase(models.Model):
    customer = models.ForeignKey(
        'Customer',
        verbose_name='Customer',
        related_name='customer_purchase',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        verbose_name='Date',
        blank=True,
        null=True,
    )
    amount = models.IntegerField(
        verbose_name='Amount',
        blank=True,
        null=True,
    )
    sla_unlock = models.IntegerField(
        verbose_name='SLA Unlock',
        blank=True,
        null=True,
    )
    sla_lock = models.IntegerField(
        verbose_name='SLA Lock',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(
        verbose_name='Created By',
        max_length=100,
        blank=True,
        null=True,
    )
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(
        verbose_name='Updated By',
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.customer
