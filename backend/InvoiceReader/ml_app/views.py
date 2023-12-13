import os
import django
from .models import Invoice
import requests
import base64



API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-document-qa"
headers = {"Authorization": "Bearer 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"}



def query_invoice_image(image_path):
    questions = [
        "What is the total?",
        "When is the duedate?",
        "Who is the bill to?",
        "Who or what company is the invoice from?",
        "What is the invoicenumber?",
    ]

    answers = []
    for question in questions:
        response = query_invoice_image_question(image_path, question)
        try:
            answer = response[0].get('answer', None)
        except (IndexError, TypeError):
            answer = None
        answers.append(answer)

    print(answers[4])

    # Handle the case where 'answers' list does not contain the expected values
    if len(answers) == len(questions) and all(answer is not None for answer in answers):
        # Create an Invoice object and save it to the database
        new_invoice = Invoice(
            invoiceNumber=answers[4],
            receiver=answers[2],
            sender=answers[3],
            price=answers[0],
            dueDate=answers[1]
        )
        new_invoice.save()

    return answers

def query_invoice_image_question(image_path, question):
    with open(image_path, "rb") as f:
        img = f.read()
        payload = {
            "inputs": {
                "image": base64.b64encode(img).decode("utf-8"),
                "question": question,
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    
