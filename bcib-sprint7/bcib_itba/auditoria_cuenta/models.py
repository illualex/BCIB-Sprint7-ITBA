# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.FloatField(blank=True, null=True)
    new_balance = models.FloatField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.TextField(blank=True, null=True)
    new_type = models.TextField(blank=True, null=True)
    user_action = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'
