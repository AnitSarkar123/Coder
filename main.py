from client.llm_client import LLMClient
import asyncio
async def main():
    client = LLMClient()
    messages = [
        {"role": "user", "content": "What's up bro?"},]
    await client.chat_completion(messages, stream=False)
    print("Done")
    
    
    
asyncio.run(main())