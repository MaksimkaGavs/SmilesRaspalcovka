__version__ = (1, 0, 0)
from .. import loader, utils
from telethon.tl.types import Message


@loader.tds
class smiles(loader.Module):

    strings = {"name": "smiles"}

    async def smilecmd(self, message: Message) -> None:
        first = [
            "👍", "👎", "🤞", "✌️", "🤟", "☝️", "🤙", "👌", "🖕"
        ]
        llslsls = await self.animate(
            message,
            first,
            interval=0.3,
            inline=False,
        )
        await llslsls.edit(f"<b>распальцовка окончена </b>")