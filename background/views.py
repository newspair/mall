from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from background.models import *
from django.views import View
#导入json
import json
#导入时间模块
import datetime
import time
#导入django内置的密码库
from django.contrib.auth.hashers import make_password,check_password
from mall import settings
import os

from rest_framework.response import Response

from .serializers import *

from rest_framework.views import APIView

#上传图片
def upload_allimg(img):
    print(img)
    f = open(os.path.join(settings.UPLOAD_ROOT,'',img.name),'wb')
    #写文件 遍历图片文件流
    for chunk in img.chunks():
        f.write(chunk)
        #关闭文件流
    f.close()

class Image(APIView):
    def post(self,request):
        img = request.FILES.get('img')
        upload_allimg(img)
        img_url = 'http://127.0.0.1:8000/upload/'+img.name
        mes = {}
        mes['path'] = img_url
        mes['code'] = 200
        return Response(mes)


class Login(View):
    def get(self,request):
        return JsonResponse({'code':200})
    #   def post(self,request):
    #     #time.sleep(5)
    #     #接收参数
    #     username = request.POST.get('username','未收到username')
    #     password = request.POST.get('password','未收到password')
    #     print(username)
    #     #对秘钥加密
    #     password_hash = make_password(password,'123')

    #     #利用check_password来比对密码
    #     #print(check_password(password,make_password(password,'123')))
    #     print(password_hash)       

    #     #判断用户名和密码
    #     res = User.objects.filter(username=username,password=password_hash).count()
    #     print(res)
        
    #     if res > 0:
    #         #登录成功的逻辑
    #         mes = {}
    #         mes['code'] = 200
    #         response = JsonResponse(mes)
    #         #对中文进行编码
    #         username = bytes(username,'utf-8').decode('ISO-8859-1')
    #         response.set_cookie("username",username,max_age=3600)
    #         response.set_cookie("password",password,max_age=3600)
    #         return response
    #     else:
            #登录失败的逻辑
            

#首页
class L_index(View):
    def get(self,request):
       
        return render(request,'admin/index.html',locals())

#品牌管理
class Shop_guan(APIView):
    def get(self,request):
        id = request.GET.get('id')
        print(id)
    

        if id:
            print('aaaaaaaaaaaaaaaaaa')
            bumen = Brand.objects.filter(id=id).all()
            bumen_serializer = BrandModelSerializer(bumen,many=True)
            mes = {}
            mes['list'] = bumen_serializer.data
            print(mes)
        else:
            # print('bbbbbbbbbbbbbbbbbb')
            sou = request.GET.get('sou','').strip()
            print(type(sou))
            print(sou)
            # 使用模糊查询 加入排序逻辑 倒序
            if sou and sou != 'null' :

                bumen = Brand.objects.filter(name__icontains=sou)
            else:
                bumen = Brand.objects.all()
                print(bumen)

            bumen_serializer = BrandModelSerializer(bumen,many=True)
            mes = {}
            mes['code'] = 200
            mes['brand'] = bumen_serializer.data
            print(mes)
        return Response(mes)

 #品牌管理添加页面
class Brand_detail(APIView):
    def post(self,request):  
        # print(request.data)
        mes = {}
        res = request.GET.get('data')
        print(res)
        brand = BrandSerializer(data=request.data)
        print(brand)
        if brand.is_valid():
            brand.save()
            mes['code'] = 200
        else:
            print(brand.errors)
        return Response(mes)

#品牌管理修改页面
class Brand_detail_edit(APIView):
    def post(self,request):  
        res = request.data
        Brand.objects.filter(id=res['id']).update(name=res['name'],first=res['first'],logo=res['logo'],b_logo=res['b_logo'],story=res['story'],sort=res['sort'],is_show=res['is_show'],is_company=res['is_company'] )

        mes = {}
        mes['code'] = 200
        return Response(mes)



