from src.drivers.tests.http_requester import HttpRequesterSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.stages.extract.contracts.extract_contract import ExtractContract
from .extract_html import ExtractHtml
from src.errors.extract_error import ExtractError

def test_extract_html():
    html_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(html_requester, html_collector)
    response = extract_html.extract_html()

    assert isinstance(response, ExtractContract)
    assert html_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essential_information_attributes

def test_extract_html_error():
    html_requester = 'IssoVaiDarErro'
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(html_requester, html_collector)

    try:
        extract_html.extract_html()
    except Exception as exception:
        assert isinstance(exception, ExtractError)


