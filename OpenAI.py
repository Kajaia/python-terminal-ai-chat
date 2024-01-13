from ApiService import ApiService
import settings

class OpenAI(ApiService):
    base_url = settings.OPENAI_BASE_URL # API base url
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "OpenAI-Beta": settings.OPENAI_ASSISTANT_VERSION
    } # Bearer token and Assistant version
    assistant_id = settings.OPENAI_ASSISTANT_ID
    thread_id = None
    run_id = None
    
    def create_thread(self):
        res = super().post_data(url=self.base_url, endpoint='/threads', headers=self.headers)
        OpenAI.thread_id = res['id']

    def add_message_to_thread(self, question):
        json = {
            "role": "user",
            "content": question
        }
        return super().post_data(
            url=self.base_url,
            endpoint=f'/threads/{OpenAI.thread_id}/messages',
            json=json,
            headers=self.headers
        )

    def run_assistant(self):
        json = {"assistant_id": self.assistant_id}
        res = super().post_data(
            url=self.base_url,
            endpoint=f'/threads/{OpenAI.thread_id}/runs',
            json=json,
            headers=self.headers
        )
        OpenAI.run_id = res['id']

    def check_run_status(self):
        res = super().get_data(
            url=self.base_url,
            endpoint=f'/threads/{OpenAI.thread_id}/runs/{OpenAI.run_id}',
            headers=self.headers
        )
        return res['status']

    def display_assistant_response(self):
        res = super().get_data(
            url=self.base_url,
            endpoint=f'/threads/{OpenAI.thread_id}/messages',
            headers=self.headers
        )
        return res

    def retrieve_message(self, message_id):
        res = super().get_data(
            url=self.base_url,
            endpoint=f'/threads/{OpenAI.thread_id}/messages/{message_id}',
            headers=self.headers
        )
        return res
    
    def chat(self, question):
        json = {
            "model": settings.OPENAI_BASE_MODEL,
            "messages": [
                {"role": "system", "content": settings.OPENAI_INSTRUCTIONS},
                {"role": "user", "content": question}
            ]
        }
        OpenAI.headers.pop('OpenAI-Beta')
        res = super().post_data(url=self.base_url, endpoint=f'/chat/completions', json=json, headers=self.headers)
        return res
    
    def create_image(self, prompt):
        json = {"model": "dall-e-3", "prompt": prompt, "n": 1, "size": "1024x1024"}
        OpenAI.headers.pop('OpenAI-Beta')
        res = super().post_data(url=self.base_url, endpoint=f'/images/generations', json=json, headers=self.headers)
        return res