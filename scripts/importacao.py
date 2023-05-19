from datetime import date
def main(app):
    limite = 5
    folder = app.unrestrictedTraverse("Portal/agenda")
    site = app.unrestrictedTraverse("Portal") 
    url = site.absolute_url()
    catalog = site.portal_catalog
    date_range = {
    'query': (
        date(2018, 1, 1),
        date(2023, 5, 16),
    ),
    'range': 'min:max',
}
    results = catalog.searchResults({
        'portal_type': 'Event',
        'review_state': 'published', 
        'effective': date_range,
        #'sort_limit': limite,
        'sort_on': 'start', 
        'sort_order': 'descending'})
    texto = "{title};{data_inicio};{data_fim};{data_publicacao};{local}"
    cabecalho = texto.format(
            title = "Titulo",
            data_inicio = "Data de inicio",
            data_fim = "Data de fim",
            local = "Local",
            data_publicacao = "Data publicacao" )
    print(cabecalho)
    for i in results:        
        retorno = texto.format(
            title = i["Title"],
            data_inicio = i["start"],
            data_fim = i["end"],
            local = ( i["Description"] if len(i["Description"]) > 0 else "Prefeitura" ),
            data_publicacao = i["EffectiveDate"] )
        print(retorno)

if "app" in locals():
    main(app)
