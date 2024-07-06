# Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)

# Parameters:

# title (str) – Title of the notification
# message (str) – Message of the notification
# app_name (str) – Name of the app launching this notification
# app_icon (str) – Icon to be displayed along with the message
# timeout (int) – time to display the message for, defaults to 10
# ticker (str) – text to display on status bar as the notification arrives
# toast (bool) – simple Android message instead of full notification

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        app_name='Task Manager',
        title = 'Reminder to shit!',
        ticker = 'reminder',
        message = 'It\'s healthy to poop between three times a day and three times a week.',
        app_icon = 'D:\Programming\myself\Python\Tasks\p00p.ico',
        timeout = 10

    )