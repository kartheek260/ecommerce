from idlelib.multicall import r

from django.urls import path
from cartapp import views
app_name='cartapp'

urlpatterns=[

# path=('insertcart',views.insertcart),
 path('addcart/',views.addcart),
 path('insertcart/',views.insertcart),
 path('viewcart/',views.cartview),
path('delete/',views.delete),
path('modify/',views.modify),
path('cancel',views.cancel),
path('modifiedcart',views.modifiedcart),
]