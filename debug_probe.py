"""Temporary probe: prints every raw event from LLMClient so we can see
whether the API returns text, an error, or nothing at all."""
import asyncio
from client.llm_client import LLMClient


async def main() -> None:
    client = LLMClient()
    try:
        count = 0
        async for event in client.chat_completion(
            [{"role": "user", "content": "say hi in five words"}], True
        ):
            count += 1
            text = event.text_delta.content if event.text_delta else None
            print(
                f"EVENT #{count} type={event.type} "
                f"text={text!r} error={event.error!r} "
                f"finish={event.finish_reason!r}",
                flush=True,
            )
        print(f"DONE total_events={count}", flush=True)
    finally:
        await client.close()


asyncio.run(main())
