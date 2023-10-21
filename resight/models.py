from django.db import models


class Gafa(models.Model):
    solares = models.BooleanField()
    vendido = models.BooleanField()
    # Right eye values
    miopia_right = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    astigmatismo_right = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hipermetropia_right = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Left eye values
    miopia_left = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    astigmatismo_left = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hipermetropia_left = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    img = models.ImageField(upload_to='gafa_images/')
    estado = models.CharField(choices=(
        ('1', "Bueno"),
        ('2', "Muy Bueno"),
        ('3', "Excelente"),
    ),
        max_length=1
    )


''' Aportacion miguel_Updated_version:
    # Add a ManyToManyField for associating multiple images
    images = models.ManyToManyField(Image)
new_gafa = Gafa.objects.create(...)
image1 = Image.objects.create(image='path_to_image1.jpg')
image2 = Image.objects.create(image='path_to_image2.jpg')
new_gafa.images.add(image1, image2)
'''

"""
    images = models.ArrayField(
        models.ImageField(upload_to='images/'),
        blank=True,
        null=True
    )
"""
