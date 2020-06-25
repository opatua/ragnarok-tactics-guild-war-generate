from django.urls import path

from ragnarok import views

urlpatterns = [
    # Authentication
    path('', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),

    # Country URLs
    path('country/data', views.CountryDataView.as_view(), name='country_data'),
    path('country', views.CountryListView.as_view(), name='country_index'),
    path('country/create', views.CountryCreateView.as_view(), name='country_create'),
    path('country/<slug:pk>/update', views.CountryUpdateView.as_view(), name='country_update'),
    path('country/<slug:pk>/delete', views.CountryDeleteView.as_view(), name='country_delete'),

    path('character/data', views.CharacterDataView.as_view(), name='character_data'),
    path('character', views.CharacterListView.as_view(), name='character_index'),
    path('character/create', views.CharacterCreateView.as_view(), name='character_create'),
    path('character/<slug:pk>/update', views.CharacterUpdateView.as_view(), name='character_update'),
    path('character/<slug:pk>/delete', views.CharacterDeleteView.as_view(), name='character_delete'),

    path('guild-war-character/data', views.GuildWarCharacterDataView.as_view(), name='guild_war_character_data'),
    path('guild-war-character', views.GuildWarCharacterListView.as_view(), name='guild_war_character_index'),
    path('guild-war-character/create', views.GuildWarCharacterCreateView.as_view(), name='guild_war_character_create'),
    path('guild-war-character/<slug:pk>/update', views.GuildWarCharacterUpdateView.as_view(), name='guild_war_character_update'),
    path('guild-war/suggestion', views.GuildWarSuggestionView.as_view(), name='guild_war_suggestion'),

    # Resonance
    path('resonance/data', views.ResonanceDataView.as_view(), name='resonance_data'),
    path('resonance', views.ResonanceListView.as_view(), name='resonance_index'),
    path('resonance/create', views.ResonanceCreateView.as_view(), name='resonance_create'),
    path('resonance/<slug:pk>/update', views.ResonanceUpdateView.as_view(), name='resonance_update'),
    path('resonance/<slug:pk>/delete', views.ResonanceDeleteView.as_view(), name='resonance_delete'),

    # User URLs
    path('user/data', views.user.UserDataView.as_view(), name='user_data'),
    path('user', views.user.UserListView.as_view(), name='user_index'),
    path('user/create', views.user.UserCreateView.as_view(), name='user_create'),
    path('user/<slug:pk>/update', views.user.UserUpdateView.as_view(), name='user_update'),
    path('user/<slug:pk>/password', views.user.UserPasswordChangeView.as_view(), name='user_password'),
    path('user/<slug:pk>/delete', views.user.UserDeleteView.as_view(), name='user_delete'),
]
