
from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name='about'),
   
 
    path('sports/', views.sports_homepage, name='sports'),                          # =========== Start of yapper urls
    path('sports/<slug:sports_name_slug>/', views.sports_profile, name='sports_name'),        
    path('breeds/', views.breed_homepage ,name='breeds'),
    path('breeds/<slug:breed_name_slug>/', views.breed_profile ,name='breed_profile'),             
    path("breeds/<slug:breed_name_slug>/<slug:dog_slug>/", views.dog_profile ,name='dog_profile'), 
    path('competitions/', views.competition_homepage, name='competitions'), 
    path('competitions/<slug:competition_name_slug>/', views.competition_profile ,name='competition_name'),    
    path('help/', views.faq ,name='help'),
    path('register_profile/', views.register_profile, name='register_profile'),  
    path('user/<slug:user_name_slug>/', views.user_profile, name='user'),                                                 # Requires dynamic slug field
    path('add_dog/', views.add_dog, name='add_dog'),
    path('user/<slug:user_name_slug>/edit/', views.edit_profile, name='edit'),
    path('register_competition/', views.add_competition, name='register_competition'),
    path('explore/', views.explore, name='explore'),
    path('user/<slug:user_name_slug>/edit_competition/', views.edit_competition, name='edit_competition'),

    path('follow_breed/', views.FollowBreedView.as_view(), name='follow_breed'),
    path('follow_dog/', views.FollowDogView.as_view(), name='follow_dog'),
    path('follow_sport/', views.FollowSportView.as_view(), name='follow_sport'),
]
