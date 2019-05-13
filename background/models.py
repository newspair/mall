#导包 导入django数据库
from django.db import models

from django.contrib.auth.models import AbstractUser  

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        
        abstract = True

# #后台用户表
class Admins(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    image = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=20)
    Login_time = models.DateTimeField(auto_now_add=True)
    #状态
    status = models.IntegerField(default=1)



    class Meta: 
         #必须和数据库中的表名吻合
        db_table = "admins"




# 后台角色
class Roles(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    l_image = models.CharField(max_length=30)
    status = models.IntegerField(default=1)


    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "roles"


# # 后台角色关联表
class Admin_roles(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    admin_id = models.ManyToManyField(Admins,related_name='admin_id')
    role_id = models.ManyToManyField(Roles,related_name='r_id')

    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "admin_roles"


# 权限表
class Permission(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    l_image = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "permission"

    
# 角色权限表
class Role_permission(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ManyToManyField(Roles,related_name='ro_id')
    Permission_id = models.ManyToManyField(Permission,related_name='Permission_id')
    
    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "role_permission"


# 用户表
class Users(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    login_count = models.IntegerField()

    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "Users"



#用户信息表
class Users_detail(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users,to_field='id',on_delete='CASCADE',related_name='u_id')
    nickname = models.IntegerField()
    sex = models.IntegerField(default=1)
    birthday = models.DateTimeField()
    city = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    personalized = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    score = models.IntegerField()
    growth = models.IntegerField()

    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "users_detail"


#品牌表
class Brand(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    first = models.CharField(max_length=1)
    logo = models.CharField(max_length=255)
    b_logo = models.CharField(max_length=255)
    story = models.CharField(max_length=255)
    sort = models.IntegerField()
    is_show = models.IntegerField(default=0)
    is_company = models.IntegerField(default=0)

    #声明表名
    class Meta:
        #必须和数据库中的表名吻合
        db_table = "brand"


#分类表
class Category(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    productUnit = models.CharField(max_length=100)
    level = models.IntegerField()
    parent_id = models.IntegerField(default=0)
    is_nav_status = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    sort = models.IntegerField(default=0)
    image = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    descrip = models.CharField(max_length=255)

    class Meta():
        db_table = 'category'
        
    def to_dict(self):
        dict1 = {'id': self.id,'name':self.name}
        return dict1

#商品类型表
class Goods_type(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    attribute_count = models.IntegerField(default=0)
    param_count = models.IntegerField(default=0)
    
    class Meta():
        db_table = 'goods_type'

    def to_dict(self):
        dict1 = {'id': self.id,'name':self.name}
        return dict1

#商品类型属性表
class Goods_type_attribute(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type_id = models.ForeignKey(Goods_type, to_field='id', on_delete='CASCADE', related_name='t_id')
    filter_type = models.IntegerField(default=1)
    is_select = models.IntegerField(default=0)
    related_status = models.IntegerField(default=0)
    select_type = models.IntegerField(default=0)
    input_type = models.IntegerField(default=0)
    input_list = models.CharField(default='',max_length=50)
    hand_add_status = models.IntegerField(default=0)
    sort = models.IntegerField()
    Type = models.IntegerField()
    
    class Meta():
        db_table = 'goods_type_attribute'

    def to_dict(self):
        dict1 = {'id': self.id,'name':self.name}
        return dict1


#分类属性关联表
class Cate_attribute(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    cate_id = models.ForeignKey(Category, to_field='id', on_delete='CASCADE', related_name='ca_id')
    goods_type_attribute_id = models.ForeignKey(Goods_type_attribute, to_field='id', on_delete='CASCADE', related_name='goods_type_attribute_id')

    class Meta():
        db_table = 'cate_attribute'



#用户成长值表
class Growth(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    descrip = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)

    class Meta:
        db_table = "growth"

#用户积分表
class Score(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    descrip = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    action = models.IntegerField(default=0)

    class Meta:
        db_table = "score"

#标签表
class Label(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    labelname = models.CharField(max_length=255)

    class Meta:
        db_table = "label"

#话题分类表
class Discourse_category(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "discourse_category"

#话题详情表
class Discourse_detail(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    user_id = models.IntegerField(default=0)
    is_hort = models.IntegerField(default=0)
    content = models.CharField(max_length=255)
    collect_sum = models.IntegerField(default=0)
    read_sum = models.IntegerField(default=0)
    evaluate_sum = models.IntegerField(default=0)
    is_show = models.IntegerField(default=0)
    dc_id = models.IntegerField(default=0) #所属分类id

    class Meta:
        db_table = "discourse_detail"

#话题标签表
class Discourse_label(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    label_id = models.ForeignKey(Label, to_field='id', on_delete='CASCADE', related_name='label_id')
    discourse_detail_id = models.ForeignKey(Discourse_detail, to_field='id', on_delete='CASCADE', related_name='discourse_detail_id')

    class Meta():
        db_table = 'discourse_label'

#用户话题收藏表
class Discourse_collect(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, to_field='id', on_delete='CASCADE', related_name='us_id')
    discourse_id = models.ForeignKey(Discourse_detail, to_field='id', on_delete='CASCADE', related_name='discourse_id')
    Type = models.IntegerField(default=0) #1话题  2专题  3商品 4 品牌

    class Meta():
        db_table = 'discourse_collect'

#话题评论表
class Discourse_comment(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    discourse_id = models.IntegerField()
    content = models.CharField(max_length=255)
    pid = models.IntegerField(default=0)
    total_zan = models.IntegerField(default=0)

    class Meta:
        db_table = "discourse_comment"

#话题评论图片表
class Discourse_comment_img(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    discourse_comment_id = models.IntegerField()
    pic = models.CharField(max_length=255)

    class Meta:
        db_table = "discourse_comment_img"

#评论点赞表
class Comment_zan(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, to_field='id', on_delete='CASCADE', related_name='user_id')
    discourse_comment_id = models.ForeignKey(Discourse_comment, to_field='id', on_delete='CASCADE', related_name='dc_id')

    class Meta():
        db_table = 'comment_zan'

#话题评论表
class Discourse_award(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    discourse_id = models.IntegerField()
    discrip = models.CharField(max_length=255)
    number = models.IntegerField(default=0)
    Type = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    label_id = models.CharField(max_length=255) #优惠卷编码

    class Meta:
        db_table = "discourse_award"

#优惠卷表
class Coupon(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    Type = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    platform = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    limit_get = models.IntegerField(default=0)
    threshold = models.IntegerField(default=0)
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()
    type1 = models.IntegerField(default=0)
    describe = models.CharField(max_length=255)
    starte = models.IntegerField(default=0)
    Y_l_number = models.IntegerField(default=0)
    D_l_number = models.IntegerField(default=0)
    Y_s_number = models.IntegerField(default=0)
    W_s_number = models.IntegerField(default=0)
    
    class Meta:
        db_table = "coupon"

#用户优惠卷表
class User_label(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    user_id = models.IntegerField()
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()
    coupon_code = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    
    class Meta:
        db_table = "user_label"

#喜欢的分类表
class Like_category(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, to_field='id', on_delete='CASCADE', related_name='yonghu_id')
    category_id = models.ForeignKey(Category, to_field='id', on_delete='CASCADE', related_name='c_id')

    
    class Meta:
        db_table = "like_category"

#用户关注的品牌
class User_concern_brand(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, to_field='id', on_delete='CASCADE', related_name='user_brand_id')
    brand_id = models.ForeignKey(Brand, to_field='id', on_delete='CASCADE', related_name='brand_id')

    
    class Meta:
        db_table = "user_concern_brand"

#商品表
class Goods(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField()
    cate_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    brand_id = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255)
    goods_code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market_price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    low_stock = models.IntegerField(default=0)
    unit = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    sort = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    growht = models.IntegerField(default=0)
    use_point_limit = models.IntegerField(default=0)
    is_preview = models.IntegerField(default=0)
    is_pubilsh = models.IntegerField(default=0)
    is_new = models.IntegerField(default=0)
    detail_title = models.CharField(max_length=255)
    deatail_descrip = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    goods_type_id = models.IntegerField(default=0)
    content = models.CharField(max_length=255)
    
    class Meta:
        db_table = "goods"

#商品促销价格表
class Goods_sales_price(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    promote_price = models.DecimalField(max_digits=8, decimal_places=2)
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()

    class Meta:
        db_table = "goods_sales_price"

#商品会员价格表
class Goods_member_price(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    member_level_id = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    member_level_name = models.CharField(max_length=50)

    class Meta:
        db_table = "goods_member_price"

#商品阶梯价格表
class Goods_fight(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    pro_count = models.IntegerField()
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "goods_fight"

#商品满减表
class Goods_full_price(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    full_price = models.DecimalField(max_digits=8, decimal_places=2)
    reduce_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "goods_full_price"

#商品属性表
class Goods_attribute_value(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(Goods, to_field='id', on_delete='CASCADE', related_name='g_id')
    attribute_id = models.ForeignKey(Goods_type_attribute, to_field='id', on_delete='CASCADE', related_name='attribute_id')

    class Meta:
        db_table = "goods_attribute_value"

#商品属性库存表
class Goods_attribute_stock(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    sku_code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    low_stock = models.IntegerField(default=0)
    sp1 = models.CharField(max_length=255)
    sp2 = models.CharField(max_length=255)
    sp3 = models.CharField(max_length=255)
    sale = models.IntegerField(default=0)
    lock_stocp = models.IntegerField(default=0)

    class Meta:
        db_table = "goods_attribute_stock"

#商品相册表
class Goods_pics(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    pic = models.CharField(max_length=255)

    class Meta:
        db_table = "goods_pics"

#指定商品优惠表
class Goods_coupon(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.ForeignKey(Coupon, to_field='id', on_delete='CASCADE', related_name='cou_id')
    goods_id = models.ForeignKey(Goods, to_field='id', on_delete='CASCADE', related_name='goods_id')

    class Meta:
        db_table = "goods_coupon"

#优惠卷分类表
class Coupon_cate(BaseModel,models.Model):   
    id = models.AutoField(primary_key=True)
    coupon_id = models.ForeignKey(Coupon, to_field='id', on_delete='CASCADE', related_name='coup_id')
    cate_id = models.ForeignKey(Category, to_field='id', on_delete='CASCADE', related_name='cate_id')

    class Meta():
        db_table = 'coupon_cate'

#省市区表
class Area(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.IntegerField(default=0)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "area"

#用户收获地址表
class Address(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    country = models.IntegerField(default=0)
    city = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    telphone = models.CharField(max_length=255)
    is_default = models.IntegerField(default=0)

    class Meta:
        db_table = "address"

#购物车表
class Cart(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=255)
    sp1 = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    img = models.CharField(max_length=255)

    class Meta:
        db_table = "cart"

#用户订单表
class User_orders(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    order_sn = models.CharField(max_length=255)
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    total_money = models.DecimalField(max_digits=8, decimal_places=2)
    coupon_money = models.DecimalField(max_digits=8, decimal_places=2)
    actual_money = models.DecimalField(max_digits=8, decimal_places=2)
    pay_type = models.IntegerField(default=0)
    source = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    pay_code = models.CharField(max_length=255)

    class Meta:
        db_table = "user_orders"

#专题栏分类表
class Special_category(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    recommend = models.IntegerField(default=0)

    class Meta:
        db_table = "special_category"

#专题表
class Special(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    product_sum = models.IntegerField(default=0)
    recommend = models.IntegerField(default=0)
    content = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    collection_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    class Meta:
        db_table = "special"

#专题图片表
class Special_pic(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    special_id = models.IntegerField()
    pic = models.CharField(max_length=255)

    class Meta:
        db_table = "special_pic"

#优选表
class Super(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=255)

    class Meta:
        db_table = "super"

#帮助/管理表
class Manage(BaseModel,models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        db_table = "manage"



#秒杀时间段
class Ceckil_activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30) #名称
    startTime=models.DateTimeField() #开始时间
    endTime=models.DateTimeField() #结束时间
    status=models.IntegerField() #状态（1是0否）

    class Meta:
        db_table = 'ceckil_activity'


#秒杀活动表
class Quentum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30) #名称
    start_time=models.DateTimeField(max_length=100) #开始时间
    end_time=models.DateTimeField(max_length=100) #结束时间
    is_on = models.IntegerField(default=0)#是否上线


    class Meta:
        db_table = 'quentum'