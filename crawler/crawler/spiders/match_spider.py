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
            url = "https://web.archive.org/web/20220809144459/https://www.thesoccerworldcups.com/world_cups/2022_results.php"
            yield scrapy.Request(url, self.parse)
        else:
            for year in self.years:
                url = f"https://www.thesoccerworldcups.com/world_cups/{year}_results.php"
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        year = response.url.split("/")[-1][0:4]
        matches = response.xpath("//div[contains(@class, 'game') and contains(@class, 'clearfix')]")
        for match in matches:
            home = match.xpath(".//div[@class='left margen-b2 clearfix']/div[contains(@class, 'left ')]/text()").extract()
            if len(home) > 1:
                home = home[0]

            score = match.xpath(".//div[@class='left a-center margen-b3 clearfix']/div[@class='left wpx-60']/a/text()").extract()
            if len(score) > 1:
                score = "".join(score)
            
            away = match.xpath(".//div[@class='left a-left margen-b2 clearfix']/div[contains(@class, 'left ')]/text()").extract()
            if len(away) > 1:
                away = away[1]

            yield {
                "home": home,
                "score": score,
                "away": away,
                "year": year,
            }
