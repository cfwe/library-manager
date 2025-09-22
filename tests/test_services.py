import pytest
from app.services.market_price_scraper import scrape_bookoff_online_price

# テストケース: (ISBN, 期待される中古価格, 期待される定価)
# 外部サイトの状況により、価格は変動する可能性があります。
book_test_cases = [
    ("9784053049032", 550, 1320),
    # ("4910066630553", 440, 1320), # JANコードであり、中古在庫がないためテストから除外
    ("9784789846691", 3960, 3960),
    ("9784274233159", 4070, 6160),
    ("9784501117207", 3135, 3740),
    ("9784488025694", 1375, 1870),
    ("9784103330639", 550, 2090),
]


@pytest.mark.parametrize("isbn, expected_market_price, expected_list_price", book_test_cases)
@pytest.mark.anyio
async def test_scrape_bookoff_online_price(isbn, expected_market_price, expected_list_price):
    """
    scrape_bookoff_online_priceがBook-Off Onlineから正しく価格情報を取得できるかテストする。
    このテストは外部サイトに依存します。
    """
    prices = await scrape_bookoff_online_price(isbn)

    assert prices is not None, f"ISBN {isbn} の価格情報が取得できませんでした。"
    assert prices["market_price"] == expected_market_price, f"ISBN {isbn} の中古価格が期待値と異なります。"
    assert prices["list_price"] == expected_list_price, f"ISBN {isbn} の定価が期待値と異なります。"
