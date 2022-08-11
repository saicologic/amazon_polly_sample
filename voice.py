import sys
import os
import subprocess
import fire

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir

class Polly:
    def __init__(self):
        pass

    def synthesize_speech(self, text):
        engine = 'neural'

        try:
            session = Session(profile_name=os.environ.get('AWS_PROFILE'))
        except Exception as error:
            print(error)
            sys.exit(-1)

        polly = session.client('polly')

        try:
            response = polly.synthesize_speech(
                Engine=engine,
                LanguageCode="ja-JP",
                Text=text,
                TextType="text",
                OutputFormat="mp3",
                VoiceId="Takumi"
            )
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)
        return response

    def save_audio(self, response):
        output_path = "./output"
        output_file = "output.mp3"
        output = os.path.join(output_path, output_file)

        if os.path.isfile(output):
            os.remove(output)

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:


                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    print(error)
                    sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)
        return output

    def play_audio(self, output):
        subprocess.call(["open", output])

def say(text):
    polly = Polly()
    response = polly.synthesize_speech(text)
    output = polly.save_audio(response)
    polly.play_audio(output)

if __name__ == "__main__":
    fire.Fire()
