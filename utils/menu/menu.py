from pages.main import admins, components, heroes, profile, el11, provincia, region, votoblanco, participacion
from utils.menu.parser import parse_menu

main_pages = {
    "paneo-general": el11.paneo_general,
    "component-form": components.form,
    "resultados-provincia": provincia.provincia,
    "resultados-region": region.region,
    "resultados-participacion": participacion.participacion,
    "resultados-votoblanco": votoblanco.votoblanco,
    "component-extra": components.extra,
    "hero-thor": heroes.thor,
    "hero-flash": heroes.flash,
    "hero-cap": heroes.cap,
    "hero-goku": heroes.goku,
    "hero-netero": heroes.netero,
    "admins-list": admins.show,
    "profile": profile.show,
    "profile-settings": profile.settings,
    "profile-notifications": profile.notifications,
}

app_menu = parse_menu("app", main_pages)