#修改按钮页面页面
class Brand_edit(APIView):
    def post(self,request):  
        res = request.POST.get('ids')
        print(res)
        idc = request.POST.get('idc')
        is_company = request.POST.get('is_company')
        is_show = request.POST.get('is_show')
        idc = request.POST.get('idc')
        print(idc)
        is_nav_status = request.POST.get('is_nav_status')
        is_show = request.POST.get('is_show')
        status = request.POST.get('status')
        print(status)
        # print(is_company)
        if idc:
            if is_nav_status:
                Category.objects.filter(id=idc).update(is_nav_status=is_nav_status)
            else:
                Category.objects.filter(id=idc).update(status=status)
        elif res:
            if is_company:
                Brand.objects.filter(id=res).update(is_company=is_company)
            else:
                Brand.objects.filter(id=res).update(is_show=is_show)
        
        mes = {}
        mes['code'] = 200
        return Response(mes)



#品牌删除方法
class Del_brand(APIView):
    def get(self,request):
        # print(request.data)
        id = request.GET.get('id')
        print(id)
        Brand.objects.filter(id=id).delete()
        mes = {}
        mes['code'] = 200
        return Response(mes,status=None)

#商品分类
class Category_lei(APIView):
    def get(self,request):
        # res = Category.objects.all()
        #  #接受参数
        # searchtitle = request.GET.get('searchtitle','')
        # #清除字符串两边的空格
        # searchtitle = searchtitle.strip()
        # #读库
        # #使用模糊查询 加入排序逻辑 倒序
        # res = Category.objects.filter(name__contains=searchtitle)

        # return render(request,'admin/fenlei.html',locals())
        pid = request.GET.get('pid')
        print(type(pid))
        print(pid)
        mes = {}
        if pid != 'undefined' and pid != None:
              category = Category.objects.filter(parent_id=pid).all()
              print(category)
        else:
            category = Category.objects.filter(level=0).all()
            l_list = []
            for i in category:
                c_dict = i.to_dict()
                print(c_dict)
                cate_to = Category.objects.filter(parent_id=c_dict['id']).all()
                j_list = []
                for j in cate_to:
                    cate_edit = j.to_dict()
                    j_list.append(cate_edit)

                c_dict['children'] = j_list
                l_list.append(c_dict)
                print(l_list)
                mes['list1'] = l_list


        category_serializer = CategoryModelSerializer(category,many=True)
        
        mes['list'] = category_serializer.data
        return Response(mes)


#商品列表展示
class Shop_list(APIView):
    def get(self,request):
        
        shop = Goods.objects.all()
        goods_serializer = CategoryModelSerializer(shop,many=True)
        mes = {}
        mes['mes'] = goods_serializer.data
        return Response(mes)


#商品分类删除方法
class Del_fenlei(APIView):
    def get(self,request):
        id = request.GET.get('id')
        print(id)
        Category.objects.filter(id=id).delete()
        mes = {}
        mes['code'] = 200
        return Response(mes)


#商品类型
class Shop_lei(APIView):
    def get(self,request):
        good_type = Goods_type.objects.all()
        goodtype_serializer = LeixingModelSerializer(good_type,many=True)
        mes = {}
        mes['list'] = goodtype_serializer.data
        return Response(mes)

    def post(self,request):
        mes = {}
        ree= request.data
        # res = request.POST.get('data')
        # print(res)
        res = {}
        res['name'] = ree['name']
        # try:
        #     type1 = Goods_type_attribute.objects.filter(name=res['name']).values('Type')
        #     print(type1)
        #     type1 = type1[0]['Type']
        #     print(type1)
        # except IndexError as e:
        #     print(e)
        # if type1 == 0:
        #     attribute_count = Goods_type_attribute.objects.filter(type_id=t_id.id).count()
        # else:
        #     param_count = Goods_type_attribute.objects.filter(type_id=t_id.id).count()

        # res['attribute_count'] = attribute_count
        # res['param_count'] = param_count
        brand = LeixingSerializer(data=request.data)
        print(brand)
       
        if brand.is_valid():
            brand.save()
            mes['code'] = 200
        else:
            print(brand.errors)
        return Response(mes)

