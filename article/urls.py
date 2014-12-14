from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^create/$', 'article.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', 'article.views.delete_comment'),
    url(r'^add_commentsecond/(?P<article_id>\d+)/$', 'article.views.add_commentsecond'),
    url(r'^delete_commentsecond/(?P<article_id>\d+)/$', 'article.views.delete_commentsecond'),


)
