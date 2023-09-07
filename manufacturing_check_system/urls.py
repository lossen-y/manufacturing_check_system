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
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
# from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path as url

from app01 import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^index/', views.index, name='index'),
                  url(r'^$', views.login, name='login'),
                  url(r'^changePassword/', views.change_password, name='change_password'),
                  url(r'^knowledge_detail/', views.knowledge_detail, name='knowledge_detail'),

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
                  url(r'^delete_PMIRule/([0-9]+)/$', views.delete_PMIRule, name='delete_PMIRule'),
                  url(r'^add_PMIRule/$', views.add_PMIRule, name='add_PMIRule'),
                  url(r'^edit_PMIRule/([0-9]+)/$', views.edit_PMIRule, name='edit_PMIRule'),

                  # 工艺性审查知识
                  # url(r'^processCheck/manuAbility/', views.manufacturing_ability_mat, name='manufacturing_ability'),
                  # url(r'^processCheck/manuAbility/', views.manufacturing_ability_acc, name='manufacturing_ability'),
                  url(r'^processCheck/', views.process_check, name='process_check'),
                  url(r'^delete_processCheck/', views.delete_process_check, name='delete_process_check'),
                  url(r'^edit_processCheck/', views.edit_process_check, name='edit_process_check'),
                  url(r'^add_processCheck/', views.add_process_check, name='add_process_check'),

                  url(r'^processCheck/manuAbility/', views.manufacturing_ability, name='manufacturing_ability'),
                  url(r'^processCheck/spacePosition/', views.space_position, name='space_Position'),
                  url(r'^processCheck/strucMachinability/', views.structural_machinability,
                      name='structural_machinability'),
                  # 脚本函数的关键词搜索
                  url(r'^search_script_supporter/', views.search_script_supporter, name='search_script_supporter'),

                  # 制造资源
                  url(r'^standardKnowNInfo/standardStruction/', views.standard_struction, name='standard_struction'),
                  url(r'^standardKnowNInfo/standardProcess/', views.standard_process, name='standard_process'),
                  url(r'^standardKnowNInfo/material/', views.material, name='material'),
                  url(r'^standardKnowNInfo/resource/$', views.resource, name='resource'),
                  url(r'^standardKnowNInfo/standardize/', views.standardize, name='standardize'),

                  # 查表函数
                  url(r'^scriptFunction/table_function/$', views.table_function, name='table_function'),
                  # 数据字典
                  url(r'^scriptFunction/data_dictionary/$', views.data_dictionary, name='data_dictionary'),
                  url(r'^delete_dataDictionary/([0-9]+)/$', views.delete_dataDictionary, name='delete_dataDictionary'),
                  url(r'^change_dataDictionary/$', views.change_dataDictionary, name='change_dataDictionary'),
                  url(r'^data_Dictionary_search/$', views.search_dataDictionary, name='search_dataDictionary'),
                  # 脚本函数
                  url(r'^scriptFunction/script_function/$', views.script_function, name='script_function'),
                  url(r'^delete_scriptFunction/$', views.delete_scriptFunction, name='delete_scriptFunction'),
                  url(r'^add_scriptFunction/$', views.add_scriptFunction, name='add_scriptFunction'),
                  url(r'^edit_scriptFunction/$', views.edit_scriptFunction, name='edit_scriptFunction'),
                  # 机床相关的对应关系
                  url(r'^add_mach/$', views.add_mach, name='add_mach'),
                  url(r'^search_mach/$', views.search_mach, name='search_mach'),
                  url(r'^delete_mach/([0-9]+)/$', views.delete_mach, name='delete_mach'),
                  url(r'^edit_mach/([0-9]+)/$', views.edit_mach, name='edit_mach'),

                  # 工装相关的对应关系
                  url(r'^add_fixture/$', views.add_fixture, name='add_fixture'),
                  url(r'^search_fixture/$', views.search_fixture, name='search_fixture'),
                  url(r'^delete_fixture/([0-9]+)/$', views.delete_fixture, name='delete_fixture'),
                  url(r'^edit_fixture/([0-9]+)/$', views.edit_fixture, name='edit_fixture'),

                  # 角度头相关的对应关系
                  url(r'^add_head/$', views.add_head, name='add_head'),
                  url(r'^search_head/$', views.search_head, name='search_head'),
                  url(r'^delete_head/([0-9]+)/$', views.delete_head, name='delete_head'),
                  url(r'^edit_head/([0-9]+)/$', views.edit_head, name='edit_head'),

                  # 刀具相关的对应关系
                  # url(r'^standardKnowNInfo/resource/', views.cutter_list, name='standardKnowNInfo'),
                  # url(r'^resource/$', views.reource, name='book_list'),
                  url(r'^add_cutter/$', views.add_cutter, name='add_cutter'),
                  url(r'^search_cutter/$', views.search_cutter, name='search_cutter'),
                  url(r'^delete_cutter/([0-9]+)/$', views.delete_cutter, name='delete_cutter'),
                  url(r'^edit_cutter/([0-9]+)/$', views.edit_cutter, name='edit_cutter'),

                  # 标准孔相关的对应关系
                  # url(r'^standardKnowNInfo/resource/', views.cutter_list, name='standardKnowNInfo'),
                  # url(r'^resource/$', views.reource, name='book_list'),
                  url(r'^add_apert/$', views.add_apert, name='add_apert'),
                  url(r'^search_apert/$', views.search_apert, name='search_apert'),
                  url(r'^delete_apert/([0-9]+)/$', views.delete_apert, name='delete_apert'),
                  url(r'^edit_apert/([0-9]+)/$', views.edit_apert, name='edit_apert'),
                  # 下载excel
                  url(r'^download_apert/([0-9]+)/$', views.download_excel, name='download_excel'),

                  # 基本偏差表
                  url(r'^add_precision/$', views.add_precision, name='add_precision'),
                  url(r'^search_precision/$', views.search_precision, name='search_precision'),
                  url(r'^delete_precision/([0-9]+)/$', views.delete_precision, name='delete_precision'),
                  url(r'^edit_precision/([0-9]+)/$', views.edit_precision, name='edit_precision'),

                  # 公差等差表
                  url(r'^add_fitTolerance/$', views.add_fitTolerance, name='add_fitTolerance'),
                  url(r'^search_fitTolerance/$', views.search_fitTolerance, name='search_fitTolerance'),
                  url(r'^delete_fitTolerance/([0-9]+)/$', views.delete_fitTolerance, name='delete_fitTolerance'),
                  url(r'^edit_fitTolerance/([0-9]+)/$', views.edit_fitTolerance, name='edit_fitTolerance'),

                  # 优先配合表
                  url(r'^add_prio/$', views.add_prio, name='add_prio'),
                  url(r'^search_prio/$', views.search_prio, name='search_prio'),
                  url(r'^delete_prio/([0-9]+)/$', views.delete_prio, name='delete_prio'),
                  url(r'^edit_prio/([0-9]+)/$', views.edit_prio, name='edit_prio'),

                  # 零件工艺路线表
                  url(r'^add_part/$', views.add_part, name='add_part'),
                  url(r'^search_part/$', views.search_part, name='search_part'),
                  url(r'^delete_part/([0-9]+)/$', views.delete_part, name='delete_part'),
                  url(r'^edit_part/([0-9]+)/$', views.edit_part, name='edit_part'),

                  # 特征工艺路线表
                  url(r'^add_feat/$', views.add_feat, name='add_feat'),
                  url(r'^search_feat/$', views.search_feat, name='search_feat'),
                  url(r'^delete_feat/([0-9]+)/$', views.delete_feat, name='delete_feat'),
                  url(r'^edit_feat/([0-9]+)/$', views.edit_feat, name='edit_feat'),

                  # 材料牌号表
                  url(r'^add_materialDesignation/$', views.add_materialDesignation, name='add_materialDesignation'),
                  url(r'^search_materialDesignation/$', views.search_materialDesignation,
                      name='search_materialDesignation'),
                  url(r'^delete_materialDesignation/([0-9]+)/$', views.delete_materialDesignation,
                      name='delete_materialDesignation'),
                  url(r'^edit_materialDesignation/([0-9]+)/$', views.edit_materialDesignation,
                      name='edit_materialDesignation'),

                  # 材料牌号表
                  url(r'^add_materialMachinability/$', views.add_materialMachinability,
                      name='add_materialMachinability'),
                  url(r'^search_materialMachinability/$', views.search_materialMachinability,
                      name='search_materialMachinability'),
                  url(r'^delete_materialMachinability/([0-9]+)/$', views.delete_materialMachinability,
                      name='delete_materialMachinability'),
                  url(r'^edit_materialMachinability/([0-9]+)/$', views.edit_materialMachinability,
                      name='edit_materialMachinability'),

                  # 标准特征相关的对应关系
                  url(r'^add_Feature/$', views.add_Feature, name='add_Feature'),
                  url(r'^search_Feature/$', views.search_Feature, name='search_Feature'),
                  url(r'^delete_Feature/([0-9]+)/$', views.delete_Feature, name='delete_Feature'),
                  url(r'^edit_Feature/([0-9]+)/$', views.edit_Feature, name='edit_Feature'),
                  url(r'^search_feature_second/$', views.search_feature_second, name='search_feature_second'),

                  # 制造能力规则相关的对应关系
                  # url(r'^standardKnowNInfo/resource/', views.cutter_list, name='standardKnowNInfo'),
                  # url(r'^resource/$', views.reource, name='book_list'),
                  url(r'^add_ManuCapRule/$', views.add_ManuCapRule, name='add_ManuCapRule'),
                  url(r'^search_ManuCapRule/$', views.search_ManuCapRule, name='search_ManuCapRule'),
                  url(r'^delete_ManuCapRule/([0-9]+)/$', views.delete_ManuCapRule, name='delete_ManuCapRule'),
                  url(r'^edit_ManuCapRule/([0-9]+)/$', views.edit_ManuCapRule, name='edit_ManuCapRule'),
                  url(r'^edit_ParaForManuCapRule/([0-9]+)/$', views.edit_ParaForManuCapRule,
                      name='edit_ParaForManuCapRule'),
                  url(r'^add_rule_search_Feature_para/$', views.add_rule_search_Feature_para,
                      name='add_rule_search_Feature_para'),

                  # 规则参数表相关的对应关系
                  url(r'^add_KnowledgeParaTable/([0-9]+)/$', views.add_KnowledgeParaTable,
                      name='add_KnowledgeParaTable'),
                  url(r'^delete_KnowledgeParaTable/([0-9]+)/$', views.delete_KnowledgeParaTable,
                      name='delete_KnowledgeParaTable'),
                  url(r'^edit_KnowledgeParaTable/([0-9]+)/$', views.edit_KnowledgeParaTable,
                      name='edit_KnowledgeParaTable'),

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
