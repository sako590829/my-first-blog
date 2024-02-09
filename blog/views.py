from django.shortcuts import render

# Create your views here.
def post_list(reqest):
    return render(reqest,'blog/post_box.html',{})
