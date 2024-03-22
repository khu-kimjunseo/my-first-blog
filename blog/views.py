from django.shortcuts import render

def post_list(req):
  return render(req, 'blog/post_list.html', {})