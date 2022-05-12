from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.extract.contracts.extract_contract import ExtractContract
from .extract_html import ExtractHtml
from src.errors.extract_error import ExtractError

def test_extract_html():
    html_requester = HttpRequester()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(html_requester, html_collector)
    response = extract_html.extract_html()
    print()
    print(response)
    print(response.extraction_date)

    assert isinstance(response, ExtractContract)

def test_extract_html_error():
    html_requester = 'IssoVaiDarErro'
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(html_requester, html_collector)

    try:
        extract_html.extract_html()
    except Exception as exception:
        assert isinstance(exception, ExtractError)


