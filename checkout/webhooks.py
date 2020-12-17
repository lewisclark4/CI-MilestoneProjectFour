# https://stripe.com/docs/webhooks/build


from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import json
import stripe

@require_POST
@csrf_exempt
def webhook(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET_KEY

    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key, webhook_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(content=e, status=400)
    
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('success!')
    return HttpResponse(status=200)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object 

    elif event.type == 'payment_method.attached':
        payment_method = event.data.object 

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)