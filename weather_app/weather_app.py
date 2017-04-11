import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'condition, temp, scale, location')

def main():
    print_header()
    postal_code = input('What postal code do you want the weather for(R4H 1E9)?')
    html = get_html_from_web(postal_code)
    report = parse_html(html)

    print('The temp in {} is {} {} and it is {}'.format(
        report.location,
        report.temp,
        report.scale,
        report.condition
    ))



def print_header():
    """
    Prints header for app
    :return: 
    """
    print('-------------------------------------------')
    print('         Weather APP')
    print('-------------------------------------------')
    print()


def get_html_from_web(postal_code):
    """
    gets html weather for postal code
    :param postal_code: 
    :return: 
    """
    postal_code = postal_code.replace(" ", "")
    url = "https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}".format(postal_code)
    response = requests.get(url)
    return response.text


def parse_html(html):
    """
    pares html and returns a named tuple with the current conditions
    :param html: 
    :return: 
    """
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    location = cleanup_text(location)
    location = find_city_and_province_from_location(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(condition=condition, temp=temp, scale=scale, location=location)

    return report


def find_city_and_province_from_location(loc: str):
    """
    returns just the first line
    :param loc: 
    :return: 
    """
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    """
    strips whitespace
    :param text: 
    :return: 
    """
    if not text:
        return text

    text = text.strip()
    return text

if __name__ == '__main__':
    main()