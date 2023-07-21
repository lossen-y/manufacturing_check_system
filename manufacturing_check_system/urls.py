"""manufacturing_check_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path as url

from app01 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.login, name='login'),
    url(r'^changePassword/', views.change_password, name='change_password'),

    # 出版社相关的对应关系
    url(r'^publisher_list/$', views.publisher_list, name='publisher_list'),
    url(r'^add_publisher/$', views.AddPublisher.as_view(), name='add_publisher'),
    # url(r'^add_publisher/', views.add_publisher, name='add_publisher'),
    url(r'^delete_publisher/([0-9]+)/$', views.delete_publisher, name='delete_publisher'),
    url(r'^edit_publisher/([0-9]+)/$', views.edit_publisher, name='edit_publisher'),

    # 书相关的对应关系
    url(r'^book_list/$', views.book_list, name='book_list'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^delete_book/([0-9]+)/$', views.delete_book, name='delete_book'),
    url(r'^edit_book/([0-9]+)/$', views.edit_book, name='edit_book'),

    # 作者相关的对应关系
    url(r'^add_author/$', views.add_author, name='add_author'),
    url(r'^delete_author/([0-9]+)/$', views.delete_author, name='delete_author'),
    url(r'^edit_author/([0-9]+)/$', views.edit_author, name='edit_author'),
    #
    # 建模质量
    url(r'^modelQuality/PMI/', views.PMI_annotation, name='PMI_annotation'),

    # 工艺性审查知识
    # url(r'^processCheck/manuAbility/', views.manufacturing_ability_mat, name='manufacturing_ability'),
    # url(r'^processCheck/manuAbility/', views.manufacturing_ability_acc, name='manufacturing_ability'),
    url(r'^processCheck/manuAbility/', views.manufacturing_ability, name='manufacturing_ability'),
    url(r'^processCheck/spacePosition/', views.space_position, name='space_Position'),
    url(r'^processCheck/strucMachinability/', views.structural_machinability, name='structural_machinability'),

    # 制造资源
    url(r'^standardKnowNInfo/standardStruction/', views.standard_struction, name='standard_struction'),
    url(r'^standardKnowNInfo/standardProcess/', views.standard_process, name='standard_process'),
    url(r'^standardKnowNInfo/material/', views.material, name='material'),
    url(r'^standardKnowNInfo/resource/$', views.resource, name='resource'),
    url(r'^standardKnowNInfo/standardize/', views.standardize, name='standardize'),

    #  脚本与函数
    url(r'^scripNFunction/table_function/$', views.table_function, name='table_function'),








    # 刀具相关的对应关系
    #url(r'^standardKnowNInfo/resource/', views.cutter_list, name='standardKnowNInfo'),
    #url(r'^resource/$', views.reource, name='book_list'),
    url(r'^add_cutter/$', views.add_cutter, name='add_cutter'),
    url(r'^search_cutter/$', views.search_cutter, name='search_cutter'),
    url(r'^delete_cutter/([0-9]+)/$', views.delete_cutter, name='delete_cutter'),
    url(r'^edit_cutter/([0-9]+)/$', views.edit_cutter, name='edit_cutter'),

    # 标准特征相关的对应关系
    url(r'^add_Feature/$', views.add_Feature, name='add_Feature'),
    url(r'^search_Feature/$', views.search_Feature, name='search_Feature'),
    url(r'^delete_Feature/([0-9]+)/$', views.delete_Feature, name='delete_Feature'),
    url(r'^edit_Feature/([0-9]+)/$', views.edit_Feature, name='edit_Feature'),

    # 制造能力规则相关的对应关系
    # url(r'^standardKnowNInfo/resource/', views.cutter_list, name='standardKnowNInfo'),
    # url(r'^resource/$', views.reource, name='book_list'),
    url(r'^add_ManuCapRule/$', views.add_ManuCapRule, name='add_ManuCapRule'),
    url(r'^search_ManuCapRule/$', views.search_ManuCapRule, name='search_ManuCapRule'),
    url(r'^delete_ManuCapRule/([0-9]+)/$', views.delete_ManuCapRule, name='delete_ManuCapRule'),
    url(r'^edit_ManuCapRule/([0-9]+)/$', views.edit_ManuCapRule, name='edit_ManuCapRule'),
    url(r'^edit_ParaForManuCapRule/([0-9]+)/$', views.edit_ParaForManuCapRule, name='edit_ParaForManuCapRule'),
    # url(r'^add_rule_search_Feature_para/$', views.add_rule_search_Feature_para, name='add_rule_search_Feature_para'),

    # 规则参数表相关的对应关系
    url(r'^add_KnowledgeParaTable/([0-9]+)/$', views.add_KnowledgeParaTable, name='add_KnowledgeParaTable'),
    url(r'^delete_KnowledgeParaTable/([0-9]+)/$', views.delete_KnowledgeParaTable, name='delete_KnowledgeParaTable'),
    url(r'^edit_KnowledgeParaTable/([0-9]+)/$', views.edit_KnowledgeParaTable, name='edit_KnowledgeParaTable'),

    # 查表函数对应关系
    url(r'^add_TableFunction/$', views.add_TableFunction, name='add_TableFunction'),
    url(r'^search_TableFunction/$', views.search_TableFunction, name='search_TableFunction'),
    url(r'^delete_TableFunction/([0-9]+)/$', views.delete_TableFunction, name='delete_TableFunction'),
    url(r'^edit_TableFunction/([0-9]+)/$', views.edit_TableFunction, name='edit_TableFunction'),


    # 系统接口
    # url(r'^input_FeaturePara/([0-9]+)/$', views.input_FeaturePara, name='input_FeaturePara'),
    # url(r'^input_table_Function/([0-9]+)/$', views.input_FeaturePara, name='input_FeaturePara'),
    #
    #
    #
    #
    # url(r'^output_RuleData/([0-9]+)/$', views.output_RuleData, name='output_RuleData'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
