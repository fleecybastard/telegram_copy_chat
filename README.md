# SCRIPT TO COPY ANY CHAT IN TELEGRAM TO ANOTHER CHAT
## Copies the following types of messages:
1. Text messages
2. Audio files with captions
3. Images with captions
4. Videos with captions
5. Documents with captions
6. Voices
7. Video Notes

## HOW TO RUN
1. Create an app in telegram (Quick guide https://core.telegram.org/api/obtaining_api_id)
2. Insert your **API_ID** and **API_HASH** into **main.py** file and **TO_CHAT_ID** - chat id of the chat you want messages to be sent to
3. Create and activate venv
```bash 
python -m venv venv   
venv\Scripts\activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run main.py
```bash
python main.py
```