import user.network as network
import user.graphic as graphic
import user.config as config
import user.speech as speech


remote_user_id = config.get("saynote.remoteUser")
my_user_id = config.get("saynote.myUser")
backend = config.get("saynote.backend")

my_note_text = fetch(backend + "/getNote?userId=" + my_user_id).text()

speech_client = speech.AudioClient()
speech_client.encoding = "LINEAR16"
speech_client.sampleRate = 44100
speech_client.languageCode = "en_US"

speech_recog = {}


def start_listening():
    speech_recog = speech_client.recognize(0)  # listen indefinitely


def stop_listening():
    speech_client.terminate()
    
    send_note = " ".join(speech_recog["final"])
    fetch(backend + "/setNote?userId=" + remote_user_id, {
        "method": "post",
        "data": { "note": send_note },
    })

layout = graphic.createLayout(graphic.LayoutType.LinearVertical)

my_note = graphic.createText(my_note_text)
start_button = graphic.createButton("start note", "start_listening")
stop_button = graphic.createButton("end note", "stop_listening")

graphic.addComponentToLayout(layout, my_note)
graphic.addComponentToLayout(layout, start_button)
graphic.addComponentToLayout(layout, stop_button)

render(layout)
import user.network as network
import user.graphic as graphic
import user.config as config
import user.speech as speech


speech_client = speech.AudioClient()
speech_client.encoding = "LINEAR16"
speech_client.sampleRate = 44100
speech_client.languageCode = "en_US"

speech_recog = {}


def start_listening():
    speech_recog = speech_client.recognize(0)  # listen indefinitely


def stop_listening():
    speech_client.terminate()
    send_note = " ".join(speech_recog["final"])
    fetch(backend + "/setNote?userId=" + remote_user_id, {
        "method": "post",
        "data": { "note": send_note },
    })

"""
Called every render cycle, must be implemented
"""
def on_tick():
    remote_user_id = config.get("saynote.remoteUser")
    my_user_id = config.get("saynote.myUser")
    backend = config.get("saynote.backend")

    my_note_text = fetch(backend + "/getNote?userId=" + my_user_id).text()

    layout = graphic.createLayout(graphic.LayoutType.LinearVertical)

    my_note = graphic.createText(my_note_text)
    start_button = graphic.createButton("start note", "start_listening")
    stop_button = graphic.createButton("end note", "stop_listening")

    graphic.addComponentToLayout(layout, my_note)
    graphic.addComponentToLayout(layout, start_button)
    graphic.addComponentToLayout(layout, stop_button)

    render(layout, 200, 400)
