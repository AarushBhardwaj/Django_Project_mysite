from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm, EditProfileForm, ContactForm


# Create your views here.

def single_slug(request, single_slug):
	categories = [c.category_slug for c in TutorialCategory.objects.all()]
	if single_slug in categories:
		matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

		series_urls = {}
		for m in matching_series.all():
			part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
			series_urls[m] = part_one.tutorial_slug

		return render(request,
			          "main/category.html",
			          {"part_ones": series_urls})

	tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
		tutorial_from_Series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")

		this_tutorial_idx = list(tutorial_from_Series).index(this_tutorial)

		sidebar_list = {}
		if this_tutorial_idx > 0:
			sidebar_list['prev'] = tutorial_from_Series[this_tutorial_idx - 1]
		if this_tutorial_idx < len(tutorial_from_Series) - 1:
			sidebar_list['next'] = tutorial_from_Series[this_tutorial_idx + 1]

		return render(request,
			          "main/tutorial.html",
			          {"tutorial": this_tutorial,
			          "sidebar": tutorial_from_Series,
			          "this_tutorial_idx": this_tutorial_idx,
			          "sidebar_list": sidebar_list,
			          "has_next": this_tutorial_idx < len(tutorial_from_Series) - 1})

	return render(request, "main/404.html", status=404)


def homepage(request):
	return render(request=request,
		          template_name="main/categories.html",
		          context={"categories": TutorialCategory.objects.all})


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = NewUserForm

	return render(request,
				  "main/register.html",
				  context={"form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out Successfully!")
	return redirect("main:homepage")


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request=request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid Username or Password.")
		else:
			messages.error(request, "Invalid Username or Password.")

	form = AuthenticationForm()

	return render(request,
				  "main/login.html",
				  {"form": form})


@login_required(login_url='/login/')
def account(request):
	return render(request, "main/account.html")


@login_required(login_url='/login/')
def edit_profile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated successfully!")
			return redirect("main:account")
		else:
			messages.error(request, "Please correct the errors below.")
	else:
		form = EditProfileForm(instance=request.user)

	return render(request, "main/edit_profile.html", {"form": form})


@login_required(login_url='/login/')
def change_password(request):
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, "Password changed successfully!")
			return redirect("main:account")
		else:
			messages.error(request, "Please correct the errors below.")
	else:
		form = PasswordChangeForm(request.user)

	return render(request, "main/change_password.html", {"form": form})


def search(request):
	query = request.GET.get('q', '')
	results = []

	if query:
		# Search tutorials
		tutorials = Tutorial.objects.filter(
			Q(tutorial_title__icontains=query) |
			Q(tutorial_content__icontains=query)
		)
		for t in tutorials:
			results.append({
				'title': t.tutorial_title,
				'slug': t.tutorial_slug,
				'summary': t.tutorial_content[:150] + '...' if len(t.tutorial_content) > 150 else t.tutorial_content,
				'type': 'Tutorial',
			})

		# Search categories
		categories_qs = TutorialCategory.objects.filter(
			Q(tutorial_category__icontains=query) |
			Q(category_summary__icontains=query)
		)
		for c in categories_qs:
			results.append({
				'title': c.tutorial_category,
				'slug': c.category_slug,
				'summary': c.category_summary,
				'type': 'Category',
			})

		# Search series
		series = TutorialSeries.objects.filter(
			Q(tutorial_series__icontains=query) |
			Q(series_summary__icontains=query)
		)
		for s in series:
			first_tutorial = Tutorial.objects.filter(
				tutorial_series=s
			).order_by('tutorial_published').first()
			if first_tutorial:
				results.append({
					'title': s.tutorial_series,
					'slug': first_tutorial.tutorial_slug,
					'summary': s.series_summary,
					'type': 'Series',
				})

	return render(request, "main/search.html", {
		"query": query,
		"results": results,
		"categories": TutorialCategory.objects.all(),
	})


def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your message has been sent! We'll get back to you soon.")
			return redirect("main:contact")
		else:
			messages.error(request, "Please correct the errors below.")
	else:
		form = ContactForm()

	return render(request, "main/contact.html", {"form": form})


def custom_404(request, exception):
	return render(request, "main/404.html", status=404)


def custom_500(request):
	return render(request, "main/500.html", status=500)
