import json

from django.contrib import auth
from django.core import serializers
from django.shortcuts import render, redirect
from django.views import View

from app01 import models


# =========Class Based View==================
class AddPublisher(View):
    def get(self, request):
        return render(request, 'old/add_publisher.html')

    def post(self, request):
        new_name = request.POST.get('publisher_name', None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        error_msg = '出版社名字不能为空'
        return render(request, 'old/add_publisher.html', {'error_msg': error_msg})


# class add_rule_search_Feature_para(View):
#     @method_decorator(ensure_csrf_cookie)
#     def get(self, request):
#         return render(request, 'old/add_ManuCapRule.html')
#
#     def post(self, request, featType):
#         all_Feature_obj = models.Feature.objects.filter(classSecond__icontains=featType).all()
#         error_msg = ''
#         return render(request, 'old/add_ManuCapRule.html', {'FeaturePara_list': all_Feature_obj})

# class FeaturePara:
#     ParaDes = ''
#     ParaName=''
def add_rule_search_Feature_para(request):
    featype = request.POST.get('featype')
    all_Feature_obj = models.Feature.objects.filter(classSecond__icontains=featype).first()
    error_msg = ''
    json_str = all_Feature_obj.paraDef
    # JSON解析
    data = json.loads(json_str)
    # print(data)
    # for para in data:

    return render(request, 'old/search_Feature.html', {'FeaturePara_list': data})


# =========Function Based View==================
def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'old/publisher_list.html', {'publisher_list': ret})


def add_publisher(request):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name', None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        error_msg = '出版社名字不能为空'
    return render(request, 'old/add_publisher.html', {'error': error_msg})


def delete_publisher(request, del_id):
    if del_id:
        models.Publisher.objects.get(id=del_id).delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('要删除的数据不存在')


def edit_publisher(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name')
        if new_name:
            edit_pub = models.Publisher.objects.get(id=edit_id)
            edit_pub.name = new_name
            edit_pub.save()
            return redirect('/publisher_list/')
        else:
            error_msg = '出版社名不能为空'
    publisher_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'old/edit_publisher.html', {'publisher': publisher_obj, 'error_msg': error_msg})


def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, 'old/book_list.html', {'books': all_book})


def add_book(request):
    error_msg = ''
    ret = models.Publisher.objects.all()
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        if new_title:
            select_publisher_id = request.POST.get('publisher')
            models.Book.objects.create(title=new_title, publisher_id=select_publisher_id)
            return redirect('/book_list/')
        else:
            error_msg = '书名不能为空'
    return render(request, 'old/add_book.html', {'publisher_list': ret, 'error_msg': error_msg})


def delete_book(request, del_id):
    models.Book.objects.get(id=del_id).delete()
    return redirect('/book_list/')


