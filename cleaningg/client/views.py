from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from . forms import ProfileForm, CustomUserChangeForm, CustomPasswordChangeForm
from . forms import OrderForm, EditOrderForm, ProposalForm, ReviewForm
from . models import Order, Proposal, Profile, User


@login_required
def make_review(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.profile = user.profile
            review.reviewer = request.user
            review.save()

            if request.user.profile.is_cleaner:
                return redirect('cleaner-home')
            else:
                return redirect('client-home')

    form = ReviewForm()

    return render(request, 'client/make_review.html', {
        'form': form
    })


@login_required
def home_redirect(request):
    user = request.user

    if user.profile.is_cleaner:
        return redirect('cleaner-home')
    else:
        return redirect('client-home')


@login_required
def waiting_response(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'client/cleaner_waiting_response.html', {
        'order': order
    })


@login_required
def execution_page(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        order.is_done_client = True
        order.save()
        order.delete()
        return redirect('make-review', order.taken_by.id)

    return render(request, 'client/execution_page.html', {
        'order': order
    })


@login_required
def show_proposals(request, pk):
    order = get_object_or_404(Order, pk=pk)
    proposals = order.proposals_list.all()

    if request.method == 'POST':
        selected_proposal_id = request.POST.get('selected_proposal_id')
        
        Proposal.objects.filter(order=order).exclude(id=selected_proposal_id).delete()
        order.is_taken = True
        order.accepted += 1
        order.save()
        return redirect('execution-page', pk=order.id)

    return render(request, 'client/show_proposals.html', {
        'order': order,
        'proposals': proposals
    })


@login_required
def make_proposal(request, pk):
    order = get_object_or_404(Order, pk=pk)
    user = request.user


    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            order.proposals += 1
            order.save()
            proposal = form.save(commit=False)
            proposal.order = order
            proposal.created_by = user
            proposal.save()
            order.proposals_list.add(proposal)
            order.taken_by = user
            order.save()
            next_url = reverse('waiting-response', kwargs={'pk': order.pk})
            return redirect(next_url)
    else:
        form = ProposalForm()

    return render(request, 'client/make_proposal.html', {
        'order': order,
        'form': form,
    })


def cleaner_home(request):
    available_orders = Order.objects.filter(is_taken=False)
    user_proposals = Proposal.objects.filter(created_by=request.user)

    order_info = []
    for order in available_orders:
        user_has_proposal = user_proposals.filter(order=order).exists()
        order_info.append({'order': order, 'user_has_proposal': user_has_proposal})

    if request.method == 'POST':
        order = Order.objects.filter(taken_by=request.user).first()
        order.is_done_cleaner = True
        order.save()
        return redirect('make-review', order.created_by.id)

    order = Order.objects.filter(taken_by=request.user).first()
    return render(request, 'client/cleaner_base.html', {
        'available_orders': order_info,
        'order': order
    })


@login_required
def client_home(request):
    orders = Order.objects.filter(created_by=request.user)

    return render(request, 'client/base.html', {
        'orders': orders
    })


@login_required
def order_creation(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user

            your_price = form.cleaned_data['client_price']
            package = form.cleaned_data['package']

            if package and your_price and your_price < package.price:
                form.add_error('client_price', 'Your price cannot be lower than the package price.')
                return render(request, 'client/order.html', {'form': form})

            order.save()
            return redirect('details', pk=order.id)
        else:
            print("Form is not valid")
    
    else:
        form = OrderForm()

    return render(request, 'client/order.html', {'form': form})


@login_required
def details(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'client/details.html', {
        'order': order
    })


@login_required
def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditOrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()

            return redirect('details', pk=order.id)
    
    else:
        form = EditOrderForm(instance=order)
    
    return render(request, 'client/edit.html', {
        'form': form,
        'order': order
    })


@login_required
def delete(request, pk):
    order = get_object_or_404(Order, pk=pk, created_by=request.user)
    order.delete()

    return redirect('client-home')


@login_required
def settings(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('client-home')

        
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('client-home')
        
    else:
        user_form = CustomUserChangeForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'client/settings.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def password_change(request):

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            print(form.errors)
        
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'client/password.html', {
        'form': form
    })