import logging
import requests
# from django.core.mail import BadHeaderError
from django.shortcuts import render
# from django.core.cache import cache
# from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
# from .tasks import notify_customers
# from templated_mail.mail import BaseEmailMessage

logger = logging.getLogger(__name__) #playground.views

# @cache_page(5 * 60)
# def say_hello(request):

#     # notify_customers.delay('Hello')
#     # try:

#     #     message = BaseEmailMessage(
#     #         template_name='emails/hello_email.html',
#     #         context={'name': 'Masab'}
#     #     )
#     #     message.send(['to@masab.com'])

#     # except BadHeaderError:
#     #     pass
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})

class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info("Calling httpbin")
            response = requests.get('https://httpbin.org/delay/2')
            logger.info("Received the response")
            data = response.json()
        except requests.ConnectionError:
            logger.critical("httpbin is offline")
        return render(request, 'hello.html', {'name': 'Masab'})        
