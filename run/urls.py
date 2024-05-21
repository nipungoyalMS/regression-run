from django.urls import path
from run.views import run,extract_block_names,extract_programs_for_block,get_latest_project_setup,get_latest_build_path

urlpatterns = [
    path('', run,name="run"),
    path('get_blocks/', extract_block_names, name='get_blocks'),
    path('get_projects/<str:block_name>/', extract_programs_for_block, name='get_programs_for_block'),
    path('get_project_setups/<str:project>/', get_latest_project_setup, name='get_latest_project_setup'),
    path('get_latest_build_path/', get_latest_build_path, name='get_latest_build_path'),
    
]