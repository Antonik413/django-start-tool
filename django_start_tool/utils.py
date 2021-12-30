import random
import shutil
from urllib.request import urlretrieve
from zipfile import ZipFile


def copy_tree(path, target):
    shutil.copytree(
        path,
        target,
        copy_function=shutil.copyfile,
        dirs_exist_ok=True
    )


def extract(path, target):
    with ZipFile(path) as archive:
        archive.extractall(target)


def get_subfolder_name(url):
    repo_name = url.split('/')[4]
    branch_name = url.split('/')[6][:-4]
    return f'{repo_name}-{branch_name}'


def get_files_to_render(path, patterns):
    return [
        entity
        for pattern in patterns
        for entity in path.glob(f'**/{pattern}')
        if entity.is_file()
    ]


def get_random_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(random.choice(chars) for _ in range(50))


def download(url, target):
    content, _ = urlretrieve(url)

    with ZipFile(content) as archive:
        archive.extractall()

    # There is subfolder in the GitHub repository zip archive
    # like this: django-start-tool-main -- '{repo_name}-{branch_name}'.
    # It is necessary to extract all the contents and delete this subfolder.
    subfolder_name = get_subfolder_name(url)
    copy_tree(subfolder_name, target)
    shutil.rmtree(subfolder_name)


def is_url(template):
    template = str(template)
    schemes = ['http', 'https', 'ftp']

    if ':' not in template:
        return False

    scheme = template.split(':', 1)[0].lower()
    return scheme in schemes


def rename_entities(path, project_name):
    # Renaming folders
    for entity in path.glob('**/project_name'):
        if entity.is_dir():
            new = entity.with_name(project_name)
            entity.rename(new)
    
    # Renaming files
    for entity in path.glob('**/*.py-tpl'):
        if entity.is_file():
            new = entity.with_name(entity.name[:-4])
            entity.rename(new)
