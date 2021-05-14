import httpx
from typing import Optional

http = httpx.AsyncClient(http2=True)

api_url = "https://api.itaykibotsonetwo.ml"


class multiapi:
    async def get_exec_langs():
        a = (await http.get(f"{api_url}/execlangs")).json()
        await http.aclose()
        return a["langs"]

    async def exec_code(lang: str, code: str):
        if not (lang or code):
            return "please specify the code or the language"
        a = (await http.get(f"{api_url}/exec?lang={lang}&code={code}")).json()
        await http.aclose()
        if "Errors" in a:
            return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Errors:\n\n {a['Errors']}"
        elif "Stats" in a:
            return f"Language: {a['Language']}\n\n Code:\n\n {a['Code']}\n\n Results:\n\n {a['Results']}\n\n Stats:\n\n {a['Stats']}"
        else:
            return a["langs"]

    async def ocr(url: str):
        if not url:
            return "please specify the url"
        a = (await http.get(f"{api_url}/ocr?url={url}")).json()
        await http.aclose()
        if "ocr" in a:
            return f"ocr: {a['ocr']}"
        elif "error" in a:
            return f"Error: {a['error']}"

    async def translate(
        text: str, fromlang: Optional[str] = None, lang: Optional[str] = "en"
    ):
        if not text:
            return "please specify the url"
        a = (
            (await http.get(f"{api_url}/tr?text={text}&lang={lang}")).json()
            if not fromlang
            else (
                await http.get(
                    f"{api_url}/tr?text={text}&fromlang={fromlang}&lang={lang}"
                )
            ).json()
        )
        await http.aclose()
        return f"Text: \n\n{a['text']}\n\nfrom language: {a['from_language']}\n\nto language: {a['to_language']}"
