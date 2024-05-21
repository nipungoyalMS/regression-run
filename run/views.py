from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from run.forms import RunForm
import re

# Create your views here.

def run(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        block = request.POST.get('block')
        project = request.POST.get('project')
        projectSetup = request.POST.get('projectSetup')
        buildPath = request.POST.get('buildPath')

        # Print all form data
        print("Block:", block)
        print("Project:", project)
        print("Project Setup:", projectSetup)
        print("Build Path:", buildPath)
        
        # You can perform further processing with the form data here
        command = f"/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/launch_regression_run.zsh "

        if block:
            command += f"""-b "{block}" """
        if project:
            command+= f"""-programs "{project}" """
        if buildPath:
            command += f"""-build_path {buildPath} """
        if projectSetup:
            command += f"""-project_setup {projectSetup} """

        command += f"""-once"""

        print(command)


        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        template = loader.get_template('run.html')
        return HttpResponse(template.render({}, request))



def extract_block_names(request):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    block_names = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+ "blocks=(\w+)', line)
            if match:
                block_names.add(match.group(1))
    return JsonResponse({'blocks': list(block_names)})


def extract_programs_for_block(request, block_name):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    programs = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+\s+"blocks\s*=\s*(\w+)\s+project\s*=\s*(\w+)', line)
            if match and match.group(1) == block_name:
                programs.add(match.group(2))
    return JsonResponse({'programs': list(programs)})


import os
from pathlib import Path

def get_latest_project_setup(request, project):
    if project == 'KNG':
        folder_path = '/home/scratch-kingsgate/tsmc003ffe/A0/pd/setup'
    elif project == 'BRG':
        folder_path = '/home/scratch-braga/tsmc003ffe/A0/pd/setup'
    else:
        return JsonResponse({'projectSetups': []})  # Unknown project

    # Get the list of directories and sort them by creation time
    directories = sorted(filter(os.path.isdir, Path(folder_path).iterdir()), key=os.path.getctime, reverse=True)

    # Get the names of the 5 latest directories
    latest_directories = [directory.name for directory in directories[:5]]
    return JsonResponse({'projectSetups': latest_directories})


def get_latest_build_path(request):
    folder_path = '/home/scratch-designinfra/genesys_mile/'
    # Get the list of directories and sort them by creation time
    directories = sorted(filter(os.path.isdir, Path(folder_path).iterdir()), key=os.path.getctime, reverse=True)

    # Get the names of the 5 latest directories
    latest_directories = [directory.name for directory in directories[:5]]
    return JsonResponse({'latestBuildPaths': latest_directories})