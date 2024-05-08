from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from presidio_analyzer import Pattern, PatternRecognizer
from presidio_anonymizer.entities import OperatorConfig
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
from faker import Faker
from app import *


polish_phone_numbers_pattern = Pattern(
    name="polish_phone_numbers_pattern",
    regex="(?<!\w)(\(?(\+|00)?48\)?)?[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}(?!\w)",
    score=1,
)

# Define the recognizer with one or more patterns
polish_phone_numbers_recognizer = PatternRecognizer(
    supported_entity="POLISH_PHONE_NUMBER", patterns=[polish_phone_numbers_pattern]
)



fake = Faker(locale="pl_PL")


def fake_polish_phone_number(_=None):
    return fake.phone_number()


fake_polish_phone_number()

new_operators = {
    "POLISH_PHONE_NUMBER": OperatorConfig(
        "custom", {"lambda": fake_polish_phone_number}
    )
}

anonymizer = PresidioAnonymizer()
anonymizer.add_recognizer(polish_phone_numbers_recognizer)
anonymizer.add_operators(new_operators)
anonymizedtext=anonymizer.anonymize(pdftext)

anonymizer_with_memory = PresidioReversibleAnonymizer()

deanonymizedtext=anonymizer_with_memory.anonymize(anonymizedtext)
