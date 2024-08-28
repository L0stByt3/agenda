from django.http import HttpResponse
from django.urls import reverse

def inicio(request):
    urls = {
        "Redoc": reverse('redoc'),
        "Swagger UI": reverse('swagger-ui'),
    }

    html_content = """
    <html>
    <head>
        <style>
            body {{
                background-color: #000;
                color: #fff;
                font-family: Arial, sans-serif;
                height: 100vh;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 20px;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 10px 0;
            }}
            a {{
                color: #00ffff;
                text-decoration: none;
                font-size: 1.5em;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div>
            <h1>Bienvenido a tu agendita API</h1>
            <ul>
                {items}
            </ul>
        </div>
    </body>
    </html>
    """


    items = "".join(f"<li><a href='{url}'>{name}</a></li>" for name, url in urls.items())

    html_content = html_content.format(items=items)

    return HttpResponse(html_content)
