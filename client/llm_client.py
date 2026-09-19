from openai import AsyncOpenAI
from typing import Any
class LLMClient:
    def __init__(self) -> None:
        self._client: AsyncOpenAI | None = None
        # self._max_retries: int = 3
        # self.config = config

    def get_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                api_key="",  # "sk-or-v1-20c17f48aafd0338a3b88"
                base_url="https://openrouter.ai/api/v1",  # "https://openrouter.ai/api/v1"
            )
        return self._client

    async def close(self) -> None:
        if self._client:
            await self._client.close()
            self._client = None
            
    async def chat_completion(
        self,
        message:list[dict[str,Any]],
        stream:bool =True
    ):
        Client =self.get_client()
        kwargs = {
            "model": "",
            "messages": message,
            "stream": stream,
        }
        if stream:
            await self._stream_response(client=Client, kwargs=kwargs)
        else:
            await self._non_stream_response(client=Client, kwargs=kwargs)
            
    async def _stream_response(self, client: AsyncOpenAI, kwargs: dict[str, Any]):
        # Implement streaming response logic here
        response = await client.chat.completions.create(**kwargs)
        async for chunk in response:
            print(chunk)
    async def _non_stream_response(
        self,
        client: AsyncOpenAI,
        kwargs :dict[str, Any],
        ):
        response = await client.chat.completions.create(**kwargs)
        print(response)