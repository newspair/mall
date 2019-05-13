
#导包 导入序列化库
from rest_framework import serializers
#导入数据库 类
from .models import *



#获取分类
#品牌表
class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        
        fields = '__all__'

#分类表
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        
        fields = '__all__'

#添加分类
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    level = serializers.IntegerField(required=True)
    parent_id = serializers.IntegerField(required=True)
    is_nav_status = serializers.IntegerField(required=True)
    status = serializers.IntegerField(required=True)
    sort = serializers.IntegerField(required=True)
    image = serializers.CharField(required=True, max_length=100)
    keyword = serializers.CharField(required=True, max_length=100)
    descrip = serializers.CharField(required=True, max_length=255)
    productUnit = serializers.CharField(required=True, max_length=255)


    def create(self,validated_data):
        return Category.objects.create(**validated_data)



#定义反序列化类
class BrandSerializer(serializers.Serializer):
    
    name = serializers.CharField(required=True,max_length=50)
    first = serializers.CharField(required=True,max_length=1)
    logo = serializers.CharField(required=True,max_length=255)
    b_logo = serializers.CharField(required=True,max_length=255)
    story = serializers.CharField(required=True,max_length=255)
    sort = serializers.IntegerField(required=True)
    is_show = serializers.IntegerField(default=0)
    is_company = serializers.IntegerField(default=0)
    

    def create(self,data):
        
        return Brand.objects.create(**data)



#类型表
class LeixingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods_type
        
        fields = '__all__'

#类型表添加反序列化
class LeixingSerializer(serializers.Serializer):
    # id = models.AutoField(primary_key=True)
    name = serializers.CharField(required=True,max_length=100)
    attribute_count = serializers.IntegerField(default=0)
    param_count = serializers.IntegerField(default=0)

    def create(self,data):
        print(data)
        return Goods_type.objects.create(**data)

#属性表
class ShuxingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods_type_attribute
        
        fields = '__all__'

#定义属性表反序列化类
class ShuxingSerializer(serializers.Serializer):
    
    name = serializers.CharField(required=True,max_length=50)
    filter_type = serializers.CharField(default=1)
    is_select = serializers.CharField(default=0)
    related_status = serializers.CharField(default=0)
    select_type = serializers.IntegerField(default=0)
    input_type = serializers.IntegerField(default=0)
    input_list = serializers.CharField(default='',max_length=50)
    hand_add_status = serializers.IntegerField(default=0)
    sort = serializers.IntegerField(required=True)
    Type = serializers.IntegerField(required=True)

    def create(self,data):
        # print(data)
        
        
        return Goods_type_attribute.objects.create(type_id=self.context["g"],**data)


#秒杀时间段表
class FlashModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceckil_activity
        
        fields = '__all__'


#秒杀时间段反序列化
class FlashSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=30) #名称
    startTime=serializers.DateTimeField(required=True) #开始时间
    endTime=serializers.DateTimeField(required=True) #结束时间
    status=serializers.IntegerField(default=0) #状态（1是0否）

    def create(self,data):
        print(data)
        return Ceckil_activity.objects.create(**data)


#m秒杀活动表
class QuentumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quentum

        fields = '__all__'


#秒杀活动反序列化
class QuentumSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=30) #名称
    start_time=serializers.DateTimeField(required=True) #开始时间
    end_time=serializers.DateTimeField(required=True) #结束时间
    is_on = serializers.IntegerField(default=0)#是否上线


    def create(self,data):
        print(data)
        return Quentum.objects.create(**data)


#优惠券表
class CouponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon

        fields = '__all__'


#优惠卷表
class CouponSerializer(serializers.Serializer):
    Type = serializers.IntegerField(default=0)
    name = serializers.CharField(required=True,max_length=255)
    platform = serializers.IntegerField(default=0)
    number = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)
    limit_get = serializers.IntegerField(default=0)
    threshold = serializers.IntegerField(default=0)
    starttime = serializers.DateTimeField(required=True)
    stoptime = serializers.DateTimeField(required=True)
    type1 = serializers.IntegerField(default=0)
    describe = serializers.CharField(required=True,max_length=255)
    starte = serializers.IntegerField(default=0)
    Y_l_number = serializers.IntegerField(default=0)
    D_l_number = serializers.IntegerField(default=0)
    Y_s_number = serializers.IntegerField(default=0)
    W_s_number = serializers.IntegerField(default=0)

    def create(self,data):
        print(data)
        return Coupon.objects.create(**data)