# #商品类型修改
# class Edit_lei(APIView):
#     def post(self,request):
        


#商品类型删除方法
class Del_leixing(APIView):
    def get(self,request):
        id = request.GET.get('id')
        print(type(id))
        ids = int(id)
        print(ids,type(ids))
        try:
            Goods_type.objects.filter(id=int(ids)).delete()
        except Exception as e:
            print(e)
        mes = {}
        mes['code'] = 200
        return Response(mes)


#属性列表
class Shu_xing(APIView):
    def get(self,request):
        
        id = request.GET.get('id')
        cid = request.GET.get('cid')
        print(cid,'*******')
        type = request.GET.get('type')
        print(type,'type')
        mes = {}
        if cid !='undefined' and cid != None:
            
            print(cid,'***********************')
            res = Goods_type_attribute.objects.filter(type_id=cid,Type=type).all()
            

            shuxing_serializer = ShuxingModelSerializer(res,many=True)

            mes['shu'] = shuxing_serializer.data
        else:

             
            res = Goods_type.objects.all()
            

            shuxing_serializer = LeixingModelSerializer(res,many=True)

            mes['shu'] = shuxing_serializer.data
        
        
       
        # mes['list1'] = l_list

        lei = Goods_type.objects.all()

        lei_serializer = LeixingModelSerializer(lei,many=True)
            
        mes['lei'] = lei_serializer.data
        
        
        return Response(mes)


#筛选属性接口
class AttrInfo(APIView):
    def get(self,request):
        mes={}
        id=request.GET.get('id')
        if id:
            pass
        else:
            good = Goods_type.objects.all()
            list1 = []
            for i in good:
                goods_type_dict = i.to_dict()
                print(goods_type_dict)
                goods_type_attribute=Goods_type_attribute.objects.filter(type_id=goods_type_dict['id']).all()
                list2=[]
                for j in goods_type_attribute:
                    attribute_dict=j.to_dict()
                    list2.append(attribute_dict)
                goods_type_dict['productAttributeList']=list2
                list1.append(goods_type_dict)
        mes['list']=list1
        print(mes)
        return Response(mes)

#属性添加页面
class Shu_xing_detail(APIView):
    def post(self,request):
        
        request.data['Type'] = 0
        print(request.data)
        g = Goods_type.objects.filter(id=request.data['type_id']).first()
        if request.data['input_list'] == '':
            del request.data['input_list']

        shuxing_detail = ShuxingSerializer(data=request.data,context={"g": g})
        print(shuxing_detail)
        mes = {}
        if shuxing_detail.is_valid():
            shuxing_detail.save()
            mes['code'] = 200
        else:

            print(shuxing_detail.errors)
            mes['errors'] = 201
        return Response(mes)
            
#属性修改页面
class Shuxing_edit(APIView):
    def post(self,request):
        res = request.data
        print(res)
        Goods_type_attribute.objects.filter(id=res['id']).update(name=res['name'],filter_type=res['filter_type'],is_select=res['is_select'],related_status=res['related_status'],select_type=res['select_type'],input_type=res['input_type'],input_list=res['input_list'],hand_add_status=res['hand_add_status'],sort=res['sort'],Type=res['Type'],type_id=res['type_id'])

        mes = {}
        mes['code'] = 200
        return Response(mes)


#商品分类删除方法
class Del_shuxing(View):
    def post(self,request):
        ids = request.POST.get('ids')
        print(ids,'************************************')
        Goods_type_attribute.objects.filter(id=int(ids)).delete()
        mes = {}
        mes['code'] = 200
        return Response(mes) 

#分类添加
class Fenlei_detail(APIView):
    def post(self,request):
        mes = {}
        data = request.data
        print(data['parent_id'])
        print(type(data['parent_id']))
        if int(data['parent_id'])==0:
            data['level']=0
        else:
            data['level']=1
            print(data,"222222")
        data['productAttributeIdList']=str(data['productAttributeIdList'])
        category = CategorySerializer(data=request.data)
        print(category,'************************')
        if category.is_valid():
            category.save()
            mes['code'] = 200
        else:
            print(category.errors)
            mes['code'] = 201
        return Response(mes)




