from django.conf.urls import url

from . import views

app_name = 'djcytoscape'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate/(?P<num_nodes>[0-9]+)/$', views.generate, name='generate'),
    url(r'^generate_tree/(?P<num_nodes>[0-9]+)/$', views.generate_tree, name='generate_tree'),
    url(r'^(?P<scape_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<scape_id>[0-9]+)/graph/$', views.graph, name='graph'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ScapeUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ScapeDelete.as_view(), name='delete'),

]
