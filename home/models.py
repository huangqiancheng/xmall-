from django.db import models

# Create your models here.

#首页导航栏
from goods.models import Good


class Navlist(models.Model):
    name = models.CharField(max_length=120,verbose_name="导航名称")
    panelId = models.PositiveIntegerField('面板ID',default=0)
    #链接类型，默认为1,1为本地链接，0为站外链接
    type = models.PositiveIntegerField('链接类型',default=1)
    #排序
    sortOrder = models.PositiveIntegerField('排序',default=0)
    fullUrl = models.CharField(max_length=120,verbose_name="网址链接")
    picUrl = models.CharField(max_length=120,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "导航栏类别"
        verbose_name_plural = verbose_name
        ordering = ['sortOrder']


#首页面板
class Panel(models.Model):
    name = models.CharField(max_length=120,verbose_name="板块名称")
    type = models.PositiveIntegerField()
    sort_order = models.PositiveIntegerField(verbose_name="排序")
    position = models.PositiveIntegerField(default=0)
    limit_num = models.PositiveIntegerField()
    status = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "首页面板"
        verbose_name_plural = verbose_name

class Panelcontent(models.Model):
    type = models.PositiveIntegerField()
    good_id = models.ForeignKey(Good,verbose_name="商品ID",null=True,blank=True,related_name="goods",on_delete=models.CASCADE)
    sort_order = models.PositiveIntegerField(verbose_name="排序")
    full_url = models.CharField(max_length=120,null=True,blank=True)
    pic_url =  models.CharField(max_length=100,null=True,blank=True)
    pic_url2 =  models.CharField(max_length=100,null=True,blank=True)
    pic_url3 =  models.CharField(max_length=100,null=True,blank=True)
    panel_id = models.ForeignKey(Panel,verbose_name="面板ID",related_name = "panels",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.good_id.productName

    class Meta:
        verbose_name = "面板内容"
        verbose_name_plural = verbose_name
