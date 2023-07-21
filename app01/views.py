from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from app01 import models
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


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
            new_cutter_obj = models.Cutter.objects.create(name=new_cutter,supplier=request.POST.get('cutter_supplier'),
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
    #books = models.Book.objects.all()
    return render(request, 'old/add_cutter.html', { 'error_msg': error_msg})


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
            edit_cutter_obj.cutterImg = request.POST.get('cutter_cutterImg')
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
    return render(request, 'standard_knowledge_and_information/resource.html', {'cutter_list': all_cutter_obj})




def add_Feature(request):
    error_msg = ''
    if request.method == 'POST':
        new_Feature = request.POST.get('Feature_classSecond')
        if new_Feature:
            # img_file=request.FILES.get('Feature_FeatureImg')
            new_Feature_obj = models.Feature.objects.create(classSecond=new_Feature,classFirst=request.POST.get('Feature_classFirst'),
                                                          paraDef=request.POST.get('Feature_paraDef'),
                                                          imgPath=request.POST.get('Feature_imgPath'),
                                                          remark=request.POST.get('Feature_remark')
                                               )

            return redirect('/standardKnowNInfo/standardStruction/')
        else:
            error_msg = '特征小类不能为空'
    #books = models.Book.objects.all()
    return render(request, 'old/add_Feature.html', { 'error_msg': error_msg})


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
    return render(request, 'standard_knowledge_and_information/standard_struction.html', {'Feature_list': all_Feature_obj})











def ManuCapRule_list(request):
    all_ManuCapRule = models.ManuCapRule.objects.all()
    return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_list': all_ManuCapRule})

# def add_rule_search_Feature_para(request):
#     search = request.GET.get('ManuCapRule_featType2')
#     all_Feature_obj = models.Feature.objects.filter(classSecond__icontains=search).all()
#     error_msg = ''
#     return render(request, 'old/add_ManuCapRule.html', {'FeaturePara_list': FeaturePara_list})

def add_ManuCapRule(request):
    error_msg = ''
    if request.method == 'POST':
        new_ManuCapRule = request.POST.get('ManuCapRule_name')
        if new_ManuCapRule:
            # img_file=request.FILES.get('ManuCapRule_ManuCapRuleImg')
            new_ManuCapRule_obj = models.ManuCapRule.objects.create(name=new_ManuCapRule,captype=request.POST.get('ManuCapRule_captype'),
                                                          manuType=request.POST.get('ManuCapRule_manuType'),
                                                          featType1=request.POST.get('ManuCapRule_featType1'),
                                                          featType2=request.POST.get('ManuCapRule_featType2'),
                                                          featPro=request.POST.get('ManuCapRule_featPro'),
                                                          resType=request.POST.get('ManuCapRule_resType'),
                                                          content=request.POST.get('ManuCapRule_content'),
                                                          script=request.POST.get('ManuCapRule_script'),
                                                          inputParaList=request.POST.get('ManuCapRule_inputParaList'),
                                                          outputParaList=request.POST.get('ManuCapRule_outputParaList'),
                                                          paraTable=request.POST.get('ManuCapRule_paraTable'),
                                                          ManuCapRemark=request.POST.get('ManuCapRule_ManuCapRemark')
                                               )

            return redirect('/processCheck/manuAbility/')
        else:
            error_msg = '刀具名称不能为空'
    #books = models.Book.objects.all()
    Feature_list = models.Feature.objects.all()
    FeaturePara_list=models.Feature.objects.all()
    return render(request, 'old/add_ManuCapRule.html', { 'FeaturePara_list':FeaturePara_list,'Feature_list':Feature_list,'error_msg': error_msg})


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
    KnowledgePara_list=models.KnowledgeParaTable.objects.filter(ruleid=edit_id).all
    return render(request, 'old/edit_ManuCapRule.html', {'KnowledgePara_list':KnowledgePara_list,'ManuCapRule': ManuCapRule_obj, 'error_msg': error_msg})

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
    KnowledgePara_list=models.KnowledgeParaTable.objects.filter(ruleid=edit_id).all
    return render(request, 'old/edit_ParaForManuCapRule.html', {'KnowledgePara_list':KnowledgePara_list,'ManuCapRule': ManuCapRule_obj, 'error_msg': error_msg})


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
            tablefunctionId=request.POST.get('KnowledgeParaTable_tableFunction')
            tablefunction_obj=models.TableFunction.objects.get(id=tablefunctionId)
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

            return redirect('/edit_ParaForManuCapRule/'+str(rule_id)+'/')
        else:
            error_msg = '参数名称不能为空'
    rule_name =ManuCapRule_obj.name
    tableFunction_list=models.TableFunction.objects.all()
    return render(request, 'old/add_KnowledgeParaTable.html', {'tableFunction_list':tableFunction_list,'rule_name':rule_name,'rule_id': rule_id, 'error_msg': error_msg})

def delete_KnowledgeParaTable(request, del_id):
    rule_id=models.KnowledgeParaTable.objects.get(id=del_id).ruleid
    models.KnowledgeParaTable.objects.get(id=del_id).delete()

    return redirect('/edit_ManuCapRule/'+str(rule_id.id)+'/')


def edit_KnowledgeParaTable(request, edit_id):
    error_msg = ''
    ManuCapRule_obj=models.KnowledgeParaTable.objects.get(id=edit_id).ruleid
    #ManuCapRule_obj = models.ManuCapRule.objects.get(id=rule_id)
    if request.method == 'POST':
        new_name = request.POST.get('KnowledgeParaTable_name')
        if new_name:
            tablefunctionId=request.POST.get('KnowledgeParaTable_tableFunction')
            tablefunction_obj=models.TableFunction.objects.get(id=tablefunctionId)
            edit_KnowledgeParaTable_obj = models.KnowledgeParaTable.objects.get(id=edit_id)
            edit_KnowledgeParaTable_obj.name = new_name
            edit_KnowledgeParaTable_obj.ruleid = ManuCapRule_obj
            edit_KnowledgeParaTable_obj.paraType = request.POST.get('KnowledgeParaTable_paraType')
            edit_KnowledgeParaTable_obj.defaultValue = request.POST.get('KnowledgeParaTable_defaultValue')
            edit_KnowledgeParaTable_obj.tableFunction = tablefunction_obj
            edit_KnowledgeParaTable_obj.remark = request.POST.get('KnowledgeParaTable_remark')
            edit_KnowledgeParaTable_obj.save()
            return redirect('/edit_ParaForManuCapRule/'+str(ManuCapRule_obj.id)+'/')
        else:
            error_msg = '刀具名不能为空'
    KnowledgeParaTable_obj = models.KnowledgeParaTable.objects.get(id=edit_id)
    rule_id=ManuCapRule_obj.id
    rule_name =ManuCapRule_obj.name
    tableFunction_list=models.TableFunction.objects.all()
    return render(request, 'old/edit_KnowledgeParaTable.html', {'KnowledgeParaTable': KnowledgeParaTable_obj, 'tableFunction_list':tableFunction_list,'rule_name':rule_name,'rule_id': rule_id, 'error_msg': error_msg})
    # return render(request, 'old/edit_KnowledgeParaTable.html', {'KnowledgeParaTable': KnowledgeParaTable_obj, 'error_msg': error_msg})



















def TableFunction_list(request):
    all_TableFunction = models.TableFunction.objects.all()
    return render(request, 'script_and_function/table_function.html', {'TableFunction_list': all_TableFunction})

def add_TableFunction(request):
    error_msg = ''
    if request.method == 'POST':
        new_TableFunction = request.POST.get('TableFunction_name')
        if new_TableFunction:
            # img_file=request.FILES.get('TableFunction_TableFunctionImg')
            new_TableFunction_obj = models.TableFunction.objects.create(name=new_TableFunction,functionName=request.POST.get('TableFunction_functionName'),
                                                          inputPara=request.POST.get('TableFunction_inputPara'),
                                                          outputPara=request.POST.get('TableFunction_outputPara'),
                                                          sql=request.POST.get('TableFunction_sql'),
                                                          remark=request.POST.get('TableFunction_remark')
                                               )

            return redirect('/scripNFunction/table_function/')
        else:
            error_msg = '数据库内表名不能为空'
    #books = models.Book.objects.all()
    return render(request, 'old/add_TableFunction.html', { 'error_msg': error_msg})


def delete_TableFunction(request, del_id):
    models.TableFunction.objects.get(id=del_id).delete()
    return redirect('/scripNFunction/table_function/')


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
            return redirect('/scripNFunction/table_function/')
        else:
            error_msg = '刀具名不能为空'
    TableFunction_obj = models.TableFunction.objects.get(id=edit_id)
    return render(request, 'old/edit_TableFunction.html', {'TableFunction': TableFunction_obj, 'error_msg': error_msg})

def search_TableFunction(request):
    search = request.GET.get('TableFunction_search')
    all_TableFunction_obj = models.TableFunction.objects.filter(name__icontains=search).all()
    error_msg = ''
    return render(request, 'script_and_function/table_function.html', {'TableFunction_list': all_TableFunction_obj})

















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
            return render(request, 'index.html')
        else:
            # 返回登录失败信息
            error_msg = '用户名或密码错误'
            # return HttpResponse('登陆失败')
            return render(request, 'login.html', {'errorMessage':error_msg})

    return render(request, 'login.html', {'errorMessage':error_msg})


def index(request):
    return render(request, 'index.html')


def PMI_annotation(request):
    all_author = models.Author.objects.all()
    return render(request, 'model_quality/PMI_annotation.html', {'author_list': all_author})


def manufacturing_ability(request):
    all_mat_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="材料").all()
    all_acc_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="精度").all()
    all_size_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="尺寸").all()
    return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_mat_list': all_mat_ManuCapRule,'ManuCapRule_acc_list': all_acc_ManuCapRule,'ManuCapRule_size_list': all_size_ManuCapRule})


def knowledge_para(request):
    knowledge_para = models.ManuCapRule.objects.filter(captype__icontains="材料").all()
    all_acc_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="精度").all()
    all_size_ManuCapRule = models.ManuCapRule.objects.filter(captype__icontains="尺寸").all()
    return render(request, 'process_Check/manufacturing_ability.html', {'ManuCapRule_mat_list': all_mat_ManuCapRule,'ManuCapRule_acc_list': all_acc_ManuCapRule,'ManuCapRule_size_list': all_size_ManuCapRule})




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


def table_function(request):
    all_tablaFuction = models.TableFunction.objects.all()
    return render(request, 'script_and_function/table_function.html', {'TableFunction_list': all_tablaFuction})


