from PySide6.QtGui import QGuiApplication
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtQml import QQmlApplicationEngine
import sys

from pathlib import Path
import qml_element

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / 'main.qml'
    # engine.addImportPath("./")
    engine.addImportPath("qrc:/")
    engine.load(qml_file)
    print(engine.rootObjects())
    if not engine.rootObjects():
        print(2222222)
        sys.exit(-1)
    app.exec()
    
