import globalshared
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.filechooser import FileChooserListView
import os

def main():

    class NoteWindow(BoxLayout):
        note_text = StringProperty("No Note Opened.")

        def update(self, content):
            print("moment")
            note_text = content
            self.root.ids.note_text_in_window.text = note_text

    class FileBrowser(FileChooserListView):
        def selected(self, fileloc):
            try:
                filename = fileloc[0]
            except:
                return
            file = open(filename, 'r')
            content = file.read()
            file.close()
            globalshared.note = content
            NoteWindow.update(NoteWindow, content)

    class GlobalLayout(BoxLayout):
        pass
	
    class LoomApp(App):
        pass

    LoomApp().run()

if __name__ == "__main__":
	main()
