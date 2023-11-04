import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 1000
    height: 500
    title: "SmartC"
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/Tom Clancy's Rainbow Six® Siege2023-9-5-22-35-50.jpg"
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }

                text: "16:38:33"
                font.pixelSize: 24
                color: "white"
            }
        }
    }
}
