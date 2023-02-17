from plyer import notification

title = 'Alert'

message= 'You used Laptop for long Time' 

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
