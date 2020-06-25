from factorial.factorialclient import FactorialClient
from factorial.exceptions import AuthenticationTokenNotFound, ApiError, UserNotLoggedIn
from datetime import date
import calendar
import os
from constants import BASE_PROJECT

if __name__ == '__main__':
    try:
        week = calendar.day_name[date.today().weekday()];

        if week == "Saturday" or week == "Sunday":
            print ("Fin de semana")
        elif week == "Friday":
            config = os.path.join(BASE_PROJECT, 'viernes.json')
        else:
            config = os.path.join(BASE_PROJECT, 'lunes_jueves.json')

        client = FactorialClient.load_from_settings(config)
        client.worked_day(date.today(), config)
    except AuthenticationTokenNotFound as err:
        print(f"Can't retrieve the login token: {err}")
    except UserNotLoggedIn as err:
        print(f'User not logged in: {err}')
    except ApiError as err:
        print(f"Api error: {err}")
