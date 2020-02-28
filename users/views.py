from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages

from paytm_gateway.models import PaymentHistory
from .models import Profile, Wallet, TransferHistory
from .forms import ProfileForm, TransferForm, AddMoneyForm

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # profile = form.save(commit=False)
            # user.profile = request.user
            profile.save()
            return redirect('user-profile')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)


@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)

@login_required
def add_money(request):
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            return redirect('payment', amount=request.POST.get('amount'))
    else:
        form = AddMoneyForm()
    context = {
        'form': form
    }
    return render(request, 'users/add_money.html', context)

@login_required
def transfer_money(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # Check if user has enough balance in wallet
            from_wallet = Wallet.objects.get(user = request.user)
            if from_wallet.balance - form.cleaned_data.get('amount') < 0:
                return HttpResponse('<h1>You do not have enough Balance in your wallet</h1>')

            # Saving Money transfer record in TransferHistory
            try:
                to_user = get_object_or_404(User, username=request.POST.get('to_user'))
            except:
                return HttpResponse('<h1>No such user exist</h1>')
            transfer = TransferHistory.objects.create(from_user = request.user,
                    to_user = to_user,
                    amount = form.cleaned_data.get('amount'))
            transfer.save()

            # Deduct amount from the sender
            from_wallet.balance = from_wallet.balance - form.cleaned_data.get('amount')
            from_wallet.save()

            # Adding amount to the receiver
            to_wallet = Wallet.objects.get(user = to_user)
            to_wallet.balance = to_wallet.balance + form.cleaned_data.get('amount')
            to_wallet.save()
            messages.success(request, 'Transfer Success of: ₹{0} to {1} successfully'.format(
                form.cleaned_data.get('amount'),
                request.POST.get('to_user')))
            return redirect('user-profile')
    else:
        form = TransferForm()
    context = {
        'form': form
    }
    return render(request, 'users/transfer_money.html', context)

@login_required
def add_to_wallet_history(request):
    payments = get_list_or_404(PaymentHistory, user=request.user)
    context = get_paginator_context(request, payments, 10) # Show 10 Payments per page
    return render(request, 'users/payment_history.html', context)

@login_required
def transfer_history(request):
    transfers = get_list_or_404(TransferHistory, from_user=request.user)
    context = get_paginator_context(request, transfers, 10) # Show 10 Payments per page
    return render(request, 'users/transfer_history.html', context)

def get_paginator_context(request, data_list, count):
    paginator = Paginator(data_list, count) # Show 10 Orders per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return context