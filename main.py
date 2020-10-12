import user.network as network
import user.graphic as graphic
import user.config as config
import user.speech as speech

speech_client = speech.AudioClient()


def start_listening():
    speech_client.startClient(0)  # listen indefinitely


def stop_listening():
    backend = config.get("saynote.backend")

    speech_client.stopClient()
    results = speech_client.getNaturalText().get("final")
    final_sentence = max(results.items(), key=lambda item:item[1])
    fetch(backend + "/setNote?userId=" + remote_user_id, {
        "method": "post",
        "data": { "note": final_sentence },
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
