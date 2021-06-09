class News:
    '''
    News class to define News Object Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,name,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content