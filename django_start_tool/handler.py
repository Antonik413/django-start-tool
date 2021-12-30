from zipfile import is_zipfile

from jinja2 import Template

from .utils import copy_tree
from .utils import download
from .utils import extract
from .utils import get_files_to_render
from .utils import is_url
from .utils import rename_entities


def handle_template(
    project_name,
    target,
    template,
    files_patterns,
    context
):
    if is_url(template):
        download(template, target)
    elif is_zipfile(template):
        extract(template, target)
    else:
        copy_tree(template, target)

    for file in get_files_to_render(target, files_patterns):
        content = Template(file.read_text()).render(**context)
        eof = '\n' if file.stat().st_size > 0 else ''
        file.write_text(content + eof)

    rename_entities(target, project_name)
