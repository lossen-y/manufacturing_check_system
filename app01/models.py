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

class Fixture(models.Model):
    '''
    工装表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, unique=True)    #工装编号
    fixtureType = models.CharField(max_length=128, null=True, unique=False)  #工装类型
    fixtureName = models.CharField(max_length=128, null=True, unique=False)  #工装名称
    fixtureCode = models.CharField(max_length=128, null=True, unique=False)  #工装打标号
    geoDim = models.CharField(max_length=128, null=True, unique=False)  #工装尺寸
    partType = models.CharField(max_length=128, null=True, unique=False)  #零件类型
    partStruct = models.CharField(max_length=128, null=True, unique=False)  #零件结构形式
    partMat = models.CharField(max_length=128, null=True, unique=False)  #零件材料
    partSize = models.CharField(max_length=128, unique=False)  #零件尺寸
    InterfaceDim = models.TextField(null=True, unique=False)  #接口尺寸
    fixtureImg = models.FileField(null=True, unique=False)  # 工装图片
    fixtureRemark = models.TextField(null=True, unique=False)  # 备注
    otherFields = models.TextField(null=True, unique=False)  # 其他字段

    def __str__(self):
        return self.name

class Mach(models.Model):
    '''
    机床表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=True, unique=True)    #机床名称
    machType = models.CharField(max_length=128, null=True, unique=False)  #机床类型
    travelX = models.CharField(max_length=128, null=True, unique=False)  # 线行轴X行程
    travelY = models.CharField(max_length=128, null=True, unique=False)  # 线行轴Y行程
    travelZ = models.CharField(max_length=128, null=True, unique=False)  # 线行轴Z行程
    travelA = models.CharField(max_length=128, null=True, unique=False)  # A轴行程
    travelB = models.CharField(max_length=128, null=True, unique=False)  # B轴行程
    travelC = models.CharField(max_length=128, null=True, unique=False)  # C轴行程
    PrecisionX = models.CharField(max_length=128, null=True, unique=False)  # X轴定位精度
    PrecisionY = models.CharField(max_length=128, null=True, unique=False)  # Y轴定位精度
    PrecisionZ = models.CharField(max_length=128, null=True, unique=False)  # Z轴定位精度
    PrecisionA = models.CharField(max_length=128, null=True, unique=False)  # A轴定位精度
    PrecisionB = models.CharField(max_length=128, null=True, unique=False)  # B轴定位精度
    PrecisionC = models.CharField(max_length=128, null=True, unique=False)  # C轴定位精度
    worktableSize_length = models.CharField(max_length=128, null=True, unique=False)  # 工作台长
    worktableSize_width = models.CharField(max_length=128, null=True, unique=False)  # 工作台宽
    load = models.CharField(max_length=128, null=True, unique=False)  # 工作台允许最大荷重（kg）
    process = models.CharField(max_length=128, null=True, unique=False)  #适用工序
    feature = models.CharField(max_length=128, null=True, unique=False)  #适用特征
    headID = models.CharField(max_length=128, null=True, unique=False)  #关联角度头
    machImg = models.FileField(null=True, unique=False)  # 机床图片
    machRemark = models.TextField(null=True, unique=False)  # 机床备注
    otherFields = models.TextField(null=True, unique=False)  # 其他字段

    def __str__(self):
        return self.name


