import requests

def gen(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T=data.text
    except:
        T = "Error Occured"

    print(T)

if __name__ == "__main__":
    print("Welcome to weather forcast\n")
    city_name = input('Enter your city name: ')
    print(gen(city_name))