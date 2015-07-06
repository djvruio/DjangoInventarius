from django.db import models
from django.template.defaultfilters import slugify

# Clase abstracta (no se crea en la bdd)
class TimeStampModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

# Clase Brand (Marca ej. HP, Cisco, etc)
class Brand(models.Model):
	name = models.CharField(max_length=75)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

# Clase Equiment (Guarda todos los datos de un equipo)
class Equipment(TimeStampModel):
	model = models.CharField(max_length=150, blank=False, null=False)
	brand = models.ForeignKey(Brand)
	ip_conf = models.GenericIPAddressField(blank=True, null=True, default=None)
	mask_conf = models.GenericIPAddressField(blank=True, null=True, default=None)
	ip_swi = models.GenericIPAddressField(blank=True, null=True, default=None)
	mask_swi = models.GenericIPAddressField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	admin_user = models.ForeignKey(User) #falta algo

	def __unicode__(self):
		return "%s %s" % (self.brand.name, self.model)


#Clase BackupConf(Guarda los respaldos de configuraciones)
class BackupConf(TimeStampModel):
	name = models.CharField(max_length=75, editable=False)
	equipment = models.ForeignKey(Equipment)
	log_conf = models.TextField()

	def __unicode__(self):
		return self.name

		