class Head(models.Model):
    '''
    角度头表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=True, unique=True)    #角度头名称
    headType = models.CharField(max_length=128, null=True, unique=False)    #角度头型号
    headStruct = models.CharField(max_length=128, null=True, unique=False)    #角度铣头及加长杆包络轮廓
    headDepth = models.CharField(max_length=128, null=True, unique=False)    #最大加工深度
    toolDiamRange_max = models.CharField(max_length=128, null=True, unique=False)    #适用刀具直径范围（最大）
    toolDiamRange_min = models.CharField(max_length=128, null=True, unique=False)  # 适用刀具直径范围（最小）
    appMach = models.CharField(max_length=128, null=True, unique=False)    #适用机床
    headImg = models.FileField(null=True, unique=False)  # 角度头图片
    headRemark = models.TextField(null=True, unique=False)  # 角度头备注
    otherFields = models.TextField(null=True, unique=False)  # 其他字段

    def __str__(self):
        return self.name

class Apert(models.Model):
    '''
    标准孔径表
    '''
    id = models.AutoField(primary_key=True)
    apertType = models.CharField(max_length=128, null=True, unique=False)    #孔类型名称
    standard_apert = models.TextField(null=True, unique=False) # 标准孔径
    apertImg = models.FileField(null=True, unique=False)  # 标准孔图片
    excel_apertfile = models.FileField(null=True, unique=False, upload_to='excel_apertfiles/') # excel_apert文件模板
    apertRemark = models.TextField(null=True, unique=False)  # 标准孔备注
    otherFields = models.TextField(null=True, unique=False)  # 其他字段

    def __str__(self):
        return self.name

class Precision(models.Model):
    '''
    基本偏差表
    '''
    id = models.AutoField(primary_key=True)
    basic = models.CharField(max_length=128, null=True, unique=False) # 基准
    nomiSizeL = models.CharField(max_length=128, null=True, unique=False) # 公称尺寸下界
    nomiSizeR = models.CharField(max_length=128, null=True, unique=False) # 公称尺寸上界
    tolGrade = models.CharField(max_length=128, null=True, unique=False) # 公差等级
    basicDevNum = models.CharField(max_length=128, null=True, unique=False) # 基本偏差数值
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name

class FitTolerance(models.Model):
    '''
    公差等级表
    '''
    id = models.AutoField(primary_key=True)
    Class = models.CharField(max_length=128, null=True, unique=False) # 精度等级
    nomiSizeL = models.CharField(max_length=128, null=True, unique=False) # 公称尺寸下界
    nomiSizeR = models.CharField(max_length=128, null=True, unique=False) # 公称尺寸上界
    tolNum = models.CharField(max_length=128, null=True, unique=False) # 公差值
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name

class Prio(models.Model):
    '''
    优先配合表
    '''
    id = models.AutoField(primary_key=True)
    basic = models.CharField(max_length=128, null=True, unique=False) # 基准
    holeTol = models.CharField(max_length=128, null=True, unique=False) # 基准孔代号
    shaftTol = models.CharField(max_length=128, null=True, unique=False) # 轴公差代号
    fitType = models.CharField(max_length=128, null=True, unique=False) # 配合类型
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name

class Part(models.Model):
    '''
    零件工艺路线表
    '''
    id = models.AutoField(primary_key=True)
    partType = models.CharField(max_length=128, null=True, unique=False) # 零件类型
    partStruct = models.CharField(max_length=128, null=True, unique=False) # 零件结构形式
    partMat = models.CharField(max_length=128, null=True, unique=False) # 零件材料
    partSize = models.CharField(max_length=128, null=True, unique=False) # 零件尺寸

    geoFix = models.TextField(null=True, unique=False)  # 零件装夹位置
    PMIInfo = models.CharField(max_length=128, null=True, unique=False)  # 关联的PMI及精度
    featType = models.CharField(max_length=128, null=True, unique=False)  # 关联的特征类型
    processFlow = models.TextField(null=True, unique=False)  # 工艺流程
    Img = models.FileField(null=True, unique=False)  # 示意图

    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name


class Feat(models.Model):
    '''
    特征工艺路线表
    '''
    id = models.AutoField(primary_key=True)
    featID = models.CharField(max_length=128, null=True, unique=False) # 关联的特征
    featType = models.CharField(max_length=128, null=True, unique=False) # 特征几何结构
    featMat = models.CharField(max_length=128, null=True, unique=False) # 特征材料
    geoDim = models.CharField(max_length=128, null=True, unique=False) # 关联的PMI
    precision = models.TextField(null=True, unique=False)  # 最高精度
    processFlow = models.TextField(null=True, unique=False)  # 工艺流程
    Img = models.FileField(null=True, unique=False)  # 示意图
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name


class MaterialDesignation(models.Model):
    '''
    材料牌号表
    '''
    id = models.AutoField(primary_key=True)
    GBName = models.CharField(max_length=128, null=True, unique=False) # 材料名称
    matType1 = models.CharField(max_length=128, null=True, unique=False) # 材料大类
    matType2 = models.CharField(max_length=128, null=True, unique=False) # 材料小类
    matName = models.CharField(max_length=128, null=True, unique=False) # 材料别名
    ASTM = models.CharField(max_length=128, null=True, unique=False)  # ASTM
    SAE = models.CharField(max_length=128, null=True, unique=False)  # SAE
    desc = models.CharField(max_length=128, null=True, unique=False) # 描述
    Img = models.FileField(null=True, unique=False)  # 示意图
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

    def __str__(self):
        return self.name


class MaterialMachinability(models.Model):
    '''
    材料切削性表
    '''
    id = models.AutoField(primary_key=True)
    materialName = models.CharField(max_length=128, null=True, unique=False) # 材料名称
    Strength = models.CharField(max_length=128, null=True, unique=False) # 强度
    hardness = models.CharField(max_length=128, null=True, unique=False) # 硬度
    therConduct = models.CharField(max_length=128, null=True, unique=False) # 热传导率
    hardening = models.CharField(max_length=128, null=True, unique=False)  # 加工硬化
    affinity = models.CharField(max_length=128, null=True, unique=False)  # 刀具材料亲和性
    otherField1 = models.CharField(max_length=128, null=True, unique=False)  # 其他字段1
    otherField2 = models.TextField(null=True, unique=False)  # 其他字段2

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
    #ruleid=models.ForeignKey(to='ManuCapRule',to_field='id',on_delete=models.CASCADE) # 规则id,多对一关系
    name = models.CharField(max_length=128, null=False, unique=True)  # 参数名
    paraType=models.CharField(max_length=128, null=True, unique=False)  # 参数类型
    defaultValue = models.TextField(null=True, unique=False)  # 默认值
    #tableFunction = models.ForeignKey(to='TableFunction',to_field='name',null=True,on_delete=models.SET_NULL)  # 查表函数，外键多对一关系
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
    特征表
    '''
    id = models.AutoField(primary_key=True)
    classFirst = models.CharField(max_length=128, null=False, unique=False)  # 特征大类，写死，（孔、口框、槽、凸台、筋、加工面、轮廓）
    classSecond = models.CharField(max_length=128, null=True, unique=True)  # 特征小类
    # classID = models.CharField(max_length=128, null=True, unique=False) #特征编号
    # classDes=models.TextField(null=True, unique=False)   # 特征描述
    paraDef = models.TextField(null=True, unique=False)   # 参数化定义
    imgPath = models.FileField(null=True, unique=False)  # 示意图片
    remark = models.TextField(null=True, unique=False)  # 备注

    def __str__(self):
        return self.classSecond

