import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Hellow World"

    readonly property list<string> texts: ["Olá Mundo", "Hello World", "Bonjour le Monde", "Hola Mundo", "Hei Maailma"]

    function setText() {
        var i = Math.round(Math.random() * 4)
        text.text = texts[i]
    }
    
    ColumnLayout {
        anchors.fill: parent

        Text{
            id: text
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }
        Button {
            text: "Click Me"
            Layout.alignment: Qt.AlignHCenter
            onClicked: setText()
        }
    }
}