#秒杀时间段
class Miao_sha(APIView):
    def get(self,request):
        ceckil_activity = Ceckil_activity.objects.all()
        ceckil_serializer = FlashModelSerializer(ceckil_activity,many=True)
        mes = {}
        mes['list'] = ceckil_serializer.data
        return Response(mes)


#秒杀时间段添加
class Add_miaosha(APIView):
    def post(self,request):
        data = request.data
        cid = request.GET.get('cid')
        print(cid,'***************')
        mes = {}
        if cid:
            try:
                Ceckil_activity.objects.filter(id=cid).update(name=data['name'],startTime=data['startTime'],endTime=data['endTime'],status=data['status'])
                mes['code'] = 200
            except Exception as e:
                print(e)
        else:
            
            miaosha = FlashSerializer(data=data)
            # print(miaosha)
            if miaosha.is_valid():
                miaosha.save()
                mes['code'] = 200
            else:
                print(miaosha.errors)
                mes['code'] = 201
        return Response(mes)


#秒杀按钮修改
class Is_show_miao(APIView):
    def post(self,request):  
        res = request.data
        print(res)
        Ceckil_activity.objects.filter(id=res['id']).update(status=res['status'])

        mes = {}
        mes['code'] = 200
        return Response(mes)
        
#秒杀时间段删除方法
class Del_miao(APIView):
    def post(self,request):
        res = request.data
        print(res,'************************************')
        try:
            Ceckil_activity.objects.filter(id=res['id']).delete()
        except Exception as e:
            print(e)
        mes = {}
        mes['code'] = 200
        return Response(mes) 


#秒杀活动
class Miao_huo(APIView):
    def get(self,request):
        quentum = Quentum.objects.all()
        quentum_serializer = QuentumModelSerializer(quentum,many=True)
        mes = {}
        mes['list'] = quentum_serializer.data
        return Response(mes)

# def string_toDatetime(st):
    
#     return datetime.datetime.strptime(st,"%Y-%m-%d %H:%M:%S",time.localtime())

#秒杀活动添加
class Add_miaohuo(APIView):
    def post(self,request):
        data = request.data
        # res = string_toDatetime(data['start_time'])
        # print(type(res))
        cid = request.GET.get('cid')
        print(cid,'---------------------------')
        mes = {}
        if cid:
            try:
                Quentum.objects.filter(id=cid).update(name=data['name'],startTime=data['start_time'],endTime=data['end_time'],is_on=data['is_on'])
                mes['code'] = 200
            except Exception as e:
                print(e)
        else:
            
            miaohuo = QuentumSerializer(data=data)
            # print(miaosha)
            if miaohuo.is_valid():
                miaohuo.save()
                mes['code'] = 200
            else:
                print(miaohuo.errors)
                mes['code'] = 201
        return Response(mes)


#秒杀活动删除方法
class Del_miaohuo(APIView):
    def post(self,request):
        res = request.data
        print(res,'************************************')
        try:
            Quentum.objects.filter(id=res['id']).delete()
        except Exception as e:
            print(e)
        mes = {}
        mes['code'] = 200
        return Response(mes) 

#秒杀活动按钮修改
class Edit_huo(APIView):
    def post(self,request):
        id = request.GET.get('id')
        res = request.data
        print(res)
        Quentum.objects.filter(id=id).update(is_on=res['is_on'])

        mes = {}
        mes['code'] = 200
        return Response(mes)


#秒杀活动
class Youhui(APIView):
    def get(self,request):
        coupon = Coupon.objects.all()
        coupon_serializer = CouponModelSerializer(coupon,many=True)
        mes = {}
        mes['list'] = coupon_serializer.data
        return Response(mes)
