class FeaturePara(models.Model):
    '''
    特征参数化定义表（特征属性表）
    '''
    id = models.AutoField(primary_key=True)
    parameter = models.ForeignKey(to='DataDictionary', to_field='item', on_delete=models.CASCADE)  # 参数(特征属性)
    value = models.CharField(max_length=128, null=True, unique=False)  # 参数的取值
    featureID = models.ForeignKey(to='Feature', on_delete=models.CASCADE) #对应的特征编号
    remark = models.TextField(null=True, unique=False)  # 备注

class Rule(models.Model):
    '''
    审查规则表(总表)
    '''
    id = models.AutoField(primary_key=True) # 规则编号
    name = models.CharField(max_length=128, null=True, unique=True)  # 规则名称
    ruleTypeFirst = models.CharField(max_length=128, null=True, unique=False)  # 规则大类
    ruleTypeSecond = models.CharField(max_length=128, null=True, unique=False)  # 规则小类
    #content = models.TextField(null=True, unique=False)  # 规则特定字段
    manuType = models.CharField(max_length=128, null=True, unique=False)  # 加工方式
    featTypeFirst = models.CharField(max_length=128, null=True, unique=False)  # 特征大类
    featTypeSecond = models.CharField(max_length=128, null=True, unique=False)  # 特征小类
    featPro = models.CharField(max_length=128, null=True, unique=False)  # 特征属性
    content = models.TextField(null=True, unique=False)  # 知识描述
    img=models.FileField(null=True, unique=False)  #规则图片
    script = models.TextField(null=True, unique=False)  # 脚本
    remark = models.TextField(null=True, unique=False)  # 备注

    def __str__(self):
        return self.name

# class PMI(models.Model):
#     '''
#     PMI标注表
#     '''
#     id = models.AutoField(primary_key=True)
#     PMIType = models.CharField(max_length=128, null=False, unique=False)  # 标注类型
#     paraDef = models.TextField(null=True, unique=False)  # 参数化定义，用json格式表示
#     remark = models.TextField(null=True, unique=False)  # 备注
#
#     def __str__(self):
#         return self.PMIType

class DataDictionary(models.Model):
    '''
    数据字典
    '''
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=128, null=False, unique=True)  # 数据字典
    type = models.CharField(max_length=128, null=False, unique=False)  # 数据字典类型
    remark = models.TextField(null=True, unique=False)  # 描述

    def __str__(self):
        return self.item

class ScriptFunction(models.Model):
    '''
    脚本函数表
    '''
    id = models.AutoField(primary_key=True)
    functionName = models.CharField(max_length=128, null=True, unique=True)  # 脚本函数名称
    functionHead = models.CharField(max_length=128, null=True, unique=True)  # 函数头
    inputPara = models.TextField(null=True, unique=False)   # 输入参数,以逗号的形式隔开
    outputPara = models.TextField(null=True, unique=False)  # 返回类型
    formula = models.TextField(null=True, unique=False)  # 函数表达式
    remark = models.TextField(null=True, unique=False)  # 备注

    def __str__(self):
        return self.name

class PMIRule(models.Model):
    '''
    PMI审查规则表
    '''
    id = models.AutoField(primary_key=True)    # 规则编号
    name = models.CharField(max_length=128, null=True, unique=True)  # 规则名称
    ruleType = models.CharField(max_length=128, null=True, unique=False)  # 规则类型
    annoType = models.CharField(max_length=128, null=True, unique=False)  # 规则对应标注的类型
    script = models.TextField(null=True, unique=False)  # 脚本
    content = models.TextField(null=True, unique=False)  # 知识描述
    PMIImg=models.FileField(null=True, unique=False)  #规则图片

    def __str__(self):
        return self.name