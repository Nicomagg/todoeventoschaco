from django.conf.urls import patterns, include, url
from todoeventosweb import settings
from django.contrib import admin
from todoeventosweb import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "todoeventos.views.eventos"),
    url(r'^evento/(?P<id_evento>\d+)$', 'todoeventos.views.detalle_evento'),
   	url(r'^cartelera/(?P<id_cartelera>\d+)$', 'todoeventos.views.detalle_cartelera'),
   	url(r'^carteleras/' , 'todoeventos.views.carteleras'),
   	url(r'^noche/(?P<id_noche>\d+)$', 'todoeventos.views.detalle_noche'),
   	url(r'^noches/' , 'todoeventos.views.noches'),
    url(r'^galeria/(?P<id_galeria>\d+)$' , 'todoeventos.views.detalle_galeria'),
    url(r'^galerias/' , 'todoeventos.views.galerias'),
    url(r'^comentarios/' , 'todoeventos.views.comentarios'),

    url(r'^comercio/(?P<id_comercio>\d+)$' , 'todoeventos.views.detalle_comercio'),
    url(r'^servicio/(?P<id_servicio>\d+)$' , 'todoeventos.views.detalle_servicio'),    

)

# servir archivos estaticos en servidor de desarrollo
if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
          'document_root': settings.MEDIA_ROOT,}),
        )
