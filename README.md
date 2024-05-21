Set up and installation:
- First of all download the zip or clone the repo to local system using "git clone https://github.com/nipungoyalMS/regression-run.git"
- Now go inside the repo and make a virtual environment using "python3 -m venv myenv"
- Now activate virtual environment using "source myenv/bin/activate"
- Now install django inside virtual environment using "pip3 install django"
- Now make migrations using "python3 manage.py makemigrations"
- Now migrate the database using "python3 manage.py migrate"
- Now runserver using "python3 manage.py runserver"
- Now open a web browser and go to url "http://127.0.0.1:8000/run/"
- Now select the parameters and click run and command will be printed on your terminal.