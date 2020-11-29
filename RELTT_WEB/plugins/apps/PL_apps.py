# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: ./build/RELTT_WEB/plugins/apps/PL_apps.py
# Compiled at: 2020-11-28 10:34:59
# Size of source mod 2**32: 573 bytes
import os
from RELTT_WEB.dbAPI import *

class PL_Cards:

    def __init__(self, pathtothumbnail, name, desc, ct) -> None:
        self.Thumbnail = pathtothumbnail
        self.name = name
        self.desc = desc
        self.cardtype = ct


class PL_App:

    def __init__(self):
        self.cards = []

    def addcard(self, card: PL_Cards):
        self.cards.append(card)


class PL_Apps:

    def __init__(self):
        self._PL_Apps__apps = []

    def addapp(self, application: PL_App):
        self._PL_Apps__apps.append(application)

    def __getapps(self):
        return self._PL_Apps__apps
# okay decompiling PL_apps.pyc
