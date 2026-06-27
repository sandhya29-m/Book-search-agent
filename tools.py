import requests
import time

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"


def book_search(query):

    headers = {
        "User-Agent": "BookSearchAgent/1.0"
    }

    for attempt in range(3):

        try:

            response = requests.get(
                GOOGLE_BOOKS_URL,
                params={"q": query},
                headers=headers,
                timeout=20
            )

            if response.status_code == 429:
                time.sleep(2)
                continue

            response.raise_for_status()

            data = response.json()

            if "items" not in data:
                return "No books found."

            books = []

            for item in data["items"][:5]:

                info = item.get("volumeInfo", {})

                title = info.get("title", "Unknown")
                authors = ", ".join(info.get("authors", ["Unknown"]))
                publisher = info.get("publisher", "Unknown")
                published = info.get("publishedDate", "Unknown")
                rating = info.get("averageRating", "N/A")
                pages = info.get("pageCount", "Unknown")

                description = info.get(
                    "description",
                    "No description available."
                )

                if len(description) > 250:
                    description = description[:250] + "..."

                books.append(
                    f"""
Title: {title}
Author(s): {authors}
Publisher: {publisher}
Published: {published}
Pages: {pages}
Rating: {rating}

Description:
{description}
"""
                )

            return "\n".join(books)

        except requests.exceptions.Timeout:
            if attempt < 2:
                continue
            return "Google Books API timed out."

        except requests.exceptions.ConnectionError:
            if attempt < 2:
                continue
            return "Unable to connect to Google Books."

        except Exception as e:
            return str(e)