def edit_book(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        if new_title:
            new_publisher_id = request.POST.get('publisher')
            edit_book_obj = models.Book.objects.get(id=edit_id)
            edit_book_obj.title = new_title
            edit_book_obj.publisher_id = new_publisher_id
            edit_book_obj.save()
            return redirect('/book_list/')
        else:
            error_msg = '书名不能为空'
    edit_book_obj = models.Book.objects.get(id=edit_id)
    publisher_list = models.Publisher.objects.all()
    return render(request, 'old/edit_book.html',
                  {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj, 'error_msg': error_msg})


def add_author(request):
    error_msg = ''
    if request.method == 'POST':
        new_author = request.POST.get('author_name')
        if new_author:
            books = request.POST.getlist('books')  # POST提交的数据是多个值，如多选框，需要用getlist
            new_author_obj = models.Author.objects.create(name=new_author)
            new_author_obj.book.set(books)
            return redirect('/author_list/')
        else:
            error_msg = '作者姓名不能为空'
    books = models.Book.objects.all()
    return render(request, 'old/add_author.html', {'books': books, 'error_msg': error_msg})


def delete_author(request, del_id):
    models.Author.objects.get(id=del_id).delete()
    return redirect('/author_list/')


def edit_author(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        if new_author_name:
            books = request.POST.getlist('books')
            edit_author_obj = models.Author.objects.get(id=edit_id)
            edit_author_obj.name = new_author_name
            edit_author_obj.book.set(books)
            edit_author_obj.save()
            return redirect('/author_list/')
        else:
            error_msg = '作者姓名不能为空'
    edit_author_obj = models.Author.objects.get(id=edit_id)
    books = models.Book.objects.all()
    return render(request, 'old/edit_author.html',
                  {'edit_author_obj': edit_author_obj, 'books': books, 'error_msg': error_msg})


def cutter_list(request):
    all_cutter = models.Cutter.objects.all()
    return render(request, 'standard_knowledge_and_information/resource.html', {'cutter_list': all_cutter})


def add_cutter(request):
    error_msg = ''
    if request.method == 'POST':
        new_cutter = request.POST.get('cutter_name')
        if new_cutter:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_cutter_obj = models.Cutter.objects.create(name=new_cutter, supplier=request.POST.get('cutter_supplier'),
                                                          minHoleTole=request.POST.get('cutter_minHoleTole'),
                                                          maxHoleTole=request.POST.get('cutter_maxHoleTole'),
                                                          minDia=request.POST.get('cutter_minDia'),
                                                          maxDia=request.POST.get('cutter_maxDia'),
                                                          minDepDia=request.POST.get('cutter_minDepDia'),
                                                          maxDepDia=request.POST.get('cutter_maxDepDia'),
                                                          capMat=request.POST.get('cutter_capMat'),
                                                          cutterMat=request.POST.get('cutter_cutterMat'),
                                                          capPro=request.POST.get('cutter_capPro'),
                                                          cutterCost=request.POST.get('cutter_cutterCost'),
                                                          cutterImg=request.FILES.get('cutter_cutterImg_file'),
                                                          cutterRemark=request.POST.get('cutter_cutterRemark')
                                                          )

            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '刀具名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_cutter.html', {'error_msg': error_msg})


def delete_cutter(request, del_id):
    models.Cutter.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/resource/')


def edit_cutter(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('cutter_name')
        if new_name:
            edit_cutter_obj = models.Cutter.objects.get(id=edit_id)
            edit_cutter_obj.name = new_name
            edit_cutter_obj.supplier = request.POST.get('cutter_supplier')
            edit_cutter_obj.minHoleTole = request.POST.get('cutter_minHoleTole')
            edit_cutter_obj.maxHoleTole = request.POST.get('cutter_maxHoleTole')
            edit_cutter_obj.minDia = request.POST.get('cutter_minDia')
            edit_cutter_obj.maxDia = request.POST.get('cutter_maxDia')
            edit_cutter_obj.minDepDia = request.POST.get('cutter_minDepDia')
            edit_cutter_obj.maxDepDia = request.POST.get('cutter_maxDepDia')
            edit_cutter_obj.capMat = request.POST.get('cutter_capMat')
            edit_cutter_obj.cutterMat = request.POST.get('cutter_cutterMat')
            edit_cutter_obj.capPro = request.POST.get('cutter_capPro')
            edit_cutter_obj.cutterCost = request.POST.get('cutter_cutterCost')
            edit_cutter_obj.cutterImg = request.FILES.get('cutter_cutterImg_file')
            edit_cutter_obj.cutterRemark = request.POST.get('cutter_cutterRemark')
            edit_cutter_obj.save()
            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '刀具名不能为空'
    cutter_obj = models.Cutter.objects.get(id=edit_id)
    return render(request, 'old/edit_cutter.html', {'cutter': cutter_obj, 'error_msg': error_msg})


def search_cutter(request):
    search = request.GET.get('cutter_search')
    all_cutter_obj = models.Cutter.objects.filter(name__icontains=search).all()
    error_msg = ''
    tab_name = 'tool'
    return render(request, 'standard_knowledge_and_information/resource.html',
                  {'cutter_list': all_cutter_obj, 'tab_name': tab_name})


# About fixtures
def fixture_list(request):
    all_fixture = models.Fixture.objects.all()
    return render(request, 'standard_knowledge_and_information/resource.html', {'fixture_list': all_fixture})


def add_fixture(request):
    error_msg = ''
    if request.method == 'POST':
        new_fixture = request.POST.get('fixture_name')
        if new_fixture:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_fixture_obj = models.Fixture.objects.create(name=new_fixture,
                                                            fixtureType=request.POST.get('fixture_fixtureType'),
                                                            fixtureName=request.POST.get('fixture_fixtureName'),
                                                            fixtureCode=request.POST.get('fixture_fixtureCode'),
                                                            geoDim=request.POST.get('fixture_geoDim'),
                                                            partType=request.POST.get('fixture_partType'),
                                                            partStruct=request.POST.get('fixture_partStruct'),
                                                            partMat=request.POST.get('fixture_partMat'),
                                                            partSize=request.POST.get('fixture_partSize'),
                                                            InterfaceDim=request.POST.get('fixture_InterfaceDim'),
                                                            fixtureImg=request.FILES.get('fixture_fixtureImg'),
                                                            fixtureRemark=request.POST.get('fixture_fixtureRemark'),
                                                            otherFields=request.POST.get('fixture_otherFields'),
                                                            )

            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '工装名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_fixture.html', {'error_msg': error_msg})


def delete_fixture(request, del_id):
    models.Fixture.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/resource/')


def edit_fixture(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('fixture_name')
        if new_name:
            edit_fixture_obj = models.Fixture.objects.get(id=edit_id)
            edit_fixture_obj.name = new_name
            edit_fixture_obj.fixtureType = request.POST.get('fixture_fixtureType')
            edit_fixture_obj.fixtureName = request.POST.get('fixture_fixtureName')
            edit_fixture_obj.fixtureCode = request.POST.get('fixture_fixtureCode')
            edit_fixture_obj.geoDim = request.POST.get('fixture_geoDim')
            edit_fixture_obj.partType = request.POST.get('fixture_partType')
            edit_fixture_obj.partStruct = request.POST.get('fixture_partStruct')
            edit_fixture_obj.partMat = request.POST.get('fixture_partMat')
            edit_fixture_obj.partSize = request.POST.get('fixture_partSize')
            edit_fixture_obj.InterfaceDim = request.POST.get('fixture_InterfaceDim')
            edit_fixture_obj.fixtureImg = request.FILES.get('fixture_fixtureImg')
            edit_fixture_obj.fixtureRemark = request.POST.get('fixture_fixtureRemark')
            edit_fixture_obj.otherFields = request.POST.get('fixture_otherFields')
            edit_fixture_obj.save()
            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '工装名不能为空'
    fixture_obj = models.Fixture.objects.get(id=edit_id)
    return render(request, 'old/edit_fixture.html', {'fixture': fixture_obj, 'error_msg': error_msg})


def search_fixture(request):
    search = request.GET.get('fixture_search')
    all_fixture_obj = models.Fixture.objects.filter(name__icontains=search).all()
    error_msg = ''
    tab_name = 'fixture'
    return render(request, 'standard_knowledge_and_information/resource.html',
                  {'fixture_list': all_fixture_obj, "tab_name": tab_name})


# Mach
def mach_list(request):
    all_mach = models.Mach.objects.all()
    return render(request, 'standard_knowledge_and_information/resource.html', {'mach_list': all_mach})


def add_mach(request):
    error_msg = ''
    if request.method == 'POST':
        new_mach = request.POST.get('mach_name')
        if new_mach:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_mach_obj = models.Mach.objects.create(name=new_mach,
                                                      machType=request.POST.get('mach_machType'),
                                                      travelX=request.POST.get('mach_travelX'),
                                                      travelY=request.POST.get('mach_travelY'),
                                                      travelZ=request.POST.get('mach_travelZ'),
                                                      travelA=request.POST.get('mach_travelA'),
                                                      travelB=request.POST.get('mach_travelB'),
                                                      travelC=request.POST.get('mach_travelC'),
                                                      PrecisionX=request.POST.get('mach_PrecisionX'),
                                                      PrecisionY=request.POST.get('mach_PrecisionY'),
                                                      PrecisionZ=request.POST.get('mach_PrecisionZ'),
                                                      PrecisionA=request.POST.get('mach_PrecisionA'),
                                                      PrecisionB=request.POST.get('mach_PrecisionB'),
                                                      PrecisionC=request.POST.get('mach_PrecisionC'),
                                                      worktableSize_length=request.POST.get(
                                                          'mach_worktableSize_length'),
                                                      worktableSize_width=request.POST.get('mach_worktableSize_width'),
                                                      load=request.POST.get('mach_load'),
                                                      process=request.POST.get('mach_process'),
                                                      feature=request.POST.get('mach_feature'),
                                                      headID=request.POST.get('mach_headID'),
                                                      machImg=request.FILES.get('mach_machImg'),
                                                      machRemark=request.POST.get('mach_machRemark'),
                                                      otherFields=request.POST.get('mach_otherFields'),
                                                      )

            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '机床名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_mach.html', {'error_msg': error_msg})


def delete_mach(request, del_id):
    models.Mach.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/resource/')


def edit_mach(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('mach_name')
        if new_name:
            edit_mach_obj = models.Mach.objects.get(id=edit_id)
            edit_mach_obj.name = new_name
            edit_mach_obj.machType = request.POST.get('mach_machType')
            edit_mach_obj.travelX = request.POST.get('mach_travelX')
            edit_mach_obj.travelY = request.POST.get('mach_travelY')
            edit_mach_obj.travelZ = request.POST.get('mach_travelZ')
            edit_mach_obj.travelA = request.POST.get('mach_travelA')
            edit_mach_obj.travelB = request.POST.get('mach_travelB')
            edit_mach_obj.travelC = request.POST.get('mach_travelC')
            edit_mach_obj.PrecisionX = request.POST.get('mach_PrecisionX')
            edit_mach_obj.PrecisionY = request.POST.get('mach_PrecisionY')
            edit_mach_obj.PrecisionZ = request.POST.get('mach_PrecisionZ')
            edit_mach_obj.PrecisionA = request.POST.get('mach_PrecisionA')
            edit_mach_obj.PrecisionB = request.POST.get('mach_PrecisionB')
            edit_mach_obj.PrecisionC = request.POST.get('mach_PrecisionC')
            edit_mach_obj.worktableSize_length = request.POST.get('mach_worktableSize_length')
            edit_mach_obj.worktableSize_width = request.POST.get('mach_worktableSize_width')
            edit_mach_obj.load = request.POST.get('mach_load')
            edit_mach_obj.process = request.POST.get('mach_process')
            edit_mach_obj.feature = request.POST.get('mach_feature')
            edit_mach_obj.headID = request.POST.get('mach_headID')
            edit_mach_obj.machImg = request.FILES.get('mach_machImg')
            edit_mach_obj.machRemark = request.POST.get('mach_machRemark')
            edit_mach_obj.otherFields = request.POST.get('mach_otherFields')
            edit_mach_obj.save()
            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '机床名不能为空'
    mach_obj = models.Mach.objects.get(id=edit_id)
    return render(request, 'old/edit_mach.html', {'mach': mach_obj, 'error_msg': error_msg})


def search_mach(request):
    search = request.GET.get('mach_search')
    all_mach_obj = models.Mach.objects.filter(name__icontains=search).all()
    error_msg = ''
    tab_name = 'mach'
    return render(request, 'standard_knowledge_and_information/resource.html',
                  {'mach_list': all_mach_obj, "tab_name": tab_name})


# Head

def head_list(request):
    all_head = models.Head.objects.all()
    return render(request, 'standard_knowledge_and_information/resource.html', {'head_list': all_head})


def add_head(request):
    error_msg = ''
    if request.method == 'POST':
        new_head = request.POST.get('head_name')
        if new_head:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_head_obj = models.Head.objects.create(name=new_head,
                                                      headType=request.POST.get('head_headType'),
                                                      headStruct=request.POST.get('head_headStruct'),
                                                      headDepth=request.POST.get('head_headDepth'),
                                                      toolDiamRange_max=request.POST.get('head_toolDiamRange_max'),
                                                      toolDiamRange_min=request.POST.get('head_toolDiamRange_min'),
                                                      appMach=request.POST.get('head_appMach'),
                                                      headImg=request.FILES.get('head_headImg'),
                                                      headRemark=request.POST.get('head_headRemark'),
                                                      otherFields=request.POST.get('head_otherFields'),
                                                      )

            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '角度头名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_head.html', {'error_msg': error_msg})


def delete_head(request, del_id):
    models.Head.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/resource/')


def edit_head(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('head_name')
        if new_name:
            edit_head_obj = models.Head.objects.get(id=edit_id)
            edit_head_obj.name = new_name
            edit_head_obj.headType = request.POST.get('head_headType')
            edit_head_obj.headStruct = request.POST.get('head_headStruct')
            edit_head_obj.headDepth = request.POST.get('head_headDepth')
            edit_head_obj.toolDiamRange_max = request.POST.get('head_toolDiamRange_max')
            edit_head_obj.toolDiamRange_min = request.POST.get('head_toolDiamRange_min')
            edit_head_obj.appMach = request.POST.get('head_appMach')
            edit_head_obj.headImg = request.FILES.get('head_headImg')
            edit_head_obj.headRemark = request.POST.get('head_headRemark')
            edit_head_obj.otherFields = request.POST.get('head_otherFields')
            edit_head_obj.save()
            return redirect('/standardKnowNInfo/resource/')
        else:
            error_msg = '角度头名不能为空'
    head_obj = models.Head.objects.get(id=edit_id)
    return render(request, 'old/edit_head.html', {'head': head_obj, 'error_msg': error_msg})


def search_head(request):
    search = request.GET.get('head_search')
    all_head_obj = models.Head.objects.filter(name__icontains=search).all()
    error_msg = ''
    tab_name = 'head'
    return render(request, 'standard_knowledge_and_information/resource.html',
                  {'head_list': all_head_obj, "tab_name": tab_name})


# Apert 标准孔

def apert_list(request):
    all_apert = models.Apert.objects.all()
    return render(request, 'standard_knowledge_and_information/standardize.html', {'apert_list': all_apert})


def add_apert(request):
    error_msg = ''
    if request.method == 'POST':
        new_apert = request.POST.get('apert_apertType')
        if new_apert:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_apert_obj = models.Apert.objects.create(
                apertType=new_apert,
                standard_apert=request.POST.get('apert_standard_apert'),
                apertImg=request.FILES.get('apert_apertImg'),
                excel_apertfile=request.FILES.get('apert_excel_apertfile'),
                apertRemark=request.POST.get('apert_apertRemark'),
                otherFields=request.POST.get('apert_otherFields'),
            )

            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '孔名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_apert.html', {'error_msg': error_msg})


def delete_apert(request, del_id):
    models.Apert.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardize/')


def edit_apert(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('apert_apertType')
        if new_name:
            edit_apert_obj = models.Apert.objects.get(id=edit_id)
            edit_apert_obj.apertType = new_name
            edit_apert_obj.standard_apert = request.POST.get('apert_standard_apert')
            edit_apert_obj.apertImg = request.FILES.get('apert_apertImg')
            edit_apert_obj.excel_apertfile = request.FILES.get('apert_excel_apertfile')
            edit_apert_obj.apertRemark = request.POST.get('apert_apertRemark')
            edit_apert_obj.otherFields = request.POST.get('apert_otherFields')
            edit_apert_obj.save()
            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '孔名称不能为空'
    apert_obj = models.Apert.objects.get(id=edit_id)
    return render(request, 'old/edit_apert.html', {'apert': apert_obj, 'error_msg': error_msg})


def search_apert(request):
    search = request.GET.get('apert_search')
    all_apert_obj = models.Apert.objects.filter(apertType__icontains=search).all()
    error_msg = ''
    tab_name = 'apert'
    return render(request, 'standard_knowledge_and_information/standardize.html',
                  {'apert_list': all_apert_obj, "tab_name": tab_name})


# 下载apert excel文件
# views.py
from django.http import HttpResponse

import os


def download_excel(request, apert_id):
    print('1')
    try:
        apert = models.Apert.objects.get(id=apert_id)
        excel_file_path = apert.excel_apertfile.path

        if os.path.exists(excel_file_path) and os.path.isfile(excel_file_path):
            with open(excel_file_path, 'rb') as excel_file:
                response = HttpResponse(excel_file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(excel_file_path)}"'
                return response

    except models.Apert.DoesNotExist:
        print('文件不存在')
        pass

    # If the Apert object does not exist or the file is not found, return a 404 Not Found response.
    return HttpResponse(status=404)


# basic Precision 基本偏差表

def precision_list(request):
    all_precision = models.Precision.objects.all()
    return render(request, 'standard_knowledge_and_information/standardize.html', {'precision_list': all_precision})


def add_precision(request):
    error_msg = ''
    if request.method == 'POST':
        new_precision = request.POST.get('precision_basic')
        if new_precision:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_precision_obj = models.Precision.objects.create(
                basic=new_precision,
                nomiSizeL=request.POST.get('precision_nomiSizeL'),
                nomiSizeR=request.POST.get('precision_nomiSizeR'),
                tolGrade=request.POST.get('precision_tolGrade'),
                basicDevNum=request.POST.get('precision_basicDevNum'),
                otherField1=request.POST.get('precision_otherField1'),
                otherField2=request.POST.get('precision_otherField2'),
            )

            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '基准名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_precision.html', {'error_msg': error_msg})


def delete_precision(request, del_id):
    models.Precision.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardize/')


def edit_precision(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('precision_basic')
        if new_name:
            edit_precision_obj = models.Precision.objects.get(id=edit_id)
            edit_precision_obj.basic = new_name
            edit_precision_obj.nomiSizeL = request.POST.get('precision_nomiSizeL')
            edit_precision_obj.nomiSizeR = request.POST.get('precision_nomiSizeR')
            edit_precision_obj.tolGrade = request.POST.get('precision_tolGrade')
            edit_precision_obj.basicDevNum = request.POST.get('precision_basicDevNum')
            edit_precision_obj.otherField1 = request.POST.get('precision_otherField1')
            edit_precision_obj.otherField2 = request.POST.get('precision_otherField2')
            edit_precision_obj.save()
            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '基准名称不能为空'
    precision_obj = models.Precision.objects.get(id=edit_id)
    return render(request, 'old/edit_precision.html', {'precision': precision_obj, 'error_msg': error_msg})


def search_precision(request):
    search = request.GET.get('precision_search')
    all_precision_obj = models.Precision.objects.filter(basic__icontains=search).all()
    error_msg = ''
    tab_name = 'precision'
    return render(request, 'standard_knowledge_and_information/standardize.html',
                  {'precision_list': all_precision_obj, "tab_name": tab_name})


# FitTolerance
def fitTolerance_list(request):
    all_fitTolerance = models.FitTolerance.objects.all()
    return render(request, 'standard_knowledge_and_information/standardize.html',
                  {'fitTolerance_list': all_fitTolerance})


def add_fitTolerance(request):
    error_msg = ''
    if request.method == 'POST':
        new_fitTolerance = request.POST.get('fitTolerance_Class')
        if new_fitTolerance:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.FitTolerance.objects.create(
                Class=new_fitTolerance,
                nomiSizeL=request.POST.get('fitTolerance_nomiSizeL'),
                nomiSizeR=request.POST.get('fitTolerance_nomiSizeR'),
                tolNum=request.POST.get('fitTolerance_tolNum'),
                otherField1=request.POST.get('fitTolerance_otherField1'),
                otherField2=request.POST.get('fitTolerance_otherField2'),
            )

            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '精度等级不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_fitTolerance.html', {'error_msg': error_msg})


def delete_fitTolerance(request, del_id):
    models.FitTolerance.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardize/')


def edit_fitTolerance(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('fitTolerance_Class')
        if new_name:
            edit_fitTolerance_obj = models.FitTolerance.objects.get(id=edit_id)
            edit_fitTolerance_obj.Class = new_name
            edit_fitTolerance_obj.nomiSizeL = request.POST.get('fitTolerance_nomiSizeL')
            edit_fitTolerance_obj.nomiSizeR = request.POST.get('fitTolerance_nomiSizeR')
            edit_fitTolerance_obj.tolNum = request.POST.get('fitTolerance_tolNum')
            edit_fitTolerance_obj.otherField1 = request.POST.get('fitTolerance_otherField1')
            edit_fitTolerance_obj.otherField2 = request.POST.get('fitTolerance_otherField2')
            edit_fitTolerance_obj.save()
            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '精度等级不能为空'
    fitTolerance_obj = models.FitTolerance.objects.get(id=edit_id)
    return render(request, 'old/edit_fitTolerance.html', {'fitTolerance': fitTolerance_obj, 'error_msg': error_msg})


def search_fitTolerance(request):
    search = request.GET.get('fitTolerance_search')
    all_fitTolerance_obj = models.FitTolerance.objects.filter(Class__icontains=search).all()
    error_msg = ''
    tab_name = 'fitTolerance'
    return render(request, 'standard_knowledge_and_information/standardize.html',
                  {'fitTolerance_list': all_fitTolerance_obj, "tab_name": tab_name})


# Prio
def prio_list(request):
    all_prio = models.Prio.objects.all()
    return render(request, 'standard_knowledge_and_information/standardize.html', {'prio_list': all_prio})


def add_prio(request):
    error_msg = ''
    if request.method == 'POST':
        new_prio = request.POST.get('prio_basic')
        if new_prio:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.Prio.objects.create(
                basic=new_prio,
                holeTol=request.POST.get('prio_holeTol'),
                shaftTol=request.POST.get('prio_shaftTol'),
                fitType=request.POST.get('prio_fitType'),
                otherField1=request.POST.get('prio_otherField1'),
                otherField2=request.POST.get('prio_otherField2'),
            )

            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '基准不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_prio.html', {'error_msg': error_msg})


def delete_prio(request, del_id):
    models.Prio.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardize/')


def edit_prio(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('prio_basic')
        if new_name:
            edit_prio_obj = models.Prio.objects.get(id=edit_id)
            edit_prio_obj.basic = new_name
            edit_prio_obj.holeTol = request.POST.get('prio_holeTol')
            edit_prio_obj.shaftTol = request.POST.get('prio_shaftTol')
            edit_prio_obj.fitType = request.POST.get('prio_fitType')
            edit_prio_obj.otherField1 = request.POST.get('prio_otherField1')
            edit_prio_obj.otherField2 = request.POST.get('prio_otherField2')
            edit_prio_obj.save()
            return redirect('/standardKnowNInfo/standardize/')
        else:
            error_msg = '基准不能为空'
    prio_obj = models.Prio.objects.get(id=edit_id)
    return render(request, 'old/edit_prio.html', {'prio': prio_obj, 'error_msg': error_msg})


def search_prio(request):
    search = request.GET.get('prio_search')
    all_prio_obj = models.Prio.objects.filter(basic__icontains=search).all()
    error_msg = ''
    tab_name = 'prio'
    return render(request, 'standard_knowledge_and_information/standardize.html',
                  {'prio_list': all_prio_obj, "tab_name": tab_name})


# Part
def part_list(request):
    all_part = models.Part.objects.all()
    return render(request, 'standard_knowledge_and_information/standard_process.html', {'part_list': all_part})


def add_part(request):
    error_msg = ''
    if request.method == 'POST':
        new_part = request.POST.get('part_partType')
        if new_part:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.Part.objects.create(
                partType=new_part,
                partStruct=request.POST.get('part_partStruct'),
                partMat=request.POST.get('part_partMat'),
                partSize=request.POST.get('part_partSize'),
                geoFix=request.POST.get('part_geoFix'),
                PMIInfo=request.POST.get('part_PMIInfo'),
                featType=request.POST.get('part_featType'),
                processFlow=request.POST.get('part_processFlow'),
                Img=request.FILES.get('part_Img'),
                otherField1=request.POST.get('part_otherField1'),
                otherField2=request.POST.get('part_otherField2'),
            )

            return redirect('/standardKnowNInfo/standardProcess/')
        else:
            error_msg = '零件类型不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_part.html', {'error_msg': error_msg})


def delete_part(request, del_id):
    models.Part.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardProcess/')


def edit_part(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('part_partType')
        if new_name:
            edit_part_obj = models.Part.objects.get(id=edit_id)
            edit_part_obj.partType = new_name
            edit_part_obj.partStruct = request.POST.get('part_partStruct')
            edit_part_obj.partMat = request.POST.get('part_partMat')
            edit_part_obj.partSize = request.POST.get('part_partSize')
            edit_part_obj.geoFix = request.POST.get('part_geoFix')
            edit_part_obj.PMIInfo = request.POST.get('part_PMIInfo')
            edit_part_obj.featType = request.POST.get('part_featType')
            edit_part_obj.processFlow = request.POST.get('part_processFlow')
            edit_part_obj.Img = request.FILES.get('part_Img')
            edit_part_obj.otherField1 = request.POST.get('part_otherField1')
            edit_part_obj.otherField2 = request.POST.get('part_otherField2')
            edit_part_obj.save()
            return redirect('/standardKnowNInfo/standardProcess/')
        else:
            error_msg = '零件类型不能为空'
    part_obj = models.Part.objects.get(id=edit_id)
    return render(request, 'old/edit_part.html', {'part': part_obj, 'error_msg': error_msg})


def search_part(request):
    search = request.GET.get('part_search')
    all_part_obj = models.Part.objects.filter(partType__icontains=search).all()
    error_msg = ''
    tab_name = 'part'
    return render(request, 'standard_knowledge_and_information/standard_process.html',
                  {'part_list': all_part_obj, "tab_name": tab_name})


# Feat

def feat_list(request):
    all_feat = models.Feat.objects.all()
    return render(request, 'standard_knowledge_and_information/standard_process.html', {'feat_list': all_feat})


def add_feat(request):
    error_msg = ''
    if request.method == 'POST':
        new_feat = request.POST.get('feat_featID')
        if new_feat:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.Feat.objects.create(
                featID=new_feat,
                featType=request.POST.get('feat_featType'),
                featMat=request.POST.get('feat_featMat'),
                geoDim=request.POST.get('feat_geoDim'),
                precision=request.POST.get('feat_precision'),
                processFlow=request.POST.get('feat_processFlow'),
                Img=request.FILES.get('feat_Img'),
                otherField1=request.POST.get('feat_otherField1'),
                otherField2=request.POST.get('feat_otherField2'),
            )

            return redirect('/standardKnowNInfo/standardProcess/')
        else:
            error_msg = '关联的特征不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_feat.html', {'error_msg': error_msg})


def delete_feat(request, del_id):
    models.Feat.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardProcess/')


def edit_feat(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('feat_featID')
        if new_name:
            edit_feat_obj = models.Feat.objects.get(id=edit_id)
            edit_feat_obj.featID = new_name
            edit_feat_obj.featType = request.POST.get('feat_featType')
            edit_feat_obj.featMat = request.POST.get('feat_featMat')
            edit_feat_obj.geoDim = request.POST.get('feat_geoDim')
            edit_feat_obj.precision = request.POST.get('feat_precision')
            edit_feat_obj.processFlow = request.POST.get('feat_processFlow')
            edit_feat_obj.Img = request.FILES.get('feat_Img')
            edit_feat_obj.otherField1 = request.POST.get('feat_otherField1')
            edit_feat_obj.otherField2 = request.POST.get('feat_otherField2')
            edit_feat_obj.save()
            return redirect('/standardKnowNInfo/standardProcess/')
        else:
            error_msg = '关联的特征不能为空'
    feat_obj = models.Feat.objects.get(id=edit_id)
    return render(request, 'old/edit_feat.html', {'feat': feat_obj, 'error_msg': error_msg})


def search_feat(request):
    search = request.GET.get('feat_search')
    all_feat_obj = models.Feat.objects.filter(featID__icontains=search).all()
    error_msg = ''
    tab_name = 'feat'
    return render(request, 'standard_knowledge_and_information/standard_process.html',
                  {'feat_list': all_feat_obj, "tab_name": tab_name})


# MaterialDesignation

def materialDesignation_list(request):
    all_materialDesignation = models.MaterialDesignation.objects.all()
    return render(request, 'standard_knowledge_and_information/material.html',
                  {'materialDesignation_list': all_materialDesignation})


def add_materialDesignation(request):
    error_msg = ''
    if request.method == 'POST':
        new_materialDesignation = request.POST.get('materialDesignation_GBName')
        if new_materialDesignation:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.MaterialDesignation.objects.create(
                GBName=new_materialDesignation,
                matType1=request.POST.get('materialDesignation_matType1'),
                matType2=request.POST.get('materialDesignation_matType2'),
                matName=request.POST.get('materialDesignation_matName'),
                ASTM=request.POST.get('materialDesignation_ASTM'),
                SAE=request.POST.get('materialDesignation_SAE'),
                desc=request.POST.get('materialDesignation_desc'),
                Img=request.FILES.get('materialDesignation_Img'),
                otherField1=request.POST.get('materialDesignation_otherField1'),
                otherField2=request.POST.get('materialDesignation_otherField2'),
            )

            return redirect('/standardKnowNInfo/material/')
        else:
            error_msg = '材料名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_materialDesignation.html', {'error_msg': error_msg})


def delete_materialDesignation(request, del_id):
    models.MaterialDesignation.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/material/')


def edit_materialDesignation(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('materialDesignation_GBName')
        if new_name:
            edit_materialDesignation_obj = models.MaterialDesignation.objects.get(id=edit_id)
            edit_materialDesignation_obj.GBName = new_name
            edit_materialDesignation_obj.matType1 = request.POST.get('materialDesignation_matType1')
            edit_materialDesignation_obj.matType2 = request.POST.get('materialDesignation_matType2')
            edit_materialDesignation_obj.matName = request.POST.get('materialDesignation_matName')
            edit_materialDesignation_obj.ASTM = request.POST.get('materialDesignation_ASTM')
            edit_materialDesignation_obj.SAE = request.POST.get('materialDesignation_SAE')
            edit_materialDesignation_obj.desc = request.POST.get('materialDesignation_desc')
            edit_materialDesignation_obj.Img = request.FILES.get('materialDesignation_Img')
            edit_materialDesignation_obj.otherField1 = request.POST.get('materialDesignation_otherField1')
            edit_materialDesignation_obj.otherField2 = request.POST.get('materialDesignation_otherField2')
            edit_materialDesignation_obj.save()
            return redirect('/standardKnowNInfo/material/')
        else:
            error_msg = '材料名称不能为空'
    materialDesignation_obj = models.MaterialDesignation.objects.get(id=edit_id)
    return render(request, 'old/edit_materialDesignation.html',
                  {'materialDesignation': materialDesignation_obj, 'error_msg': error_msg})


def search_materialDesignation(request):
    search = request.GET.get('materialDesignation_search')
    all_materialDesignation_obj = models.MaterialDesignation.objects.filter(GBName__icontains=search).all()
    error_msg = ''
    tab_name = 'materialDesignation'
    return render(request, 'standard_knowledge_and_information/material.html',
                  {'materialDesignation_list': all_materialDesignation_obj, "tab_name": tab_name})


# MaterialMachinability

def materialMachinability_list(request):
    all_materialMachinability = models.MaterialMachinability.objects.all()
    return render(request, 'standard_knowledge_and_information/material.html',
                  {'materialMachinability_list': all_materialMachinability})


def add_materialMachinability(request):
    error_msg = ''
    if request.method == 'POST':
        new_materialMachinability = request.POST.get('materialMachinability_materialName')
        if new_materialMachinability:
            # img_file=request.FILES.get('cutter_cutterImg')
            new_new_fitTolerance_obj = models.MaterialMachinability.objects.create(
                materialName=new_materialMachinability,
                Strength=request.POST.get('materialMachinability_Strength'),
                hardness=request.POST.get('materialMachinability_hardness'),
                therConduct=request.POST.get('materialMachinability_therConduct'),
                hardening=request.POST.get('materialMachinability_hardening'),
                affinity=request.POST.get('materialMachinability_affinity'),
                otherField1=request.POST.get('materialMachinability_otherField1'),
                otherField2=request.POST.get('materialMachinability_otherField2'),
            )

            return redirect('/standardKnowNInfo/material/')
        else:
            error_msg = '材料名称不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_materialMachinability.html', {'error_msg': error_msg})


def delete_materialMachinability(request, del_id):
    models.MaterialMachinability.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/material/')


def edit_materialMachinability(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('materialMachinability_materialName')
        if new_name:
            edit_materialMachinability_obj = models.MaterialMachinability.objects.get(id=edit_id)
            edit_materialMachinability_obj.materialName = new_name
            edit_materialMachinability_obj.Strength = request.POST.get('materialMachinability_Strength')
            edit_materialMachinability_obj.hardness = request.POST.get('materialMachinability_hardness')
            edit_materialMachinability_obj.therConduct = request.POST.get('materialMachinability_therConduct')
            edit_materialMachinability_obj.hardening = request.POST.get('materialMachinability_hardening')
            edit_materialMachinability_obj.affinity = request.POST.get('materialMachinability_affinity')
            edit_materialMachinability_obj.otherField1 = request.POST.get('materialMachinability_otherField1')
            edit_materialMachinability_obj.otherField2 = request.POST.get('materialMachinability_otherField2')
            edit_materialMachinability_obj.save()
            return redirect('/standardKnowNInfo/material/')
        else:
            error_msg = '材料名称不能为空'
    materialMachinability_obj = models.MaterialMachinability.objects.get(id=edit_id)
    return render(request, 'old/edit_materialMachinability.html',
                  {'materialMachinability': materialMachinability_obj, 'error_msg': error_msg})


def search_materialMachinability(request):
    search = request.GET.get('materialMachinability_search')
    all_materialMachinability_obj = models.MaterialMachinability.objects.filter(materialName__icontains=search).all()
    error_msg = ''
    tab_name = 'materialMachinability'
    return render(request, 'standard_knowledge_and_information/material.html',
                  {'materialMachinability_list': all_materialMachinability_obj, "tab_name": tab_name})


# Feature
def add_Feature(request):
    error_msg = ''
    if request.method == 'POST':
        new_Feature = request.POST.get('Feature_classSecond')
        if new_Feature:
            # img_file=request.FILES.get('Feature_FeatureImg')
            new_Feature_obj = models.Feature.objects.create(classSecond=new_Feature,
                                                            classFirst=request.POST.get('Feature_classFirst'),
                                                            paraDef=request.POST.get('Feature_paraDef'),
                                                            imgPath=request.POST.get('Feature_imgPath'),
                                                            remark=request.POST.get('Feature_remark')
                                                            )

            return redirect('/standardKnowNInfo/standardStruction/')
        else:
            error_msg = '特征小类不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_Feature.html', {'error_msg': error_msg})


def delete_Feature(request, del_id):
    models.Feature.objects.get(id=del_id).delete()
    return redirect('/standardKnowNInfo/standardStruction/')


def edit_Feature(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('Feature_classSecond')
        if new_name:
            edit_Feature_obj = models.Feature.objects.get(id=edit_id)
            edit_Feature_obj.classSecond = new_name
            edit_Feature_obj.classFirst = request.POST.get('Feature_classFirst')
            edit_Feature_obj.paraDef = request.POST.get('Feature_paraDef')
            edit_Feature_obj.imgPath = request.POST.get('Feature_imgPath')
            edit_Feature_obj.remark = request.POST.get('Feature_remark')
            edit_Feature_obj.save()
            return redirect('/standardKnowNInfo/standardStruction/')
        else:
            error_msg = '特征小类不能为空'
    Feature_obj = models.Feature.objects.get(id=edit_id)
    return render(request, 'old/edit_Feature.html', {'Feature': Feature_obj, 'error_msg': error_msg})


def search_Feature(request):
    search = request.GET.get('Feature_search')
    all_Feature_obj = models.Feature.objects.filter(classSecond__icontains=search).all()
    error_msg = ''
    return render(request, 'standard_knowledge_and_information/standard_struction.html',
                  {'Feature_list': all_Feature_obj})


def search_feature_second(request):
    feature = request.POST.get('feature')
    if feature:
        all_feature_second_obj = models.Feature.objects.filter(classFirst__icontains=feature)
        json_data = serializers.serialize('json', all_feature_second_obj)
        print(json_data)
        return HttpResponse(json_data, content_type="application/json")


def ManuCapRule_list(request):
    all_ManuCapRule = models.ManuCapRule.objects.all()
    return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_list': all_ManuCapRule})


# def add_rule_search_Feature_para(request,featType):
#     #search = request.GET.get('ManuCapRule_featType2')
#     all_Feature_obj = models.Feature.objects.filter(classSecond__icontains=featType).all()
#     error_msg = ''
#     return render(request, 'old/add_ManuCapRule.html', {'FeaturePara_list': all_Feature_obj})

def add_ManuCapRule(request):
    error_msg = ''
    if request.method == 'POST':
        new_ManuCapRule = request.POST.get('ManuCapRule_name')
        if new_ManuCapRule:
            # img_file=request.FILES.get('ManuCapRule_ManuCapRuleImg')
            new_ManuCapRule_obj = models.ManuCapRule.objects.create(name=new_ManuCapRule,
                                                                    captype=request.POST.get('ManuCapRule_captype'),
                                                                    manuType=request.POST.get('ManuCapRule_manuType'),
                                                                    featType1=request.POST.get('ManuCapRule_featType1'),
                                                                    featType2=request.POST.get('ManuCapRule_featType2'),
                                                                    featPro=request.POST.get('ManuCapRule_featPro'),
                                                                    resType=request.POST.get('ManuCapRule_resType'),
                                                                    content=request.POST.get('ManuCapRule_content'),
                                                                    script=request.POST.get('ManuCapRule_script'),
                                                                    inputParaList=request.POST.get(
                                                                        'ManuCapRule_inputParaList'),
                                                                    outputParaList=request.POST.get(
                                                                        'ManuCapRule_outputParaList'),
                                                                    paraTable=request.POST.get('ManuCapRule_paraTable'),
                                                                    ManuCapRemark=request.POST.get(
                                                                        'ManuCapRule_ManuCapRemark')
                                                                    )

            return redirect('/processCheck/manuAbility/')
        else:
            error_msg = '刀具名称不能为空'
    # books = models.Book.objects.all()
    Feature_list = models.Feature.objects.all()
    FeaturePara_list = models.Feature.objects.all()
    return render(request, 'old/add_ManuCapRule.html',
                  {'FeaturePara_list': FeaturePara_list, 'Feature_list': Feature_list, 'error_msg': error_msg})


def delete_ManuCapRule(request, del_id):
    models.ManuCapRule.objects.get(id=del_id).delete()
    return redirect('/processCheck/manuAbility/')


def edit_ManuCapRule(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('ManuCapRule_name')
        if new_name:
            edit_ManuCapRule_obj = models.ManuCapRule.objects.get(id=edit_id)
            edit_ManuCapRule_obj.name = new_name
            edit_ManuCapRule_obj.captype = request.POST.get('ManuCapRule_captype')
            edit_ManuCapRule_obj.manuType = request.POST.get('ManuCapRule_manuType')
            edit_ManuCapRule_obj.featType1 = request.POST.get('ManuCapRule_featType1')
            edit_ManuCapRule_obj.featType2 = request.POST.get('ManuCapRule_featType2')
            edit_ManuCapRule_obj.featPro = request.POST.get('ManuCapRule_featPro')
            edit_ManuCapRule_obj.resType = request.POST.get('ManuCapRule_resType')
            edit_ManuCapRule_obj.content = request.POST.get('ManuCapRule_content')
            edit_ManuCapRule_obj.script = request.POST.get('ManuCapRule_script')
            edit_ManuCapRule_obj.inputParaList = request.POST.get('ManuCapRule_inputParaList')
            edit_ManuCapRule_obj.outputParaList = request.POST.get('ManuCapRule_outputParaList')
            edit_ManuCapRule_obj.paraTable = request.POST.get('ManuCapRule_paraTable')
            edit_ManuCapRule_obj.ManuCapRemark = request.POST.get('ManuCapRule_ManuCapRemark')
            edit_ManuCapRule_obj.save()
            return redirect('/processCheck/manuAbility/')
        else:
            error_msg = '刀具名不能为空'
    ManuCapRule_obj = models.ManuCapRule.objects.get(id=edit_id)
    KnowledgePara_list = models.KnowledgeParaTable.objects.filter(ruleid=edit_id).all
    return render(request, 'old/edit_ManuCapRule.html',
                  {'KnowledgePara_list': KnowledgePara_list, 'ManuCapRule': ManuCapRule_obj, 'error_msg': error_msg})


def edit_ParaForManuCapRule(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('ManuCapRule_name')
        if new_name:
            edit_ManuCapRule_obj = models.ManuCapRule.objects.get(id=edit_id)
            edit_ManuCapRule_obj.name = new_name
            edit_ManuCapRule_obj.captype = request.POST.get('ManuCapRule_captype')
            edit_ManuCapRule_obj.manuType = request.POST.get('ManuCapRule_manuType')
            edit_ManuCapRule_obj.featType1 = request.POST.get('ManuCapRule_featType1')
            edit_ManuCapRule_obj.featType2 = request.POST.get('ManuCapRule_featType2')
            edit_ManuCapRule_obj.featPro = request.POST.get('ManuCapRule_featPro')
            edit_ManuCapRule_obj.resType = request.POST.get('ManuCapRule_resType')
            edit_ManuCapRule_obj.content = request.POST.get('ManuCapRule_content')
            edit_ManuCapRule_obj.script = request.POST.get('ManuCapRule_script')
            edit_ManuCapRule_obj.inputParaList = request.POST.get('ManuCapRule_inputParaList')
            edit_ManuCapRule_obj.outputParaList = request.POST.get('ManuCapRule_outputParaList')
            edit_ManuCapRule_obj.paraTable = request.POST.get('ManuCapRule_paraTable')
            edit_ManuCapRule_obj.ManuCapRemark = request.POST.get('ManuCapRule_ManuCapRemark')
            edit_ManuCapRule_obj.save()
            return redirect('/processCheck/manuAbility/')
        else:
            error_msg = '刀具名不能为空'
    ManuCapRule_obj = models.ManuCapRule.objects.get(id=edit_id)
    KnowledgePara_list = models.KnowledgeParaTable.objects.filter(ruleid=edit_id).all
    return render(request, 'old/edit_ParaForManuCapRule.html',
                  {'KnowledgePara_list': KnowledgePara_list, 'ManuCapRule': ManuCapRule_obj, 'error_msg': error_msg})


def search_ManuCapRule(request):
    search = request.GET.get('ManuCapRule_search')
    all_ManuCapRule_obj = models.ManuCapRule.objects.filter(name__icontains=search).all()
    error_msg = ''
    return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_list': all_ManuCapRule_obj})


def add_KnowledgeParaTable(request, rule_id):
    error_msg = ''
    ManuCapRule_obj = models.ManuCapRule.objects.get(id=rule_id)
    if request.method == 'POST':
        new_KnowledgeParaTable = request.POST.get('KnowledgeParaTable_name')
        if new_KnowledgeParaTable:
            tablefunctionId = request.POST.get('KnowledgeParaTable_tableFunction')
            tablefunction_obj = models.TableFunction.objects.get(id=tablefunctionId)
            new_KnowledgeParaTable_obj = models.KnowledgeParaTable.objects.create(name=new_KnowledgeParaTable,
                                                                                  ruleid=ManuCapRule_obj,
                                                                                  paraType=request.POST.get(
                                                                                      'KnowledgeParaTable_paraType'),
                                                                                  defaultValue=request.POST.get(
                                                                                      'KnowledgeParaTable_defaultValue'),
                                                                                  tableFunction=tablefunction_obj,
                                                                                  remark=request.POST.get(
                                                                                      'KnowledgeParaTable_remark')
                                                                                  )

            return redirect('/edit_ParaForManuCapRule/' + str(rule_id) + '/')
        else:
            error_msg = '参数名称不能为空'
    rule_name = ManuCapRule_obj.name
    tableFunction_list = models.TableFunction.objects.all()
    return render(request, 'old/add_KnowledgeParaTable.html',
                  {'tableFunction_list': tableFunction_list, 'rule_name': rule_name, 'rule_id': rule_id,
                   'error_msg': error_msg})


def delete_KnowledgeParaTable(request, del_id):
    rule_id = models.KnowledgeParaTable.objects.get(id=del_id).ruleid
    models.KnowledgeParaTable.objects.get(id=del_id).delete()

    return redirect('/edit_ManuCapRule/' + str(rule_id.id) + '/')


def edit_KnowledgeParaTable(request, edit_id):
    error_msg = ''
    ManuCapRule_obj = models.KnowledgeParaTable.objects.get(id=edit_id).ruleid
    # ManuCapRule_obj = models.ManuCapRule.objects.get(id=rule_id)
    if request.method == 'POST':
        new_name = request.POST.get('KnowledgeParaTable_name')
        if new_name:
            tablefunctionId = request.POST.get('KnowledgeParaTable_tableFunction')
            tablefunction_obj = models.TableFunction.objects.get(id=tablefunctionId)
            edit_KnowledgeParaTable_obj = models.KnowledgeParaTable.objects.get(id=edit_id)
            edit_KnowledgeParaTable_obj.name = new_name
            edit_KnowledgeParaTable_obj.ruleid = ManuCapRule_obj
            edit_KnowledgeParaTable_obj.paraType = request.POST.get('KnowledgeParaTable_paraType')
            edit_KnowledgeParaTable_obj.defaultValue = request.POST.get('KnowledgeParaTable_defaultValue')
            edit_KnowledgeParaTable_obj.tableFunction = tablefunction_obj
            edit_KnowledgeParaTable_obj.remark = request.POST.get('KnowledgeParaTable_remark')
            edit_KnowledgeParaTable_obj.save()
            return redirect('/edit_ParaForManuCapRule/' + str(ManuCapRule_obj.id) + '/')
        else:
            error_msg = '刀具名不能为空'
    KnowledgeParaTable_obj = models.KnowledgeParaTable.objects.get(id=edit_id)
    rule_id = ManuCapRule_obj.id
    rule_name = ManuCapRule_obj.name
    tableFunction_list = models.TableFunction.objects.all()
    return render(request, 'old/edit_KnowledgeParaTable.html',
                  {'KnowledgeParaTable': KnowledgeParaTable_obj, 'tableFunction_list': tableFunction_list,
                   'rule_name': rule_name, 'rule_id': rule_id, 'error_msg': error_msg})
    # return render(request, 'old/edit_KnowledgeParaTable.html', {'KnowledgeParaTable': KnowledgeParaTable_obj, 'error_msg': error_msg})


def TableFunction_list(request):
    all_TableFunction = models.TableFunction.objects.all()
    return render(request, 'rule_configuration/table_function.html', {'TableFunction_list': all_TableFunction})


def add_TableFunction(request):
    error_msg = ''
    if request.method == 'POST':
        new_TableFunction = request.POST.get('TableFunction_name')
        if new_TableFunction:
            # img_file=request.FILES.get('TableFunction_TableFunctionImg')
            new_TableFunction_obj = models.TableFunction.objects.create(name=new_TableFunction,
                                                                        functionName=request.POST.get(
                                                                            'TableFunction_functionName'),
                                                                        inputPara=request.POST.get(
                                                                            'TableFunction_inputPara'),
                                                                        outputPara=request.POST.get(
                                                                            'TableFunction_outputPara'),
                                                                        sql=request.POST.get('TableFunction_sql'),
                                                                        remark=request.POST.get('TableFunction_remark')
                                                                        )

            return redirect('/scriptFunction/table_function/')
        else:
            error_msg = '数据库内表名不能为空'
    # books = models.Book.objects.all()
    return render(request, 'old/add_TableFunction.html', {'error_msg': error_msg})


def delete_TableFunction(request, del_id):
    models.TableFunction.objects.get(id=del_id).delete()
    return redirect('/scriptFunction/table_function/')


def edit_TableFunction(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('TableFunction_name')
        if new_name:
            edit_TableFunction_obj = models.TableFunction.objects.get(id=edit_id)
            edit_TableFunction_obj.name = new_name
            edit_TableFunction_obj.functionName = request.POST.get('TableFunction_functionName')
            edit_TableFunction_obj.inputPara = request.POST.get('TableFunction_inputPara')
            edit_TableFunction_obj.outputPara = request.POST.get('TableFunction_outputPara')
            edit_TableFunction_obj.sql = request.POST.get('TableFunction_sql')
            edit_TableFunction_obj.remark = request.POST.get('TableFunction_remark')
            edit_TableFunction_obj.save()
            return redirect('/scriptFunction/table_function/')
        else:
            error_msg = '刀具名不能为空'
    TableFunction_obj = models.TableFunction.objects.get(id=edit_id)
    return render(request, 'old/edit_TableFunction.html', {'TableFunction': TableFunction_obj, 'error_msg': error_msg})


def search_TableFunction(request):
    search = request.GET.get('TableFunction_search')
    all_TableFunction_obj = models.TableFunction.objects.filter(name__icontains=search).all()
    error_msg = ''
    return render(request, 'rule_configuration/table_function.html', {'TableFunction_list': all_TableFunction_obj})


def change_password(request):
    username = request.POST["userName"]
    old_password = request.POST["oldPassword"]
    new_password = request.POST["newPassword"]
    print(username, old_password, new_password)
    user = auth.authenticate(request, username=username, password=old_password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        return HttpResponse("修改成功!")
    else:
        return HttpResponse("用户名或原密码错误")


def login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        user = auth.authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if user is not None:
            return render(request, 'knowledge_search.html')
        else:
            # 返回登录失败信息
            error_msg = '用户名或密码错误'
            # return HttpResponse('登陆失败')
            return render(request, 'login.html', {'errorMessage': error_msg})

    return render(request, 'login.html', {'errorMessage': error_msg})


def index(request):
    if request.method == 'GET':
        return render(request, 'knowledge_search.html')
    type = request.POST.get('type')
    contents = request.POST.get('search_content')
    classes = request.POST.get('class')
    # if contents == "":
    #     return render(request, 'knowledge_search.html')
    if type == "工艺性审查知识":
        if classes != "全部":
            obj = models.Rule.objects.filter(name__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(ruleTypeFirst__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(ruleTypeSecond__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(content__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(featTypeFirst__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(featTypeSecond__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(featPro__icontains=contents, ruleClass=classes) | \
                  models.Rule.objects.filter(remark__icontains=contents, ruleClass=classes)
        else:
            obj = models.Rule.objects.filter(name__icontains=contents) | \
                  models.Rule.objects.filter(ruleTypeFirst__icontains=contents) | \
                  models.Rule.objects.filter(ruleTypeSecond__icontains=contents) | \
                  models.Rule.objects.filter(content__icontains=contents) | \
                  models.Rule.objects.filter(featTypeFirst__icontains=contents) | \
                  models.Rule.objects.filter(featTypeSecond__icontains=contents) | \
                  models.Rule.objects.filter(featPro__icontains=contents) | \
                  models.Rule.objects.filter(remark__icontains=contents)
    elif type == "PMI标注审查知识":
        obj = models.PMIRule.objects.filter(content__icontains=contents) | \
              models.PMIRule.objects.filter(name__icontains=contents) | \
              models.PMIRule.objects.filter(ruleType__icontains=contents) | \
              models.PMIRule.objects.filter(annoType__icontains=contents)
    return render(request, 'knowledge_search.html', {'obj': obj, 'type': type, 'content': contents, 'class': classes})

def knowledge_detail(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        content = request.GET.get('content')
        classes = request.GET.get('class')
        id = request.GET.get('id')
        if type == "工艺性审查知识":
            obj = models.Rule.objects.get(id=id)
        else:
            obj = models.PMIRule.objects.get(id=id)
    return render(request, 'knowledge_detail.html', {'obj': obj, 'type': type, 'content': content,'class':classes})


def PMI_annotation(request):
    if request.method == 'GET':
        if request.GET.get('content') == None:
            PMI_rule = models.PMIRule.objects.all()
            return render(request, 'model_quality/PMI_annotation.html', {'PMI_rule_list': PMI_rule})
        contents = request.GET.get('content')
        PMI_rule1 = models.PMIRule.objects.filter(content__icontains=contents)
        PMI_rule2 = models.PMIRule.objects.filter(name__icontains=contents)
        PMI_rule3 = models.PMIRule.objects.filter(ruleType__icontains=contents)
        PMI_rule4 = models.PMIRule.objects.filter(annoType__icontains=contents)
        PMI_rule = PMI_rule1 | PMI_rule2 | PMI_rule3 | PMI_rule4
        return render(request, 'model_quality/PMI_annotation.html', {'PMI_rule_list': PMI_rule})


def delete_PMIRule(request, del_id):
    models.PMIRule.objects.get(id=del_id).delete()
    return redirect('/modelQuality/PMI/')


annotationCode = {"尺寸公差": "DT", "直线度": "ST", "平面度": "FL", "圆度": "CI", "圆柱度": "CY", "线轮廓度": "PL",
                  "面轮廓度": "PS", "垂直度": "PE", "平行度": "PA", "对称度": "SY", "位置度": "PO", "同轴度": "CO",
                  "圆跳动": "CR", "全跳动": "TR"}


def add_PMIRule(request):
    error_msg = ''
    if request.method == 'POST':
        new_PMIRule = request.POST.get('PMIRule_name')
        print(request.POST.get('PMIRule_script'))
        if new_PMIRule:
            # 建立编码
            tempRule = models.PMIRule.objects.filter(annoType=request.POST.get('PMIRule_annoType')).order_by(
                '-code').values('code').first()
            if tempRule == None:
                num = 1
            else:
                print(tempRule['code'])
                num = int(tempRule['code'].split('-')[-1]) + 1
            code = 'AC-' + annotationCode[request.POST.get('PMIRule_annoType')] + "-" + str(num)
            new_PMIRule_obj = models.PMIRule.objects.create(name=new_PMIRule,
                                                            code=code,
                                                            ruleType=request.POST.get('PMIRule_ruleType'),
                                                            annoType=request.POST.get('PMIRule_annoType'),
                                                            content=request.POST.get('PMIRule_content'),
                                                            script=request.POST.get('PMIRule_script'),
                                                            PMIImg=request.FILES.get('PMIRule_Img_file'), )
            return redirect('/modelQuality/PMI/')
        else:
            error_msg = '规则名称不能为空'
    return render(request, 'old/add_PMIRule.html', {'error_msg': error_msg})


def edit_PMIRule(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('PMIRule_name')
        if new_name:
            PMIRule_obj = models.PMIRule.objects.get(id=edit_id)
            PMIRule_obj.name = request.POST.get('PMIRule_name')
            PMIRule_obj.ruleType = request.POST.get('PMIRule_ruleType')
            PMIRule_obj.annoType = request.POST.get('PMIRule_annoType')
            PMIRule_obj.content = request.POST.get('PMIRule_content')
            PMIRule_obj.script = request.POST.get('PMIRule_script')
            if request.FILES.get('PMIRule_Img_file'):
                PMIRule_obj.PMIImg = request.FILES.get('PMIRule_Img_file')
            PMIRule_obj.save()
            return redirect('/modelQuality/PMI/')
        else:
            error_msg = '刀具名不能为空'
    PMIRule_obj = models.PMIRule.objects.get(id=edit_id)
    return render(request, 'old/edit_PMIRule.html', {'PMIRule': PMIRule_obj, 'error_msg': error_msg})


def process_check(request):
    print('yes')
    if request.method == 'GET':
        if request.GET.get('content') == None:
            process_check_rule = models.Rule.objects.all()
            return render(request, 'process_Check/process_check.html', {'process_check_rule_list': process_check_rule})
        contents = request.GET.get('content')
        process_check_rule = models.Rule.objects.filter(name__icontains=contents) | \
                             models.Rule.objects.filter(ruleClass__icontains=contents) | \
                             models.Rule.objects.filter(ruleTypeFirst__icontains=contents) | \
                             models.Rule.objects.filter(ruleTypeSecond__icontains=contents) | \
                             models.Rule.objects.filter(content__icontains=contents) | \
                             models.Rule.objects.filter(featTypeFirst__icontains=contents) | \
                             models.Rule.objects.filter(featTypeSecond__icontains=contents) | \
                             models.Rule.objects.filter(featPro__icontains=contents) | \
                             models.Rule.objects.filter(remark__icontains=contents)
        return render(request, 'process_Check/process_check.html', {'process_check_rule_list': process_check_rule})


def delete_process_check(request):
    if request.method == "GET":
        del_id = request.GET.get("id")
        models.Rule.objects.get(id=del_id).delete()
    return redirect('/processCheck/')


classCode = {'零件级': "P", "特征级": "F"}
featureCode = {"孔": "H",
               "槽": "S",
               "口框": "MF",
               "凸台": "CP",
               "筋": "T",
               "加工面": "MS",
               "轮廓": "C",
               }


def add_process_check(request):
    error_msg = ''
    if request.method == 'POST':
        process_check_name = request.POST.get("rule_name")
        if process_check_name:

            # 建立编码
            tempRule = models.Rule.objects.filter(ruleClass=request.POST.get('rule_ruleClass'), \
                                                  featTypeFirst=request.POST.get('rule_featTypeFirst')).order_by(
                '-code').values('code').first()
            if tempRule == None:
                num = 1
            else:
                print(tempRule['code'])
                num = int(tempRule['code'].split('-')[-1]) + 1
            code = 'PC-' + classCode[request.POST.get('rule_ruleClass')] + "-" + featureCode[ \
                request.POST.get('rule_featTypeFirst')] + "-" + str(num)
            new_process_check_obj = \
                models.Rule.objects.create(name=process_check_name,
                                           code=code,
                                           ruleClass=request.POST.get('rule_ruleClass'),
                                           ruleTypeFirst=request.POST.get('rule_ruleTypeFirst'),
                                           ruleTypeSecond=request.POST.get('rule_ruleTypeSecond'),
                                           manuType=request.POST.get('rule_manuType'),
                                           featTypeFirst=request.POST.get('rule_featTypeFirst'),
                                           featTypeSecond=request.POST.get('rule_featTypeSecond'),
                                           featPro=request.POST.get('rule_featPro'),
                                           content=request.POST.get('rule_content'),
                                           img=request.FILES.get('rule_Img_file'),
                                           script=request.POST.get('rule_script'),
                                           remark=request.POST.get('rule_remark')
                                           )
            return redirect('/processCheck/')
        else:
            error_msg = '函数名不能为空'
    return render(request, 'old/add_process_check.html', {'error_msg': error_msg})


def edit_process_check(request):
    error_msg = ''
    if request.method == 'POST':
        edit_id = request.POST.get('rule_id')
        if edit_id:
            rule_obj = models.Rule.objects.get(id=edit_id)
            rule_obj.name = request.POST.get('rule_name')
            rule_obj.ruleClass = request.POST.get('rule_ruleClass')
            rule_obj.ruleTypeFirst = request.POST.get('rule_ruleTypeFirst')
            rule_obj.ruleTypeSecond = request.POST.get('rule_ruleTypeSecond')
            rule_obj.manuType = request.POST.get('rule_manuType')
            rule_obj.featTypeFirst = request.POST.get('rule_featTypeFirst')
            rule_obj.featTypeSecond = request.POST.get('rule_featTypeSecond')
            rule_obj.featPro = request.POST.get('rule_featPro')
            rule_obj.content = request.POST.get('rule_content')
            rule_obj.script = request.POST.get('rule_script')
            rule_obj.remark = request.POST.get('rule_remark')

            if request.FILES.get('rule_Img_file'):
                rule_obj.img = request.FILES.get('rule_Img_file')
            rule_obj.save()
            return redirect('/processCheck/')
        else:
            error_msg = '规则名不能为空'

    rule_obj = models.Rule.objects.get(id=request.GET.get("id"))
    return render(request, 'old/edit_process_check.html', {'rule_obj': rule_obj, 'error_msg': error_msg})


def manufacturing_ability(request):
    all_mat_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="材料").all()
    all_acc_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="精度").all()
    all_size_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="尺寸").all()
    return render(request, 'process_Check/manufacturing_ability.html',
                  {'ManuCapRule_mat_list': all_mat_ManuCapRule, 'ManuCapRule_acc_list': all_acc_ManuCapRule,
                   'ManuCapRule_size_list': all_size_ManuCapRule})


def knowledge_para(request):
    knowledge_para = models.ManuCapRule.objects.filter(captype__icontains="材料").all()
    all_acc_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="精度").all()
    all_size_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="尺寸").all()
    return render(request, 'process_Check/manufacturing_ability.html',
                  {'ManuCapRule_mat_list': all_mat_ManuCapRule, 'ManuCapRule_acc_list': all_acc_ManuCapRule,
                   'ManuCapRule_size_list': all_size_ManuCapRule})


# def manufacturing_ability_acc(request):
#     all_acc_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="精度").all()
#     return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_acc_list': all_acc_ManuCapRule})
#
# def manufacturing_ability_size(request):
#     all_size_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="尺寸").all()
#     return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_size_list': all_size_ManuCapRule})


def space_position(request):
    all_author = models.Author.objects.all()
    return render(request, 'process_Check/space_position.html', {'author_list': all_author})


def structural_machinability(request):
    all_author = models.Author.objects.all()
    return render(request, 'process_Check/structural_machinability.html', {'author_list': all_author})


def standard_struction(request):
    all_Feature = models.Feature.objects.all()
    return render(request, 'standard_knowledge_and_information/standard_struction.html', {'Feature_list': all_Feature})


def standard_process(request):
    return render(request, 'standard_knowledge_and_information/standard_process.html')


def material(request):
    all_author = models.Author.objects.all()
    return render(request, 'standard_knowledge_and_information/material.html', {'author_list': all_author})


def resource(request):
    all_cutter = models.Cutter.objects.all()
    return render(request, 'standard_knowledge_and_information/resource.html', {'cutter_list': all_cutter})


def standardize(request):
    all_author = models.Author.objects.all()
    return render(request, 'standard_knowledge_and_information/standardize.html', {'author_list': all_author})


def rule_parameter(request):
    if request.method == 'GET':
        if request.GET.get('content') == None:
            rule_parameter = models.KnowledgeParaTable.objects.all()
            return render(request, 'rule_configuration/rule_parameter.html', {'RuleParameter_list': rule_parameter})
        contents = request.GET.get('content')
        rule_parameter = models.KnowledgeParaTable.objects.filter(name__icontains=contents) | \
                         models.KnowledgeParaTable.objects.filter(paraType__icontains=contents) | \
                         models.KnowledgeParaTable.objects.filter(remark__icontains=contents)
        return render(request, 'rule_configuration/rule_parameter.html', {'RuleParameter_list': rule_parameter})


def delete_ruleParameter(request, del_id):
    models.KnowledgeParaTable.objects.get(id=del_id).delete()
    return redirect('/scriptFunction/rule_parameter/')


def change_ruleParameter(request):
    error_msg = ''
    if request.method == 'POST':
        name = request.POST.get('ruleParameter_name')
        ruleParameter_obj = models.KnowledgeParaTable.objects.filter(name=name)
        if ruleParameter_obj.exists():  # 修改
            ruleParameter_obj = models.KnowledgeParaTable.objects.get(name=name)
            ruleParameter_obj.paraType = request.POST.get('ruleParameter_paraType')
            ruleParameter_obj.remark = request.POST.get('ruleParameter_remark')
            if request.POST.get('ruleParameter_paraType') == '单值':
                ruleParameter_obj.defaultValue = request.POST.get('ruleParameter_singleValue')
            else:
                ruleParameter_obj.defaultValue = '[' + request.POST.get(
                    'ruleParameter_lowerValue') + ',' + request.POST.get('ruleParameter_upperValue') + ']'
            ruleParameter_obj.save()
        else:  # 更新
            if request.POST.get('ruleParameter_paraType') == '单值':
                ruleParameter_obj = \
                    models.KnowledgeParaTable.objects.create(name=name,
                                                             paraType=request.POST.get('ruleParameter_paraType'),
                                                             remark=request.POST.get('ruleParameter_remark'),
                                                             defaultValue=request.POST.get('ruleParameter_singleValue'))
            else:
                tempStr = '[' + request.POST.get('ruleParameter_lowerValue') + ',' + request.POST.get(
                    'ruleParameter_upperValue') + ']'
                ruleParameter_obj = \
                    models.KnowledgeParaTable.objects.create(name=name,
                                                             paraType=request.POST.get('ruleParameter_paraType'),
                                                             remark=request.POST.get('ruleParameter_remark'),
                                                             defaultValue=tempStr)
    return redirect('/scriptFunction/rule_parameter/')


def data_dictionary(request):
    if request.method == 'GET':
        if request.GET.get('content') == None:
            data_dictionary = models.DataDictionary.objects.all()
            return render(request, 'rule_configuration/data_dictionary.html', {'DataDictionary_list': data_dictionary})
        contents = request.GET.get('content')
        data_dictionary1 = models.DataDictionary.objects.filter(item__icontains=contents)
        data_dictionary2 = models.DataDictionary.objects.filter(type__icontains=contents)
        data_dictionary3 = models.DataDictionary.objects.filter(remark__icontains=contents)
        data_dictionary = data_dictionary1 | data_dictionary2 | data_dictionary3
        return render(request, 'rule_configuration/data_dictionary.html', {'DataDictionary_list': data_dictionary})


def delete_dataDictionary(request, del_id):
    models.DataDictionary.objects.get(id=del_id).delete()
    return redirect('/scriptFunction/data_dictionary/')


def change_dataDictionary(request):
    error_msg = ''
    if request.method == 'POST':
        item = request.POST.get('dataDictionary_item')
        dataDictionary_obj = models.DataDictionary.objects.filter(item=item)
        if dataDictionary_obj.exists():
            dataDictionary_obj = models.DataDictionary.objects.get(item=item)
            dataDictionary_obj.type = request.POST.get('dataDictionary_type')
            dataDictionary_obj.remark = request.POST.get('dataDictionary_remark')
            dataDictionary_obj.save()
        else:
            dataDictionary_obj = models.DataDictionary.objects.create(item=item,
                                                                      type=request.POST.get('dataDictionary_type'),
                                                                      remark=request.POST.get('dataDictionary_remark'))
    return redirect('/scriptFunction/data_dictionary/')


# 搜索数据字典
def search_dataDictionary(request):
    content = request.POST.get('content')
    all_dataDictionary_obj = models.DataDictionary.objects.filter(item__icontains=content) | \
                             models.DataDictionary.objects.filter(type__icontains=content) | \
                             models.DataDictionary.objects.filter(remark__icontains=content)

    json_data = serializers.serialize('json', all_dataDictionary_obj)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")


# 搜索特征属性
def search_feature_pro(request):
    content = request.POST.get("content")

    all_obj = models.DataDictionary.objects.filter(item__icontains=content, type="特征属性") | \
              models.DataDictionary.objects.filter(remark__icontains=content, type="特征属性")

    json_data = serializers.serialize('json', all_obj)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")


# 搜索规则配置的内容
def search_script_supporter(request):
    content = request.POST.get("searchContent")
    type = request.POST.get("searchType")
    if type == "数据字典":
        all_obj = models.DataDictionary.objects.filter(item__icontains=content) | \
                  models.DataDictionary.objects.filter(type__icontains=content) | \
                  models.DataDictionary.objects.filter(remark__icontains=content)
    elif type == "规则参数":
        all_obj = models.KnowledgeParaTable.objects.filter(name__icontains=content) | \
                  models.KnowledgeParaTable.objects.filter(remark__icontains=content)
    elif type == "查表函数":
        all_obj = models.TableFunction.objects.filter(name__icontains=content) | \
                  models.TableFunction.objects.filter(functionName__icontains=content) | \
                  models.TableFunction.objects.filter(remark__icontains=content)
    elif type == "脚本函数":
        all_obj = models.ScriptFunction.objects.filter(functionName__icontains=content) | \
                  models.ScriptFunction.objects.filter(formula__icontains=content) | \
                  models.ScriptFunction.objects.filter(remark__icontains=content)
    json_data = serializers.serialize('json', all_obj)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")


def table_function(request):
    all_tablaFuction = models.TableFunction.objects.all()
    return render(request, 'rule_configuration/table_function.html', {'TableFunction_list': all_tablaFuction})


def script_function(request):
    if request.method == 'GET':
        if request.GET.get('content') == None:
            script_function = models.ScriptFunction.objects.all()
            return render(request, 'rule_configuration/script_function.html', {'ScriptFunction_list': script_function})
        contents = request.GET.get('content')
        script_function1 = models.ScriptFunction.objects.filter(functionName__icontains=contents)
        script_function2 = models.ScriptFunction.objects.filter(inputPara__icontains=contents)
        script_function3 = models.ScriptFunction.objects.filter(outputPara__icontains=contents)
        script_function4 = models.ScriptFunction.objects.filter(formula__icontains=contents)
        script_function5 = models.ScriptFunction.objects.filter(remark__icontains=contents)
        script_function = script_function1 | script_function2 | script_function3 | script_function4 | script_function5
        return render(request, 'rule_configuration/script_function.html', {'ScriptFunction_list': script_function})


def delete_scriptFunction(request):
    if request.method == "GET":
        del_id = request.GET.get("id")
        models.ScriptFunction.objects.get(id=del_id).delete()
    return redirect('/scriptFunction/script_function/')


def add_scriptFunction(request):
    error_msg = ''
    if request.method == 'POST':
        new_scriptFunction = request.POST.get('scriptFunction_name')
        # print(request.POST.get('PMIRule_script'))
        if new_scriptFunction:
            new_scriptFunction_obj = \
                models.ScriptFunction.objects.create(functionName=new_scriptFunction,
                                                     inputPara=request.POST.get('scriptFunction_inputPara'),
                                                     outputPara=request.POST.get('scriptFunction_outputPara'),
                                                     formula=request.POST.get('scriptFunction_formula'),
                                                     remark=request.POST.get('scriptFunction_remark'),
                                                     functionHead=request.POST.get('scriptFunction_functionHead'))
            return redirect('/scriptFunction/script_function/')
        else:
            error_msg = '函数名不能为空'
    return render(request, 'old/add_scriptFunction.html', {'error_msg': error_msg})


def edit_scriptFunction(request):
    error_msg = ''
    if request.method == 'POST':
        ids = request.POST.get('scriptFunction_id')
        if ids:
            scriptFunction_obj = models.ScriptFunction.objects.get(id=ids)
            scriptFunction_obj.functionName = request.POST.get('scriptFunction_name')
            scriptFunction_obj.inputPara = request.POST.get('scriptFunction_inputPara')
            scriptFunction_obj.outputPara = request.POST.get('scriptFunction_outputPara')
            scriptFunction_obj.formula = request.POST.get('scriptFunction_formula')
            scriptFunction_obj.remark = request.POST.get('scriptFunction_remark')
            scriptFunction_obj.functionHead = request.POST.get('scriptFunction_functionHead')
            scriptFunction_obj.save()
            return redirect('/scriptFunction/script_function/')
        else:
            error_msg = '函数名不能为空'
    edit_id = request.GET.get('id')
    scriptFunction_obj = models.ScriptFunction.objects.get(id=edit_id)
    return render(request, 'old/edit_scriptFunction.html',
                  {'scriptFunction': scriptFunction_obj, 'error_msg': error_msg})
