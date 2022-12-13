from django.db import models
from django.template.defaultfilters import truncatechars
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")

I = '0'
E = '1'

KATEGORI_PAPER_CHOICES = (
    (I, 'Impor'),
    (E, 'Ekspor'),
)


class Negara(models.Model):
    nama = models.CharField(max_length=25)
    Kode = models.CharField(max_length=2)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Negara")
        verbose_name_plural = ("Negara")


class Distrik(models.Model):
    nama = models.CharField(max_length=25)
    negara = models.ForeignKey(Negara, on_delete=models.CASCADE)
    kode = models.CharField(max_length=5, blank=True, null=True)
    kode_pos = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.nama + ' ' + str(self.negara)

    class Meta:
        verbose_name = ("Provinsi/Distrik")
        verbose_name_plural = ("Provinsi/Distrik")


class Kontak(models.Model):
    nama = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)
    jabatan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Kontak")
        verbose_name_plural = ("Kontak")


class Shipper(models.Model):
    nama = models.CharField(max_length=50)
    id_shipper = models.PositiveIntegerField(blank=True)
    npwp = models.CharField(max_length=25)
    alamat = models.TextField()
    kota = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)
    kontak = models.ManyToManyField(Kontak)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Shipper")
        verbose_name_plural = ("Shipper")


class Consignee(models.Model):
    nama = models.CharField(max_length=50)
    id_consignee = models.PositiveIntegerField(blank=True)
    tax_id = models.CharField(max_length=25)
    alamat = models.TextField()
    kota = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)
    kontak = models.ManyToManyField(Kontak)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Consignee")
        verbose_name_plural = ("Consignee")


class Vessel(models.Model):
    liner = models.CharField(max_length=30)
    vessel_flight = models.CharField(max_length=30)
    voyage = models.CharField(max_length=6)
    imo = models.CharField(max_length=10)

    def __str__(self):
        return self.liner

    class Meta:
        verbose_name = ("Vessel")
        verbose_name_plural = ("Vessel")

class shipment_status(models.Model):
    nama = models.CharField(max_length=10)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Status Shipment")
        verbose_name_plural = ("Status Shipment")
class Shipment(models.Model):
    shipment_id = models.PositiveIntegerField()

    def __str__(self):
        return self. shipment_id

    class Meta:
        verbose_name = ("Shipment")
        verbose_name_plural = ("Shipment")