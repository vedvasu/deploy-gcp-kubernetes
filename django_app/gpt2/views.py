import time

from datetime import datetime
from django.shortcuts import render
from transformers import pipeline, set_seed

from gpt2.models import GeneratedText

set_seed(42)


def generate(request):
    """
    API to take input text and return generated sentence

    :param request: API request
    :return: Rendered output json

    """

    text = request.GET.get("text")

    if not text:
        return render(
            request, 'index.html'
        )

    else:
        t1 = time.time()

        # GPT2 Text Generator model from hugging-face
        generator = pipeline('text-generation', model='gpt2-medium')
        output = generator(text, max_length=50, num_return_sequences=3)

        prediction_time_sec = int(time.time() - t1)

        # Transform output
        output = {
            'text_{}'.format(i): ' '.join(output[i]['generated_text'].split('.')[:-1]) + '.'
            for i in range(len(output))
        }

        # Update Database
        db_transaction = GeneratedText(
            created_at=datetime.utcnow(),
            input_text=text,
            generated_text_1=output['text_0'],
            generated_text_2=output['text_1'],
            generated_text_3=output['text_2'],
            prediction_time_sec=prediction_time_sec,
        )
        db_transaction.save()

        return render(
            request, 'jsonrender.html', output
        )
