from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#buildKV = Builder.load_file("profilescreen.kv")


class ProfileScreen(Screen):
    pass


class DatabaseScreen(Screen):
    pass


screen_manager = ScreenManager()


screen_manager.add_widget(ProfileScreen(name="profile_screen"))
screen_manager.add_widget(DatabaseScreen(name="database_screen"))


class ProfileListButton(ListItemButton):
    pass


class ProfileDB(BoxLayout):
    profile_name_text_input = ObjectProperty()
    profile_list = ObjectProperty()

    def create_profile(self):
        # Get the profile's name from TextInputs
        profile_name = self.profile_name_text_input.text

        if profile_name != '':
            # Add to ListView
            self.profile_list.adapter.data.extend([profile_name])

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

    #def view_database(self):
     #   if self.profile_list.adapter.selection:

    def delete_profile(self):
        # If a list item is selected
        if self.profile_list.adapter.selection:

            # Get the text from the item selected
            selection = self.profile_list.adapter.selection[0].text

            # Remove the matching item
            self.profile_list.adapter.data.remove(selection)

            # Reset the ListView
            self.profile_list._trigger_reset_populate()


class ProfileScreen(App):
    def build(self):
        self.title = 'Profile Select'
        return ProfileDB()


screenobject = ProfileScreen()
screenobject.run()

