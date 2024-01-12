from decouple import config

APP_NAME=config('APP_NAME', default="My app")

OPENAI_BASE_URL=config('OPENAI_BASE_URL')
OPENAI_API_KEY=config('OPENAI_API_KEY')
OPENAI_ASSISTANT_VERSION=config('OPENAI_ASSISTANT_VERSION')
OPENAI_ASSISTANT_ID=config('OPENAI_ASSISTANT_ID')