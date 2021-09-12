from django.db import models

#models = models.IntegerField(default=0 , verbose_name="")

class Pdd(models.Model):
    d_max = models.IntegerField(default=0 , verbose_name="دوز ماکسیمم")
    d = models.IntegerField(default=0 , verbose_name="دوز در عمق دلخواه")

class RecToSq(models.Model):
    a_rec = models.IntegerField(default=0 , verbose_name="مساحت مستطیل")
    p_rec = models.IntegerField(default=0 , verbose_name="محیط مستظیل")

class Tar(models.Model):
    d = models.IntegerField(default=0 , verbose_name="دوز در عمق مورد نظر")
    fs = models.IntegerField(default=0 , verbose_name="دوز در همان فاصله اما هوای آزاد")    

class TarToPdd(models.Model):
    tar = models.IntegerField(default=0 , verbose_name="tar مقدار")
    bsf = models.IntegerField(default=0 , verbose_name="مقدار bsf")
    ssd = models.IntegerField(default=0 , verbose_name="مقدار ssd")
    d_max = models.IntegerField(default=0 , verbose_name="عمق دوز ماکسیمم")
    d = models.IntegerField(default=0 , verbose_name="عمق مورد نظر")

class SsdToSsd(models.Model):
    old_pdd = models.IntegerField(default=0 , verbose_name="pdd برای فاصله قبلی")
    bsf_rf = models.IntegerField(default=0 , verbose_name=" bsf (r/√f)")
    bsf_r = models.IntegerField(default=0 , verbose_name="bsf فیلد r")
    f_minord = models.IntegerField(default=0 , verbose_name="فاکتور ماینورد")

class MuSsdTechnique(models.Model):
    td = models.IntegerField(default=0 , verbose_name="دوز تومور")
    k = models.IntegerField(default=0 , verbose_name="ضریب k")
    pdd = models.IntegerField(default=0 , verbose_name="ضریب pdd")
    sc = models.IntegerField(default=0 , verbose_name="ضریب Sc")
    sp = models.IntegerField(default=0 , verbose_name="ضریب Sp")
    ssd_fac = models.IntegerField(default=0 , verbose_name="ضریب ssd factor")

class MuSadTechnique(models.Model):
    td = models.IntegerField(default=0 , verbose_name="دوز تومور")
    k = models.IntegerField(default=0 , verbose_name="ضریب k")
    tmr = models.IntegerField(default=0 , verbose_name="ضریب TMR")
    sc = models.IntegerField(default=0 , verbose_name="ضریب Sc")
    sp = models.IntegerField(default=0 , verbose_name="ضریب Sp")
    sad_fac = models.IntegerField(default=0 , verbose_name="ضریب sad factor")
    oar = models.IntegerField(default=0 , verbose_name="ضریب OAR")





