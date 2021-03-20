import nanome
from nanome.util import Logs
from nanome.util import Color

import os

SELECTED_COLOR = Color.from_int(0x00ecc4ff)
DESELECTED_COLOR = Color.from_int(0xffffffff)
CHECKICON =  "GreenCheck.png"
LOCKICON = "Lock.png"
UNLOCKICON = "Unlock.png"
REFRESHICON = "Refresh.png"
QUESTIONMARKICON = "QuestionMark.png"

class GlycamCBMenu():
    def __init__(self, GlycamCB_plugin):
        self._menu = GlycamCB_plugin.menu
        self._plugin = GlycamCB_plugin
#        self._selected_mobile = [] # button
#        self._selected_target = None # button
        self._run_button = None
#        self._current_tab = "receptor" #receptor = 0, target = 1
#        self._drop_down_dict={"rotation":["None", "Kabsch","Quaternion"],"reorder_method":["None","Hungarian","Brute", "Distance"],\
#        "select":["None","Global"]} # select["Local"] in the future
#        self._current_reorder = "None"
#        self._current_rotation = "None"
#        self._current_select = "None"

#    def _request_refresh(self):
#        self._plugin.request_refresh()

    def update_button(self, button):
        self.update_content(button)

    def make_plugin_usable(self):
        self._menu.make_plugin_usable()

    # run the rmsd algorithm
#    def _run_rmsd(self):
#        if self.check_resolve_error():
#            self._plugin.update_structures_deep(self._selected_mobile + [self._selected_target])
#            self._plugin.run_rmsd([a.complex for a in self._selected_mobile], self._selected_target.complex)
#        else:
#            self.hide_loading_bar()

    # change the args in the plugin
    def update_args(self,arg,option):
        self._plugin.update_args(arg,option)

    def make_plugin_usable(self, state = True):
        self._run_button.unusable = not state
        self._plugin.update_button(self._run_button)

    # build the menu
    def build_menu(self):
        # refresh the lists
        def refresh_button_pressed_callback(button):
            self._request_refresh()
            
        # press the run button and run the algorithm
        def run_button_pressed_callback(button):
            # self.show_loading_bar()
            if self._selected_mobile != None and self._selected_target != None:
                self.show_loading_bar()
                self._plugin.select([x.complex for x in self._selected_mobile],self._selected_target.complex)
               
            else:
                self.check_resolve_error()
        
        # press the lock button and lock/unlock the complexes
        def lock_button_pressed_callback(button):
            def toggle_lock(complex_list):
                new_locked = not all(elem.locked for elem in complex_list)

                for x in complex_list:
                    x.locked = new_locked
                    # x.boxed = new_locked
                
                self.lock_img.add_new_image(os.path.join(os.path.dirname(__file__), (LOCKICON if new_locked else UNLOCKICON)))
                self._plugin.update_menu(self._menu)
                self._plugin.update_structures_shallow(complex_list)
                
            if self._selected_target != None and len(self._selected_mobile) != 0:
                complex_list = self._plugin._mobile + [self._plugin._target]
                complex_indexes = [complex.index for complex in complex_list]
                self._plugin.request_complexes(complex_indexes, toggle_lock)

            else:
                self.change_error("unselected")

        # global <=> local
        def global_local_button_pressed_callback(button):
            if self._plugin.args.select == "global":
                self.update_args("select","local")
                button.text.value.set_all("Local")
            else:
                self.update_args("select","global")
                button.text.value.set_all("Global")
            self._plugin.update_content(button)

        # import the json file of the new UI
        menu = nanome.ui.Menu.io.from_json(os.path.join(os.path.dirname(__file__), 'GlycamCB_pluginator.json'))
        self._plugin.menu = menu

        # create the layout node that contains select and run and refresh
        self.ln_select_run = menu.root.find_node("Refresh Run",True)

        # create the Run button
        self._run_button = menu.root.find_node("Run", True).get_content()
        self._run_button.register_pressed_callback(run_button_pressed_callback)

        # create the Refresh button
        refresh_button = menu.root.find_node("Clear", True).get_content()
#        refresh_button.register_pressed_callback(clear_button_pressed_callback)

        # create the lock button
#        lock_button = menu.root.find_node("Lock Button",True).get_content()
#        lock_button.register_pressed_callback(lock_button_pressed_callback)

        # add the lock icon,
#        self.lock_img = menu.root.find_node("Lock Image",True)
#        mobile_locked = False
#        for x in self._selected_mobile:
#            if x.locked:
#                mobile_locked = True

#        if len(self._selected_mobile) != 0 and self._selected_target != None and self._selected_target.locked and mobile_locked:
#            self.lock_img.add_new_image(file_path = os.path.join(os.path.dirname(__file__), LOCKICON))
#        else:
#            self.lock_img.add_new_image(file_path = os.path.join(os.path.dirname(__file__), UNLOCKICON))

#        self.ln_loading_bar = menu.root.find_node("Loading Bar",True)
#        self.ln_loading_bar.forward_dist = .003
#        self.loadingBar = self.ln_loading_bar.add_new_loading_bar()
#        self.loadingBar.description = "      Loading...          "

        # create the error message text
#        error_node = menu.root.find_node("Error Message")
#        self.error_message = error_node.get_content()

        self._menu = menu
        
