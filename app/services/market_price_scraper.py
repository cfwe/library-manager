import httpx
from bs4 import BeautifulSoup
from typing import Optional
import re


async def scrape_bookoff_online_price(isbn: str) -> Optional[int]:
    """
    Scrapes the used book price from Book-Off Online using an ISBN.

    Args:
        isbn: The ISBN code of the book.

    Returns:
        The price as an integer if found, otherwise None.
    """
    search_url = f"https://shopping.bookoff.co.jp/search/keyword/{isbn}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(search_url, headers=headers, follow_redirects=True)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "lxml")
            
            # 「商品が見つからない」旨のメッセージがあるか先に確認する
            no_result_div = soup.select_one("div.mainContent__search")
            if no_result_div and "お探しの商品は見つかりませんでした" in no_result_div.get_text():
                return None

            # 1. 商品一覧ページの価格要素を探す (パターンA)
            price_element = soup.select_one("p.item-price__price")

            # 2. 見つからなければ、商品一覧ページの価格要素を探す (パターンB)
            if not price_element:
                price_element = soup.select_one("p.productItem__price")
                # print("2.price_element:", price_element)

            # 3. それでも見つからなければ、商品詳細ページの価格要素を探す
            if not price_element:
                price_element = soup.select_one("p.mainprice")

            # すべてのパターンで見つからなければNoneを返す
            if not price_element:
                return None
                
            # 要素内のテキストから最初の数値部分を抽出する
            price_text = re.sub(r".*?([0-9,]+).*", r"\1", price_element.get_text())
            price_text = price_text.replace(",", "") # カンマも削除

            return int(price_text)
        except (httpx.HTTPStatusError, ValueError, TypeError, IndexError):
            return None
