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

    #Character
    path('character/data', views.CharacterDataView.as_view(), name='character_data'),
    path('character', views.CharacterListView.as_view(), name='character_index'),
    path('character/create', views.CharacterCreateView.as_view(), name='character_create'),
    path('character/<slug:pk>/update', views.CharacterUpdateView.as_view(), name='character_update'),
    path('character/<slug:pk>/delete', views.CharacterDeleteView.as_view(), name='character_delete'),

    #Essence
    path('essence/data', views.EssenceDataView.as_view(), name='essence_data'),
    path('essence', views.EssenceListView.as_view(), name='essence_index'),
    path('essence/create', views.EssenceCreateView.as_view(), name='essence_create'),
    path('essence/<slug:pk>/update', views.EssenceUpdateView.as_view(), name='essence_update'),
    path('essence/<slug:pk>/delete', views.EssenceDeleteView.as_view(), name='essence_delete'),

    #Guild War
    path('guild-war-character/data', views.GuildWarCharacterDataView.as_view(), name='guild_war_character_data'),
    path('guild-war-character', views.GuildWarCharacterListView.as_view(), name='guild_war_character_index'),
    path('guild-war-character/create', views.GuildWarCharacterCreateView.as_view(), name='guild_war_character_create'),
    path('guild-war-character/<slug:pk>/update', views.GuildWarCharacterUpdateView.as_view(), name='guild_war_character_update'),
    path('guild-war/suggestion', views.GuildWarSuggestionView.as_view(), name='guild_war_suggestion'),

    # Monster
    path('monster/data', views.MonsterDataView.as_view(), name='monster_data'),
    path('monster', views.MonsterListView.as_view(), name='monster_index'),
    path('monster/create', views.MonsterCreateView.as_view(), name='monster_create'),
    path('monster/<slug:pk>/update', views.MonsterUpdateView.as_view(), name='monster_update'),
    path('monster/<slug:pk>/delete', views.MonsterDeleteView.as_view(), name='monster_delete'),

    # Resonance
    path('resonance/data', views.ResonanceDataView.as_view(), name='resonance_data'),
    path('resonance', views.ResonanceListView.as_view(), name='resonance_index'),
    path('resonance/create', views.ResonanceCreateView.as_view(), name='resonance_create'),
    path('resonance/<slug:pk>/update', views.ResonanceUpdateView.as_view(), name='resonance_update'),
    path('resonance/<slug:pk>/delete', views.ResonanceDeleteView.as_view(), name='resonance_delete'),

    #Simulator
    path('simulator', views.SimulatorListView.as_view(), name='simulator_index'),
    path('simulator/create', views.SimulatorCreateView.as_view(), name='simulator_create'),

    # User URLs
    path('user/data', views.user.UserDataView.as_view(), name='user_data'),
    path('user', views.user.UserListView.as_view(), name='user_index'),
    path('user/create', views.user.UserCreateView.as_view(), name='user_create'),
    path('user/<slug:pk>/update', views.user.UserUpdateView.as_view(), name='user_update'),
    path('user/<slug:pk>/password', views.user.UserPasswordChangeView.as_view(), name='user_password'),
    path('user/<slug:pk>/delete', views.user.UserDeleteView.as_view(), name='user_delete'),
]
