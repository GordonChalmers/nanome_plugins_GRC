import nanome
from nanome.util import Logs

import re
import os
from os import path
from functools import partial

import json
import requests
import tempfile
import traceback

#from .Settings import Settings

import sys
import time
# import math
# from .rmsd_calculation import *
# from rmsd_menu import RMSDMenu
#from .GlycamCB_menu import GlycamCBMenu
from GlycamCB_menu import GlycamCBMenu
# from . import rmsd_helpers as help
#from nanome.util import Logs
# from .quaternion import Quaternion
import numpy as np
# from . import rmsd_selection as selection
# from itertools import combinations

NAME = "Glycam Carbohydrate Builder"
DESCRIPTION = "Construct oligasaccharide structure pdb from a sequence."
CATEGORY = "Carbohydrate Tools"
HAS_ADVANCED_OPTIONS = False

MENU_PATH = path.join(path.dirname(path.realpath(__file__)), "menus/GlycamCB_menu.json")

class GlycamCB(nanome.PluginInstance):
    def start(self):
        Logs.debug("Start Glycam Carbohydrate Builder Plugin")
#        self.args = GlycamCB.Args()
        self._loading = False
        self._fields = {}
        self._menu = GlycamCBMenu(self)
        self._menu.build_menu()
#        self._menu = nanome.ui.Menu.io.from_json(MENU_PATH)
        self.open_menu()
#        self._menu = GlycamCBMenu(self)
#        self._menu.build_menu()
#        self.selected_before = []
#        self._mobile = []
#        self._target = None
        # passed from rmsd_menu.py to compare the index 
        # and autoselect entry menu complex
#        self.compare_index = None

#        print(self._menu.title)
        
    def on_run(self):
#        self.open_menu()
        menu = self.menu
        menu.enabled = True
#        self._menu._request_refresh()

    def open_menu(self, menu=True):
        self._menu.enabled = True
#        self.set_file_type(self.__filetype)
#        self.render_fields()
        
#    def on_complex_added(self):
#        nanome.util.Logs.debug("Complex added: refreshing")
#        self.request_refresh()

#    def on_complex_removed(self):
#        nanome.util.Logs.debug("Complex removed: refreshing")
#        self.request_refresh()

#    def request_refresh(self):
#        self._menu._selected_mobile = []
#        self._menu._selected_target = None
#        self.request_complex_list(self.on_complex_list_received)
#        nanome.util.Logs.debug("Complex list requested")

    def update_button(self, button):
        self.update_content(button)

    def make_plugin_usable(self):
        self._menu.make_plugin_usable()

#    class Args(object):
#        def __init__(self):
#            self.rotation = "kabsch" #alt: "quaternion", "none"
#            self.reorder = False
#            self.reorder_method = "hungarian" #alt "brute", "distance"
#            self.select = "global"
#            self.use_reflections = False # scan through reflections in planes (eg Y transformed to -Y -> X, -Y, Z) and axis changes, (eg X and Z coords exchanged -> Z, Y, X). This will affect stereo-chemistry.
#            self.use_reflections_keep_stereo = False # scan through reflections in planes (eg Y transformed to -Y -> X, -Y, Z) and axis changes, (eg X and Z coords exchanged -> Z, Y, X). Stereo-chemistry will be kept.
            #exclusion options
#            self.no_heterogens = True
#            self.no_hydrogen = True
#            self.selected_only = True
#            self.backbone_only = True
#            self.align = True
#            self.align_box = False
#            self.align_sequence = True

#        @property
#        def update(self):
#            return self.align

#        def __str__(self):
#            ln = "\n"
#            tab = "\t"
#            output  = "args:" + ln
#            output += tab + "rotation:" + str(self.rotation) + ln
#            output += tab + "reorder:" + str(self.reorder) + ln
#            output += tab + "reorder_method:" + str(self.reorder_method) + ln
#            output += tab + "use_reflections:" + str(self.use_reflections) + ln
#            output += tab + "use_reflections_keep_stereo:" + str(self.use_reflections_keep_stereo) + ln
#            output += tab + "no_hydrogen:" + str(self.no_hydrogen) + ln
#            output += tab + "selected_only:" + str(self.selected_only) + ln
#            output += tab + "backbone_only:" + str(self.backbone_only) + ln
#            output += tab + "align:" + str(self.align) + ln
#            output += tab + "align box:" +str(self.align_box) + ln
#            return output


def main():
    plugin = nanome.Plugin("GlycamCB", "Input an oligasaccharide sequence and obtain a minimized pdb.", "pdb_from_sequence", False)
    plugin.set_plugin_class(GlycamCB)
    plugin.run('127.0.0.1',8888)

if __name__ == "__main__":
    main()
