import os, sys, pkgutil
from importlib import import_module
from pathlib import Path


CONFIGURED_STAGES = []
for (_, name, _) in pkgutil.iter_modules([Path(__file__).parent]):
    if name != "common":
        CONFIGURED_STAGES.append(name)

STAGE = os.environ.get("STAGE")

if STAGE not in CONFIGURED_STAGES:
    STAGE = "local"

imported_module = import_module('config.settings.%s' % STAGE, package=__name__)

for attribute_name in dir(imported_module):
    attribute_value = getattr(imported_module, attribute_name)
    setattr(sys.modules[__name__], attribute_name, attribute_value)
