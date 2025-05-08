import wikipediaapi

def fetch_wikipedia_summary(page_title, language='ja'):
    """
    Wikipediaページの概要を取得します。

    :param page_title: Wikipediaページのタイトル
    :param language: 言語コード（デフォルトは 'ja' 日本語）
    :return: ページの概要またはエラーメッセージ
    """
    # ユーザーエージェントを指定
    user_agent = "MyWikipediaApp/1.0 (https://example.com; myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(language=language, user_agent=user_agent)
    page = wiki_wiki.page(page_title)

    if page.exists():
        return page.summary
    else:
        return f"ページ '{page_title}' は {language} のWikipediaに存在しません。"

if __name__ == "__main__":
    title = input("Wikipediaページのタイトルを入力してください: ")
    lang = input("言語コードを入力してください（デフォルトは 'ja'）: ") or 'ja'
    summary = fetch_wikipedia_summary(title, lang)
    print("\n概要:")
    print(summary)