from django.db import models


class Client(models.Model):
    class Meta:
        app_label = 'projects'

    name = models.CharField(max_length=255, primary_key=True)


class Project(models.Model):
    class Meta:
        app_label = 'projects'

    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)


class ProjectElement(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.PROTECT)
    ref = models.CharField(max_length=255, unique=True)
    tq_pr = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    drawing = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    elev = models.CharField(max_length=255, blank=True, null=True)
    prod = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    ppc_side = models.CharField(max_length=255, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    total_lm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_m2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Additional fields with same structure as above but differentiated by '.1' suffix
    height_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    width_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qty_1 = models.PositiveIntegerField(blank=True, null=True)
    total_lm_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_m2_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    unit = models.CharField(max_length=255, blank=True, null=True)
    thickness = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    welds = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    phase = models.CharField(max_length=255, blank=True, null=True)
    priority_1 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.ref} - {self.project_name} - {self.description}"
    
    class Meta:
        app_label  = 'projects'