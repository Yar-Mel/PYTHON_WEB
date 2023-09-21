from random import shuffle
from django.shortcuts import render, get_object_or_404
from .models import Authors, Quotes
from django.core.paginator import Paginator


def main(request, page=1):
    all_quotes = Quotes.objects.all()
    all_quotes = list(all_quotes)
    shuffle(all_quotes)
    per_page = 10
    paginator = Paginator(all_quotes, per_page)
    quotes_on_page = paginator.page(page)
    context = {"content": quotes_on_page, "top_tags": top_tags()}
    return render(request, "quotes_app/main.html", context)


def tag_page(request, tag, page=1):
    quotes_with_tag = Quotes.objects.filter(tags__contains=[tag])
    per_page = 10
    paginator = Paginator(list(quotes_with_tag), per_page)
    quotes_on_page = paginator.page(page)
    context = {"content": quotes_on_page, "tag": tag, "top_tags": top_tags()}
    return render(request, "quotes_app/tag.html", context)


def author_page(request, fullname):
    author = get_object_or_404(Authors, fullname=fullname)
    return render(request, "quotes_app/author.html", {"author": author, "our_authors": our_authors()})


def quotes(request):
    quotes = Quotes.objects.all()
    return render(request, "quotes_app/quotes.html", {"quotes": quotes})


def top_tags():
    result = [
        "love",
        "inspirational",
        "life",
        "humor",
        "books",
        "reading",
        "friendship",
        "friends",
        "truth",
        "simile",
    ]
    return result


def our_authors():
    result = Authors.objects.all()
    return result


def delete_author(request, author_id):
    Authors.objects.filter(pk=author_id).delete()
    return main(request)


def delete_quote(request, quote_id):
    Quotes.objects.filter(pk=quote_id).delete()
    return main(request)
