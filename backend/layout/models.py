from django.db import models


class Tables(models.Model):
    
    class Meta:
        verbose_name_plural = 'Tables'
        ordering = ('id',)
    
    title = models.CharField(max_length=254)
    machine_numbers = models.IntegerField()
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name
    
    def get_absolute_url(self):
        return f'/{self.slug}'


class Computers(models.Model):

    class Meta:
        verbose_name_plural = 'Computers'
        ordering = ('date_added',)

    table = models.ForeignKey(
        Tables, 
        on_delete=models.CASCADE
        )
    machine_title = models.CharField(max_length=254)
    machine_os = models.CharField(max_length=254)
    machine_ip_address = models.CharField(max_length=254)
    machine_user_name = models.CharField(max_length=254)
    numbers_of_gpu = models.IntegerField()
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_title
    
    def get_absolute_url(self):
        return f'/{self.table.slug}/{self.slug}'