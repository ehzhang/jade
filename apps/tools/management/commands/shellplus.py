from optparse import make_option
from importlib import import_module

from IPython import embed
from IPython.frontend.terminal.ipapp import load_default_config

from django.core.management.base import NoArgsCommand
from django.db.models.loading import get_models, get_apps
from django.conf import settings


class Command(NoArgsCommand):
    help = ("Like the 'shell' command but autoloads the models of all "
            "installed Django apps.")
    option_list = NoArgsCommand.option_list + (
        make_option('--kernel', action='store_true',
                    help='Embed on ipython kernel'),
    )

    def handle_noargs(self, **options):
        imported_objects = get_import_objects()

        config = None
        prompt_prefix = get_prompt_prefix()
        if prompt_prefix:
            config = load_default_config()
            config.PromptManager.in_template = (
                '(%s) In [\#]: ' % prompt_prefix)

        if options['kernel']:
            from IPython import embed_kernel
            embed_kernel(local_n=imported_objects, config=config)
        else:
            embed(user_ns=imported_objects, config=config)


def get_prompt_prefix():
    return None


def import_object(import_path):
    if not import_path:
        raise ValueError('Empty import path')

    import_pieces = import_path.split('.')
    if len(import_pieces) == 1:
        # non-relative import, eg 'collections'
        return import_module(import_path)
    else:
        module = import_module('.'.join(import_pieces[:-1]))
        return getattr(module, import_pieces[-1])


def get_import_objects():
    """
    Collect objects to populate the interactive session
    """
    imported_objects = {}
    loaded_model_names = set()
    for app in get_apps():
        app_name = app.__name__.split('.')[-2]
        for model in get_models(app):
            model_name = model.__name__
            if model_name in loaded_model_names:
                model_name = '_'.join((app_name, model_name))
            else:
                loaded_model_names.add(model_name)
            imported_objects[model_name] = model

    for extra_import in settings.EXTRA_SHELLPLUS_IMPORTS:
        if isinstance(extra_import, basestring):
            obj = import_object(extra_import)
            name = extra_import.split('.')[-1]
        else:
            import_path, name = extra_import
            obj = import_object(import_path)
        imported_objects[name] = obj

    return imported_objects

