from django.conf import settings
from django.db import models


class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    type = models.ForeignKey('DocumentType', on_delete=models.PROTECT, related_name='documents')
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    requires_subscription = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DocumentAttribute(models.Model):
    type = models.ForeignKey('DocumentType', on_delete=models.CASCADE, related_name='attributes')
    attribute = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['type', 'attribute'], name='unique_attribute_per_type'),
        ]

    def __str__(self):
        return f'{self.type.name} — {self.attribute}'


class DocumentAttributeValue(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE, related_name='attribute_values')
    attribute = models.ForeignKey('DocumentAttribute', on_delete=models.CASCADE, related_name='values')
    value = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['document', 'attribute'], name='unique_value_per_document_attribute'),
        ]

    def __str__(self):
        return f'{self.document.name} — {self.attribute.attribute}: {self.value}'
