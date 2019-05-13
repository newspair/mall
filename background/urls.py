from django.contrib import admin
from django.urls import path,re_path
from background.views import *
#导入类视图模板模块
from django.views.generic import TemplateView


urlpatterns = [
   
    #指定渲染登录页面
    path('login',TemplateView.as_view(template_name='admin/login.html')),
    #登陆逻辑
    path('do_login',Login.as_view()),
    #首页
    path('index',L_index.as_view()),
    #品牌管理
    path('brand_list',Shop_guan.as_view()),
    #品牌管理详情页
    path('brand_detail',Brand_detail.as_view()),
    #按钮修改
    path('brand_edit',Brand_edit.as_view()),
    #品牌删除
    path('del_brand',Del_brand.as_view()),
    #商品分类
    path('category',Category_lei.as_view()),
    #分类详情页
    path('fenlei_add',Fenlei_detail.as_view()),
    #商品分类删除方法
    path('del_fenlei',Del_fenlei.as_view()),
    # #查看下级分类
    # path('look',Look.as_view()),
    #商品类型
    path('leixing',Shop_lei.as_view()),
    #商品属性
    path('shuxing',Shu_xing.as_view()),
    #商品属性添加页面
    path('shuxing_detail',Shu_xing_detail.as_view()),
    #商品属性修改页面
    path('shuxing_edit',Shuxing_edit.as_view()),
    #商品类型删除
    path('del_leixing',Del_leixing.as_view()),
    #商品属性删除
    path('del_shuxing',Del_shuxing.as_view()),
    #商品列表
    path('shop_list',Shop_list.as_view()),
    #商品添加
    # path('shop_add',Shop_add.as_view()),
    
    #图片路由
    path('img',Image.as_view()),
    #品牌管理修改页面
    path('brand_detil_edit',Brand_detail_edit.as_view()),
    #秒杀页面
    path('miaosha',Miao_sha.as_view()),
    #秒杀活动添加
    path('add_miaosha',Add_miaosha.as_view()),
    #秒杀活动按钮
    path('is_show_miao',Is_show_miao.as_view()),
    #删除秒杀时间段
    path('del_miao',Del_miao.as_view()),
    #秒杀活动
    path('miaohuo',Miao_huo.as_view()),
    #秒杀活动添加
    path('add_miaohuo',Add_miaohuo.as_view()),
    #秒杀活动删除
    path('del_miaohuo',Del_miaohuo.as_view()),
    #秒杀活动按钮
    path('edit_huo',Edit_huo.as_view()),
    #筛选属性接口
    path('shaixuan',AttrInfo.as_view())
]