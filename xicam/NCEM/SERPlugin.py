from xicam.plugins.DataHandlerPlugin import DataHandlerPlugin, start_doc, descriptor_doc, event_doc, stop_doc, \
    embedded_local_event_doc

import os
import fabio
import uuid
import re
import functools
from pathlib import Path
from ncempy.io import ser


class SERPlugin(DataHandlerPlugin):
    name = 'SERPlugin'

    DEFAULT_EXTENTIONS = ['.ser']

    def __call__(self, path, *args, **kwargs):
        return ser.fileSER(path).getDataset(index=kwargs.get('index', 0))[0]

    @staticmethod
    @functools.lru_cache(maxsize=10, typed=False)
    def parseDataFile(path):
        md = ser.fileSER(path).readHeader()
        return md

    @classmethod
    def getStartDoc(cls, paths, start_uid):
        return start_doc(start_uid=start_uid, metadata={'paths': paths})