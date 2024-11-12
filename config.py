from website import Website

websites = [
    Website(
        name='PC Gamer',
        url='https://www.pcgamer.com/sitemap-2024-11.xml',
        absoluteUrl=True,
        titleTag='h1',
        bodyTags=['p'],
        imageTag='img',
        authorTag='a.link.author-byline__link',
        dateTag='time.relative-date',
        category='nav.breadcrumb > ol > li:first-child'
    ),
    Website(
        name='Digital Trends',
        url='https://www.digitaltrends.com/sitemap-all-articles_2024_10.xml',
        absoluteUrl=True,
        titleTag='h1.b-headline__title',
        bodyTags=['p'],
        imageTag='img',
        authorTag='a.author.url.fn',
        dateTag='time.b-byline__time.date.dtreviewed',
        category='span[itemprop="name"]'
    ),
    Website(
        name='CoinDesk',
        url='https://www.coindesk.com/',
        absoluteUrl=True,
        titleTag='title',
        bodyTags=['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
        imageTag='img',
        authorTag='div.at-authors',
        dateTag='span.typography__StyledTypography-sc-owin6q-0.iOUkmj',
        category='span.typography__StyledTypography-sc-owin6q-0.kRnPCi'
    ),
    Website(
        name='Crypto News',
        url='https://crypto.news/',
        absoluteUrl=True,
        titleTag='title',
        bodyTags=['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
        imageTag='img',
        authorTag='a.author-list__link',
        dateTag='time.post-detail__date',
        category='Crypto'   #default
    ),
]
