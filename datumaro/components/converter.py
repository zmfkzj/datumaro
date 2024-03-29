
# Copyright (C) 2019-2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

import logging as log
import os
import os.path as osp
import shutil

from datumaro.components.cli_plugin import CliPlugin
from datumaro.util.image import save_image, ByteImage


class Converter(CliPlugin):
    DEFAULT_IMAGE_EXT = None

    @classmethod
    def build_cmdline_parser(cls, **kwargs):
        parser = super().build_cmdline_parser(**kwargs)
        parser.add_argument('--save-images', action='store_true',
            help="Save images (default: %(default)s)")
        parser.add_argument('--image-ext', default=None,
            help="Image extension (default: keep or use format default%s)" % \
                (' ' + cls.DEFAULT_IMAGE_EXT if cls.DEFAULT_IMAGE_EXT else ''))

        return parser

    @classmethod
    def convert(cls, extractor, save_dir, **options):
        converter = cls(extractor, save_dir, **options)
        return converter.apply()

    def apply(self):
        raise NotImplementedError("Should be implemented in a subclass")

    def __init__(self, extractor, save_dir, save_images=False,
            image_ext=None, default_image_ext=None):
        default_image_ext = default_image_ext or self.DEFAULT_IMAGE_EXT
        assert default_image_ext
        self._default_image_ext = default_image_ext

        self._save_images = save_images
        self._image_ext = image_ext

        self._extractor = extractor
        self._save_dir = save_dir

    def _find_image_ext(self, item):
        id_ext = item.id.split('.')[-1]
        if id_ext.lower() in ['jpg', 'jpeg', 'png', 'bmp']:
            return ''

        src_ext = None
        if item.has_image:
            src_ext = item.image.ext
        
        return self._image_ext or src_ext or self._default_image_ext

    def _make_image_filename(self, item):
        return item.id + self._find_image_ext(item)

    def _save_image(self, item, path=None):
        if not item.image.has_data:
            log.warning("Item '%s' has no image", item.id)
            return

        path = path or self._make_image_filename(item)

        src_ext = item.image.ext.lower()
        dst_ext = osp.splitext(osp.basename(path))[1].lower()

        os.makedirs(osp.dirname(path), exist_ok=True)
        if src_ext == dst_ext and osp.isfile(item.image.path):
            shutil.copyfile(item.image.path, path)
        elif src_ext == dst_ext and isinstance(item.image, ByteImage):
            with open(path, 'wb',encoding='utf-8') as f:
                f.write(item.image.get_bytes())
        else:
            save_image(path, item.image.data)
