import user.network as network
import user.graphic as graphic
import user.config as config
import user.speech as speech


def start_listening():
    # Could provide `speech.hasClient` or similar to check, or override the previous if called multiple times
    # Create an audio backend that is managed by the SDK, 
    #  will find an available audio stream and hook it to the client automatically.
    speech.startClient()  

def stop_listening():
    backend = config.get("saynote.backend")

    send_note = speech.getNaturalText() # Auto add punctuations, context-aware phrasing etc.
    speech.stopClient()

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
