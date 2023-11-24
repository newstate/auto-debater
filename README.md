# auto-debater

This repo is aimed at simulating debates or conversations between politicians. It was made on the occasion of the Dutch elections in November 2023. The repo contains sample data that was made while simulating a debate between two Dutch politicians.

The [OpenAI assistants API](https://platform.openai.com/docs/api-reference/assistants) which is currently in beta is the foundation of this experiment. See also [the respective python cookbook](https://cookbook.openai.com/examples/assistants_api_overview_python) The idea is to equip assistants with a knowledge base by uploading documents for retrieval, in this case: the party programs of the parties that the assistants represent, thereby allowing them to promote and defend these in a debate.

It contains the following functionality:
- Starting a debate between two assistants using an initial prompt by the user to set the stage.
- Logging the messages (conversation) to a text file, including the references to the documents they have quoted in their output.
- Listening to the debate on your own computer (tested on Raspberry Pi 4, 2GB).

It requires the following to work:
- Assistants configured on the OpenAI platform (web form) or with the OpenAI API, and uploaded documents. I did not see a way to configure web search, which could be helpful to include data on recent events, for example if a politician made an important statement.
- For listening and streaming: voices created with the elevenlabs VoiceLab feature. This requires about 2-5 minutes of sample data of the politicians you want to mimick.

Not included in this repo but required for streaming:
- Streaming the debate via a RTMP server [(I used nginx)](https://www.itsfullofstars.de/2020/01/nginx-with-rtmp-on-raspberry-pi-as-a-streaming-server-for-obs/) and [Restreamer software (by Datarhei)](https://docs.datarhei.com/restreamer/installing/raspberry-pi-arm).

Notes on development:
The latest GPT-4 model's update was in April 2023 and when asking the model flat out it has internal knowledge of nearly all Dutch political party leaders.
The elections were on November 22, so the votes are in and now it is time to form a coalition and a government. This looks like it will be challenging considering all parties will have to make big compromises if they want to work together.

Next on the planning:
- Consolidate listen and stream script into one script with the option to pass arguments when running either to simply log the conversation or also listen to it or also stream it.
- Create an assistant for all the parties that have to try and form a government and create a notebook to run an autogen script that orchestrates the formation conversations. See [autogen's example on using assistants.](https://github.com/microsoft/autogen/blob/main/notebook/agentchat_oai_assistant_retrieval.ipynb)
