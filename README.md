# Autogen Studio - Introduction
This repo contains information about setting up and using the Autogen Studio to create multi-agent applications

  ```bash
  python3 -m venv autogen-yt-demo
  source autogen-yt-env-venv/bin/activate
  ```

Next, we get to install Autogen Studio:

  ```bash
  pip install autogenstudio
  ```

Setup your environment variables:

  ```bash
  export OPENAI_API_KEY=<your_api_key>
  ```

To run Autogen Studio, use:

  ```bash
  autogenstudio ui --port 8081
  ```

Also, note that there are two tools which you can add to your AutoGen skills.:

- `generate_audio_tool.py`
- `tavily_search_tool`
