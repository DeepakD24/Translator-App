from django.shortcuts import render
from translate import Translator

def home(request):
    result = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.POST.get("translate", "")
        language = request.POST.get("language", "")

        if input_text and language:
            try:
                translator = Translator(to_lang=language)
                result = translator.translate(input_text)
            except Exception as e:
                result = f"Translation error: {str(e)}"

    return render(request, "main/index.html", {
        "input_text": input_text,
        "result": result,
    })
