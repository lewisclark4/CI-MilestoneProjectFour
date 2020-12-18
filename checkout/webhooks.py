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
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key, webhook_secret
        )
    except ValueError as e:
        return HttpResponse(content=e, status=400)
    
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(content=e, status=400)
    
    except Exception as e:
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response