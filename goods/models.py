from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# Create your models here.


#商品类别表
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name ="商品类别名")
    slug = models.CharField(max_length=120,null=True,blank = True)
    parent_id = models.ForeignKey('self',verbose_name="父类别",null=True,blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品类别"
        #这个选项是指定，模型的复数形式是什么，如果不指定Django会自动在模型名称后加一个’s’
        verbose_name_plural = verbose_name
        ordering = ('id',)


#商品表
class Good(models.Model):
    salePrice = models.DecimalField(verbose_name="零售价",max_digits=10,decimal_places =2)
    productName = models.CharField(verbose_name="商品名称",max_length =50)
    subTitle = models.CharField(verbose_name="副标题",max_length=250,null=True,blank=True)
    productImageBig =models.ImageField(verbose_name="商品大图",upload_to="product/%Y/%m/%d")
    detail = RichTextUploadingField(verbose_name="商品详情",null=True,blank=True)
    category_id = models.ForeignKey('Category',verbose_name="所属类别",null=True,blank=True,on_delete=models.CASCADE,related_name="category_id")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        ordering = ['id']

#商品图片表
class Goodimage(models.Model):
    image = models.ImageField(verbose_name="商品图片",upload_to="product/smallImage/%Y/%m/%d")
    good_id = models.ForeignKey('Good',verbose_name="商品名",on_delete=models.CASCADE,related_name="image")
    index= models.PositiveIntegerField('展示顺序',default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __str__(self):
        return self.good_id.productName

    class Meta:
        ordering = ['good_id','index']
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name