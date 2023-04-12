bl_info = {
    "name": "Cross Platform PyQt6 Addon Example",
    "description": "",
    "author": "Iyad Ahmed (iyadahmed430@gmail.com)",
    "version": (0, 0, 1),
    "blender": (3, 4, 1),
    "location": "",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Scripting",
}

import os
import site
from pathlib import Path

# Add bundled packages directory to import search path
# NOTE: this path has to match the directory where the bundled packages are installed to
# the path has to be under the addon directory of course
site.addsitedir((Path(__file__).parent / "extern").as_posix())

# Set plugin path to ensure we are using bundled plugins
# (see https://github.com/iyadahmed/blender_pyqt_example_addon/issues/1#issue-1663320484)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = (Path(__file__).parent / "extern/PyQt6/Qt6/plugins/platforms").as_posix()

from PyQt6.QtWidgets import QApplication, QLabel
import bpy


def event_loop_timer():
    QApplication.processEvents()
    return 0


# Start a QApplication and loop timer if not started
if QApplication.startingUp():
    app = QApplication([])
    bpy.app.timers.register(event_loop_timer)

widgets = []


def register():
    label = QLabel("Hello from Qt: Addon was registered!")
    label.show()
    # We have to keep widgets stored somewhere,
    # otherwise they will get garbage collected and destroyed
    widgets.append(label)


def unregister():
    pass
