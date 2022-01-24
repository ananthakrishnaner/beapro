from .models import ConnectionRequest

def get_connection_request_or_false(sender,receiver):
    try:
        return ConnectionRequest.objects.get(sender=sender,receiver=receiver,is_active=True)
    except ConnectionRequest.DoesNotExist:
        return False