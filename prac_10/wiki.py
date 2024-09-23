import wikipediaapi

def main():
    wiki_wiki = wikipediaapi.Wikipedia('en')

    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wiki_wiki.page(title, autosuggest=False)

            if not page.exists():
                print(f'Page id "{title}" does not match any pages. Try another id!')
            else:
                print(f'{page.title}\n{page.summary}\n{page.fullurl}\n')
        except wikipediaapi.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipediaapi.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
