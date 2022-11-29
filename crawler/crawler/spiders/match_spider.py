import scrapy

class MatchSpider(scrapy.Spider):
    name = "match"

    years = [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978,
        1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018
    ]

    def start_requests(self):
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = "https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"
            yield scrapy.Request(url, self.parse)
        else:
            for year in self.years:
                url = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        matches = response.xpath("//div[@class='footballbox']")
        for match in matches:
            home = match.xpath(".//th[@class='fhome']/span//text()").extract()
            if len(home) > 1:
                home = home[0]

            score = match.xpath(".//th[@class='fscore']//text()").extract()
            if len(score) > 1:
                score = "".join(score)
            
            away = match.xpath(".//th[@class='faway']/span//text()").extract()
            if len(away) > 1:
                away = away[1]

            yield {
                "home": home,
                "score": score,
                "away": away,
            }
