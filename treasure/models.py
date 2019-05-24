from django.db import models

class Treasure(models.Model):
    
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_image', default='media/default.png')
    
    class Meta:
        permissions = (
            ("view_treasure", "Can see available treasure"),
            ("change_treasure_status", "Can change the name of treasure"),
            ("close_treasure", "Can remove a treasure by setting its status as closed"),
            ("create_treasure", "Can create new treasure")
        )

    def __str__(self):
        return self.name