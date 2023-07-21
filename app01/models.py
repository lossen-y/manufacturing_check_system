from django.db import models

# Create your models here.
# ORM 相关的只能写在这个文件里，写到别的文件中Django都找不到



class Publisher(models.Model):
    '''
    出版社表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    # author = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    book = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name

class Cutter(models.Model):
    '''
    刀具表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, unique=True)    #刀具编号
    supplier=models.CharField(max_length=128, null=True, unique=False)  #供应商
    minHoleTole=models.CharField(max_length=128, null=True, unique=False)  #最小孔公差
    maxHoleTole=models.CharField(max_length=128, null=True, unique=False)  #最大孔公差
    minDia=models.CharField(max_length=128, null=True, unique=False)  #最小直径
    maxDia=models.CharField(max_length=128, null=True, unique=False)  #最大直径
    minDepDia=models.CharField(max_length=128, null=True, unique=False)  #最小深径比
    maxDepDia=models.CharField(max_length=128, null=True, unique=False)  #最大深径比
    capMat=models.TextField(null=True, unique=False)  #可加工材料
    cutterMat=models.CharField(max_length=128, null=True, unique=False)  #刀具材料
    capPro=models.TextField( null=True, unique=False)  #可加工工艺
    cutterCost=models.CharField(max_length=128, null=True, unique=False)  #刀具成本
    cutterImg=models.FileField(null=True, unique=False)  #刀具图片
    cutterRemark=models.TextField( null=True, unique=False)  #备注
    def __str__(self):
        return self.name

class ManuCapRule(models.Model):
    '''
    制造能力审查规则表
    '''
    id = models.AutoField(primary_key=True)    # 规则编号
    name = models.CharField(max_length=128, null=True, unique=True)  # 规则名称
    captype = models.CharField(max_length=128, null=True, unique=False)  # 制造能力参数类型
    manuType = models.CharField(max_length=128, null=True, unique=False)  # 加工方式
    featType1 = models.CharField(max_length=128, null=True, unique=False)  # 特征大类
    featType2 = models.CharField(max_length=128, null=True, unique=False)  # 特征小类
    featPro = models.CharField(max_length=128, null=True, unique=False)  # 特征属性
    resType = models.CharField(max_length=128, null=True, unique=False)  # 制造资源/工艺方案类型
    content = models.TextField(null=True, unique=False)  # 知识描述
    script = models.TextField(null=True, unique=False)  # 脚本
    inputParaList = models.TextField(null=True, unique=False)  # 脚本输入参数列表
    outputParaList = models.TextField(null=True, unique=False)  # 脚本输出参数列表
    paraTable = models.CharField(max_length=128, null=True, unique=False)  # 知识参数表名
    ManuCapRemark = models.TextField(null=True, unique=False)  # 备注
    def __str__(self):
        return self.name

class KnowledgeParaTable(models.Model):
    '''
    规则参数表
    '''
    id = models.AutoField(primary_key=True)
    ruleid=models.ForeignKey(to='ManuCapRule',to_field='id',on_delete=models.CASCADE) # 规则id,多对一关系
    name = models.CharField(max_length=128, null=False, unique=False)  # 参数名
    paraType=models.CharField(max_length=128, null=True, unique=False)  # 参数类型
    defaultValue = models.TextField(null=True, unique=False)  # 默认值
    tableFunction = models.ForeignKey(to='TableFunction',to_field='name',null=True,on_delete=models.SET_NULL)  # 查表函数，外键多对一关系
    remark = models.TextField(null=True, unique=False)  # 备注
    def __str__(self):
        return self.name
    # book = models.ManyToManyField(to='Book')

class TableFunction(models.Model):
    '''
    查表函数表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, unique=True)  # 数据库内表名
    functionName = models.CharField(max_length=128, null=True, unique=True)  # 内部查表函数名
    inputPara = models.TextField(null=True, unique=False)   # 输入参数
    outputPara = models.TextField(null=True, unique=False)  # 返回参数
    sql = models.TextField(null=True, unique=False)  # 对应SQL语句
    remark = models.TextField(null=True, unique=False)  # 备注

    def __str__(self):
        return self.name


class Feature(models.Model):
    '''
    特征结构表
    '''
    id = models.AutoField(primary_key=True)
    classFirst = models.CharField(max_length=128, null=False, unique=False)  # 特征大类
    classSecond = models.CharField(max_length=128, null=True, unique=False)  # 特征小类
    paraDef = models.TextField(null=True, unique=False)   # 参数化定义
    imgPath = models.TextField(null=True, unique=False)  # 示意图片路径
    remark = models.TextField(null=True, unique=False)  # 备注

    def __str__(self):
        return self.classSecond

class Rule(models.Model):
    '''
    审查规则表(总表)
    '''
    id = models.AutoField(primary_key=True)    # 规则编号
    name = models.CharField(max_length=128, null=True, unique=True)  # 规则名称
    ruleTypeFirst = models.CharField(max_length=128, null=True, unique=False)  # 规则大类
    ruleTypeSecond = models.CharField(max_length=128, null=True, unique=False)  # 规则小类
    content = models.TextField(null=True, unique=False)  # 规则特定字段
    manuType = models.CharField(max_length=128, null=True, unique=False)  # 加工方式
    featTypeFirst = models.CharField(max_length=128, null=True, unique=False)  # 特征大类
    featTypeSecond = models.CharField(max_length=128, null=True, unique=False)  # 特征小类
    featPro = models.CharField(max_length=128, null=True, unique=False)  # 特征属性
    content = models.TextField(null=True, unique=False)  # 知识描述
    imgPath = models.TextField(null=True, unique=False)  # 示意图片路径
    script = models.TextField(null=True, unique=False)  # 脚本
    remark = models.TextField(null=True, unique=False)  # 备注
    def __str__(self):
        return self.name