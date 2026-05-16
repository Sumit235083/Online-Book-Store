from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from books.models import Book
from .models import CartItem


@login_required
def add_to_cart(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        book=book
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart_view(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total_price = 0

    for item in cart_items:
        total_price += item.book.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart/cart.html', context)


@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    item.delete()

    return redirect('cart')