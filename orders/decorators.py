from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def customer_only(view_func):
    """
    Restrict access to a customer's own orders.
    """
    @wraps(view_func)
    def _wrapped_view(viewset, request, *args, **kwargs):
        # Check if the user is a superuser
        if request.user.is_superuser:
            return view_func(viewset, request, *args, **kwargs)

        # Check if the user is a customer
        if not hasattr(request.user, 'customer'):
            return Response(
                {"detail": "You do not have permission to access this resource."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Restrict access to the customer's own data
        order = viewset.get_object()
        if order.customer.user != request.user:
            return Response(
                {"detail": "You do not have permission to view this order."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return view_func(viewset, request, *args, **kwargs)

    return _wrapped_view
