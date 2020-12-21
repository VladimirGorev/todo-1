from django.db import models


class ListItem(models.Model):
    """
    Модель элемента списка
    """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    list_model = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'@id={self.id}@name={self.name}@list={self.list_model.name}'

    class Meta:
        verbose_name = 'Элемент списка'
        verbose_name_plural = 'Элементы списка'
        unique_together = ('name', 'list_model')
