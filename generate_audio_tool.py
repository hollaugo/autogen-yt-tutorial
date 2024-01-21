from pathlib import Path
from openai import OpenAI
import os

def text_to_speech(input_text, file_name="speech.mp3", model="tts-1", voice="alloy"):
    """
    Convert text to speech using OpenAI's speech synthesis API and save as an MP3 file.

    Parameters:
    input_text (str): The text to be converted to speech.
    file_name (str, optional): Name of the output MP3 file. Defaults to 'speech.mp3'.
    model (str, optional): The model to be used for speech synthesis. Defaults to 'tts-1'.
    voice (str, optional): The voice to be used. Defaults to 'alloy'.
    
    Returns:
    str: Path to the saved MP3 file or an error message.
    """

    try:
        # Initialize the OpenAI client
        client = OpenAI()

        # Define the path for the output file
        speech_file_path = Path(__file__).parent / file_name

        # Create the speech synthesis request
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=input_text
        )

        # Save the response to a file
        response.stream_to_file(speech_file_path)

        return str(speech_file_path)

    except Exception as e:
        # Return the error message in case of an exception
        return f"An error occurred: {str(e)}"

# Example usage
#result = text_to_speech("Today is a wonderful day to build something people love!")
