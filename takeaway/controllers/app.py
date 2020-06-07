# from .management import  BaseComand
import  os
import subprocess
from takeaway.settings.fastapi.requirements import  requirements
from takeaway.settings.fastapi.docker import  Dockerfile
from takeaway.settings.fastapi.readme import  readme
from takeaway.settings.fastapi.container import  container
from takeaway.settings.fastapi.env import  env
from takeaway.settings.fastapi.gitignore import  gitignore
from takeaway.settings.fastapi.pipfile import  pipfile
from takeaway.settings.fastapi.piplock import  piplock
from takeaway.settings.fastapi.prestart import  prestart
from takeaway.settings.fastapi.start import  fastapistart
from takeaway.settings.fastapi.controller import  controller
from takeaway.settings.fastapi.dbsetup import  dbsetup
from takeaway.settings.fastapi.extension import  extension
from takeaway.settings.fastapi.factories import  factories
from takeaway.settings.fastapi.helpers import  helper
from takeaway.settings.fastapi.main import  main
from takeaway.settings.fastapi.models import  model
from takeaway.settings.fastapi.pipfile import  pipfile
from takeaway.settings.fastapi.piplock import  piplock
from takeaway.settings.fastapi.readme import  readme
from takeaway.settings.fastapi.schemas import  schema
from takeaway.settings.fastapi.settings import  setting,devsetting,prodsettings


from takeaway.settings.flask import  docker
from takeaway.settings.django import  docker
# from .commands import Operation
# from takeaway.controllers.commands import  Operation

class FastApiApp:
    def __init__(self,app,folder_name):

        self.app = app
        self.folder_name = folder_name
        self.root_directory = f'{self.folder_name}/'
        
        self.core = f'{self.root_directory}core'
        self.settings = f'{self.core}/settings'

        self.app_folder = f'{self.root_directory}app'
        self.controllers = f'{self.app_folder}/controllers'
        self.controller = f'{self.controllers}/controller'

        self.data = f'{self.app_folder}/data'
        self.utils = f'{self.app_folder}/utils'


    def start(self):
        self.create_app_structure()

    def file_create(self,directory,filename,content):
        with open(f"{directory}/{filename}","w") as file:
            file.write(content.strip())


    def root_folder_create(self):
        os.makedirs(self.folder_name)


    def create_app_structure(self):
        '''This will initilaze the boilerplate of the project'''

        self.root_folder_create()
        
        os.makedirs(self.core)
        os.makedirs(self.settings)
        os.makedirs(self.app_folder)
        os.makedirs(self.controllers)
        os.makedirs(self.controller)
        os.makedirs(self.data)
        os.makedirs(self.utils)

        self.create_init_file(self.core)
        self.create_init_file(self.settings)
        self.create_init_file(self.app_folder)
        self.create_init_file(self.controllers)
        self.create_init_file(self.data)
        self.create_init_file(self.utils)

        self.file_create(self.root_directory,"Dockerfile",Dockerfile)
        self.file_create(self.root_directory,".gitignore",gitignore)
        self.file_create(self.root_directory,"Pipfile", pipfile)
        self.file_create(self.root_directory,"Pipfile.lock",piplock)
        self.file_create(self.root_directory,"prestart.sh",prestart)
        self.file_create(self.root_directory,"README.md",readme)
        self.file_create(self.root_directory,".env",env)
        self.file_create(self.root_directory,"requirements.txt",requirements)
        self.file_create(self.root_directory,"container.sh",container)
        self.file_create(self.root_directory,"start.sh",fastapistart)

        self.file_create(self.core,"factories.py",factories)
        self.file_create(self.core,"extensions.py",extension)
        self.file_create(self.core,"dbsetup.py",dbsetup)

        self.file_create(self.settings,"devsettings.py",devsetting)
        self.file_create(self.settings,"prodsettings.py",prodsettings)
        self.file_create(self.settings,"settings.py",setting)
        self.file_create(self.settings,"requirements.txt",requirements)

        self.file_create(self.app_folder,"main.py",main)

        self.file_create(self.controller,"controller.py",controller)
        self.file_create(self.controller,"schemas.py",schema)
        
        self.file_create(self.data,"models.py",model)
        self.file_create(self.utils,"helpers.py",helper)

        self.activate_pipenv()
        self.install_dependencies()
        self.ending()

    def ending(self):
        print(f"👨‍💻{self.app} is ready to go! ✅ 🥳 🎉 😋 ")
        print("⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️")
        print(f'❗cd {self.folder_name}')
        print("❗pipenv shell")
        print("❗pip install -r requirements.txt")
     
     
    def create_init_file(self,directory):

        with open(f"{directory}/__init__.py", "a") as file:
            file.write("")


    

    def activate_pipenv(self):
        '''This will activate pipenv'''
        #todo may be removed next future

        pass

        # install = 'pip install -r requirements.txt'
        
        # script_path = os.path.dirname(os.path.realpath(self.root_directory))
        # print("sad",script_path)
        # pa = script_path +"/"+ self.root_directory
        
        # script_path = os.path.dirname(os.path.realpath(self.root_directory))
        # print("sad",script_path)
        # pa = script_path +"/"+ self.root_directory
        # print(pa)
        # path = os.chdir(pa)
        # # os.chdir(pa)
        # # # os.chdir(self.root_directory)
        # # activate = 'pipenv shell'
        # print(path)
        # # subprocess.call(f"cd {pa}", shell=True)

    def install_dependencies(self):
        
    
        '''This will install all dependencies the app require'''
        #todo may be removed next future
        pass






class FlaskApp:
    
    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    
    def start(self):
        print(self.app)
        print(self.folder_name)


    def folder_create(self):
        os.makedirs(self.folder_name)






class DjangoApp:
    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    # promt ele app name burda
    def start(self):
        print(self.app)
        print(self.folder_name)