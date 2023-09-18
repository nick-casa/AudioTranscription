import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "YOUR API KEY HERE"


def transcribe_audio(audio_path):
    """Transcribes audio using a hypothetical API and returns the text."""
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript.get("text", "")


def summarize_text(text):
    """Summarizes text using OpenAI's ChatGPT and returns the summary."""
    prompt = f"Please summarize the following notes:\n{text}"
    summary = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,  # You can set this to a higher or lower value
    )
    return summary.choices[0].text.strip()


# Create 'text' and 'summary' folders if they don't exist
if not os.path.exists("text"):
    os.makedirs("text")

if not os.path.exists("summary"):
    os.makedirs("summary")

# Loop through all audio files in the 'audio' folder
for filename in os.listdir("audio"):
    if filename.endswith((".mp3", ".m4a", ".wav")):  # Add other audio formats if needed
        print(f"Transcribing {filename}...")
        # Transcribe the audio file
        text = transcribe_audio(os.path.join("audio", filename))
        # Save the transcription to the 'text' folder
        text_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join("text", text_filename), "w") as f:
            f.write(text)

        # Summarize the transcribed text
        print(f"Summarizing {filename}...")
        summary = summarize_text(text)
        # Save the summary to the 'summary' folder
        summary_filename = os.path.splitext(filename)[0] + "_summary.txt"
        with open(os.path.join("summary", summary_filename), "w") as f:
            f.write(summary)

print("Transcription and summarization completed for all audio files.")
