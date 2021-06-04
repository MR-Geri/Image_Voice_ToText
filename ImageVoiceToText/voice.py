from typing import Union
import speech_recognition as sr


r = sr.Recognizer()


def voice_to_text(path: str) -> Union[None, str]:
    try:
        sample_audio = sr.AudioFile(path)
        with sample_audio as audio_file:
            r.adjust_for_ambient_noise(audio_file)
            audio_content = r.record(audio_file)
        query = r.recognize_google(audio_content, language='ru-RU')
        return query.strip()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
