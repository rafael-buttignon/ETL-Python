from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from .extract_html import ExtractHtml

def test_extract_html():
    html_requester = HttpRequester()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(html_requester, html_collector)
    response = extract_html.extract_html()
    print()
    print(response)
