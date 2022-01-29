# Import external modules.
import requests as req
from bs4 import BeautifulSoup
# Constants
_100_MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def run_main():
    _100_movies_html_str = req.get(_100_MOVIES_URL).text
    movies_soup = BeautifulSoup(markup=_100_movies_html_str, features='html.parser')
    all_movies_tags_list = movies_soup.find_all(name='h3', class_='title')
    # Create a list of all movies and remove the right character from de number.
    all_movies_list = [
        (int(item.getText().split()[0][:-1]), ' '.join(item.getText().split()[1:]))
        for item in all_movies_tags_list
    ]
    all_movies_list.sort()
    with open(file='best_100_files.md', mode='w') as a_file:
        a_file.write('##The best 100 movies list from according to "Empire" magazine.\n')
        for item in all_movies_list:
            if item[0] <= 10:
                a_file.write(f'- {item[0]}: **_{item[1]}_**.\n')
            else:
                a_file.write(f'- {item[0]}: {item[1]}.\n')
    pass
    return


if __name__ == '__main__':
    run_main()
